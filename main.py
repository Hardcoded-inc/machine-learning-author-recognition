import pandas as pd
import numpy as np

def main():

    # Data importing
    artists_df = pd.read_csv("./artists-data.csv", usecols=["Artist", "Link"])
    songs_df = pd.read_csv("./lyrics-data.csv", usecols=[ "ALink", "Lyric"])
    songs_df.rename(columns={"ALink": "Link"}, inplace=True)

    # Merge artists with songs lyrics
    df = pd.merge(songs_df, artists_df, on =["Link"], how="inner")
    df.drop(columns=["Link"], inplace=True)

    df['Lyric'] = pd.Series(df['Lyric'], dtype="string")
    df['Artist'] = pd.Series(df['Artist'], dtype="string")



    # ----------------------------- #
    #       Lyrics processing       #
    # ----------------------------- #


    nan_value = float("NaN")
    df.drop_duplicates(inplace=True)
    df.replace("", nan_value, inplace=True)
    df.dropna(inplace=True)


    # lowercase
    # ---------
    df["Lyric"] = df["Lyric"].apply(lambda lyric: lyric.lower())





    # remove brackets/parenthesis/braces
    df["Lyric"] = df["Lyric"].str.replace('\[.*\]', '')
    df["Lyric"] = df["Lyric"].str.replace('\(.*\)', '')
    df["Lyric"] = df["Lyric"].str.replace('\{.*\}', '')
    df["Artist"] = df["Artist"].str.replace('\(.*\)', '')

    # Remove incurable data (open parantheses)
    df = df[~df["Lyric"].str.contains("\[|\]|\(|\)|\{|\}")]


    # Remove written by
    # df["Lyric"] = df["Lyric"].str.replace(r'written by.*(?=\.\.)\.\.', '')

    # Remove punctuations
    df["Lyric"] = df["Lyric"].str.replace('[^\w\s]|_', '')

    # Remove phrases with numbers
    df['Lyric'] = df['Lyric'].str.replace('\w*\d\w*', '')

    # Remove empty records
    print(df.shape)
    df = df[df["Lyric"].str.contains("[a-zA-Z]")]
    print(df.shape)



    # print(df.loc[84530:84540, :])
    # df["Lyric"].to_csv("./test.csv")








if __name__ == "__main__":
    main()
    print("------ Done -------")
