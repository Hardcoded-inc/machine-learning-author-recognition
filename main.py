import pandas as pd
import numpy as np

def main():

    # ----------------------------- #
    #        Data importing         #
    # ----------------------------- #

    from loader import Loader
    loader = Loader()

    loader.read_csv("artists", "./artists-data.csv", ["Artist", "Link"])
    loader.read_csv("lyrics", "./lyrics-data.csv.zip", [ "ALink", "Lyric"])
    loader.rename_cols("lyrics", {"ALink": "Link"})

    df = loader.merge_and_return("artists", "lyrics", on_col=["Link"])


    df['Lyric'] = pd.Series(df['Lyric'], dtype="string")
    df['Artist'] = pd.Series(df['Artist'], dtype="string")


    # ----------------------------- #
    #       Lyrics processing       #
    # ----------------------------- #


    nan_value = float("NaN")
    df.drop_duplicates(inplace=True)
    df.replace("", nan_value, inplace=True)
    df.dropna(inplace=True)
#
#
    from normalizer import Normalizer
    normalizer = Normalizer()

    normalizer.lowercase(df)
    normalizer.remove_inbrackets_text(df)
    normalizer.remove_written_by(df)
    normalizer.remove_punctuations(df)
    normalizer.remove_phrases_with_numbers(df)
    normalizer.remove_empty_records(df)




#     # stopwords
#     # ---------
#     import nltk
#     from nltk.corpus import stopwords
#
#     nltk.download('stopwords')
#     stop = stopwords.words('english')
#
#
#     df['stopwords'] = df["Lyric"].apply(lambda x: len([x for x in x.split() if x in stop]))
#     print(df[['Lyric','stopwords']].head())



    # print(df.loc[84530:84540, :])
    # df["Lyric"].to_csv("./test.csv")








if __name__ == "__main__":
    main()
    print("------ Done -------")
