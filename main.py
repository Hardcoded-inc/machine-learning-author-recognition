import pandas as pd
import numpy as np

def main():
    print("Hello World")

    artists_df = pd.read_csv("./artists-data.csv", usecols=["Artist", "Link"])
    songs_df = pd.read_csv("./lyrics-data.csv", usecols=[ "ALink", "SName", "Lyric"])
    songs_df.rename(columns={"ALink": "Link"}, inplace=True)

    df = pd.merge(songs_df, artists_df, on =["Link"])
    df.drop(columns=["Link"], inplace=True)
    print(df.shape)








if __name__ == "__main__":
    main()
