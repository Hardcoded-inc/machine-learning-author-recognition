class Normalizer:
    def lowercase(self, df):
        df["Lyric"] = df["Lyric"].apply(lambda text: text.lower())


    def remove_inbrackets_text(self, df):
        # remove brackets/parenthesis/braces
        df["Lyric"] = df["Lyric"].str.replace('\[.*\]', '')
        df["Lyric"] = df["Lyric"].str.replace('\(.*\)', '')
        df["Lyric"] = df["Lyric"].str.replace('\{.*\}', '')
        df["Artist"] = df["Artist"].str.replace('\(.*\)', '')

        # Remove incurable data (open parantheses)
        df = df[~df["Lyric"].str.contains("\[|\]|\(|\)|\{|\}")]


    def remove_written_by(self, df):
        # Remove written by
        df = df[~df["Lyric"].str.contains("written by")]
        # df["Lyric"] = df["Lyric"].str.replace(r'written by.*(?=\.\.)\.\.', '')


    def remove_punctuations(self, df):
        df["Lyric"] = df["Lyric"].str.replace('[^\w\s]|_', '')


    def remove_phrases_with_numbers(self, df):
        df['Lyric'] = df['Lyric'].str.replace('\w*\d\w*', '')


    def remove_empty_records(self, df):
        df = df[df["Lyric"].str.contains("[a-zA-Z]")]
