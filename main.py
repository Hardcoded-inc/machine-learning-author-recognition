
def main():
    import sys
    flags = {
        "verbose": True if "-v" in sys.argv else False
    }

    # ----------------------------- #
    #        Data importing         #
    # ----------------------------- #

    import pandas as pd
    from loader import Loader
    loader = Loader(flags)

    loader.read_csv("artists", "./artists-data.csv", ["Artist", "Link"])
    loader.read_csv("lyrics", "./lyrics-data.csv.zip", [ "ALink", "Lyric"])
    loader.rename_cols("lyrics", {"ALink": "Link"})
    loader.merge("artists", "lyrics", on_col=["Link"])
    df = loader.get_df("artists_lyrics")


    df['Lyric'] = pd.Series(df['Lyric'], dtype="string")
    df['Artist'] = pd.Series(df['Artist'], dtype="string")


    # ----------------------------- #
    #       Lyrics processing       #
    # ----------------------------- #
#
#
    from normalizer import Normalizer
    normalizer = Normalizer(flags)

    normalizer.drop_duplicates(df)
    normalizer.drop_nans(df)
    normalizer.lowercase(df)
    normalizer.remove_inbrackets_text(df)
    normalizer.drop_written_by(df)
    normalizer.remove_punctuations(df)
    normalizer.remove_phrases_with_numbers(df)
    normalizer.drop_empty_records(df)

    print("- Saving checkpont 1")
    df.to_csv("./checkpoint1.csv")


    # df = pd.read_csv("./checkpoint1.csv")



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








if __name__ == "__main__":
    main()
    print("------ Done -------")
