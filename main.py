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
    df = loader.get_df()

    # ----------------------------- #
    #       Lyrics processing       #
    # ----------------------------- #

#
    from normalizer import Normalizer
    normalizer = Normalizer(flags)

    # normalizer.drop_duplicates(df)
    # normalizer.drop_nans(df)
    normalizer.lowercase(df)
    normalizer.remove_inbrackets_text(df)
    normalizer.drop_written_by(df)
    normalizer.remove_punctuations(df)
    normalizer.remove_phrases_with_numbers(df)
    normalizer.drop_empty_records(df)
#
#     print("- Saving checkpont 1")
#     df.to_csv("./checkpoint1.csv")
#
#
#     loader.read_csv("checkpoint1.csv", cols=["artist", "song", "seq"])
#     loader.convert_cols_to_dtype(["artist", "song", "seq"], "string")
#     df = loader.get_df()

    normalizer.remove_stop_words(df)

#
#     print("- Saving checkpont 2")
#     df.to_csv("./checkpoint2.csv")




if __name__ == "__main__":
    main()
    print("------ Done -------")
