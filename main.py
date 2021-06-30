import pandas as pd
import numpy as np
import sys

def main():
    flags = {
        "verbose": True if "-v" in sys.argv else False
    }

    # ----------------------------- #
    #        Data importing         #
    # ----------------------------- #
    from loader import Loader

    loader = Loader(flags)
    loader.read_csv("dataset.zip", cols=["artist", "song", "seq"])
    loader.convert_cols_to_dtype(["artist", "song", "seq"], "string")
    df = loader.get_df().iloc[:10000,:].copy()

    # ----------------------------- #
    #       Lyrics processing       #
    # ----------------------------- #

#
    from normalizer import Normalizer
    normalizer = Normalizer(flags)
#
    # normalizer.drop_duplicates(df)
    # normalizer.drop_nans(df)
    normalizer.lowercase(df)
    normalizer.remove_inbrackets_text(df)
    normalizer.drop_written_by(df)
    normalizer.remove_punctuations(df)
    normalizer.remove_phrases_with_numbers(df)
    normalizer.drop_empty_records(df)
    normalizer.remove_stop_words(df)
    normalizer.remove_common_words(df)
    normalizer.remove_rare_words(df)
    normalizer.stem(df)
    normalizer.tokenize(df)


    print("- Saving processed data")
    df.to_csv("./checkpoint3.csv")


if __name__ == "__main__":
    main()
    print("------ Done -------")
