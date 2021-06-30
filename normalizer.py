class Normalizer:
    def __init__(self, flags):
        self.verbose = flags["verbose"]

    def lowercase(self, df):
        if(self.verbose):
            print(f"- Lowercasing.")

        df["Lyric"] = df["Lyric"].apply(lambda text: text.lower())

    def remove_inbrackets_text(self, df):
        if(self.verbose):
            print(f"- Removing inbrackets text.")

        # remove brackets/parenthesis/braces
        df["Lyric"] = df["Lyric"].str.replace('\[.*\]', '')
        df["Lyric"] = df["Lyric"].str.replace('\(.*\)', '')
        df["Lyric"] = df["Lyric"].str.replace('\{.*\}', '')
        df["Artist"] = df["Artist"].str.replace('\(.*\)', '')

        # Remove incurable data (open parantheses)
        df = df[~df["Lyric"].str.contains("\[|\]|\(|\)|\{|\}")]


    def remove_punctuations(self, df):
        if(self.verbose):
            print(f"- Removing punctuation.")

        df["Lyric"] = df["Lyric"].str.replace('[^\w\s]|_', '')


    def remove_phrases_with_numbers(self, df):
        if(self.verbose):
            print(f"- Removing phrases with numbers.")

        df['Lyric'] = df['Lyric'].str.replace('\w*\d\w*', '')



    def drop_empty_records(self, df):
        if(self.verbose):
            print(f"- Dropping empty records.")

        df = df[df["Lyric"].str.contains("[a-zA-Z]")]


    def drop_duplicates(self, df):
        if(self.verbose):
            print(f"- Dropping duploicated.")

        df.drop_duplicates(inplace=True)


    def drop_nans(self, df):
        if(self.verbose):
            print(f"- Dropping NaNs.")

        nan_value = float("NaN")
        df.replace("", nan_value, inplace=True)
        df.dropna(inplace=True)


    def drop_written_by(self, df):
        if(self.verbose):
            print(f"- Dropping 'written by' rows.")

        # Remove written by
        df = df[~df["Lyric"].str.contains("written by")]
        # df["Lyric"] = df["Lyric"].str.replace(r'written by.*(?=\.\.)\.\.', '')
