import nltk
from nltk.corpus import stopwords
import pandas as pd
from textblob import TextBlob

nltk.download('stopwords')
stop = stopwords.words('english')


class Normalizer:
    def __init__(self, flags):
        self.verbose = flags["verbose"]

    def lowercase(self, df, col="seq"):
        if(self.verbose):
            print(f"- Lowercasing.")

        df[col] = df[col].apply(lambda text: text.lower())

    def remove_inbrackets_text(self, df, col="seq"):
        if(self.verbose):
            print(f"- Removing inbrackets text.")

        # remove brackets/parenthesis/braces
        df[col] = df[col].str.replace('\[.*\]', '')
        df[col] = df[col].str.replace('\(.*\)', '')
        df[col] = df[col].str.replace('\{.*\}', '')

        # Remove incurable data (open parantheses)
        df = df[~df[col].str.contains("\[|\]|\(|\)|\{|\}")]


    def remove_punctuations(self, df, col="seq"):
        if(self.verbose):
            print(f"- Removing punctuation.")

        df[col] = df[col].str.replace('[^\w\s]|_', '')


    def remove_phrases_with_numbers(self, df, col="seq"):
        if(self.verbose):
            print(f"- Removing phrases with numbers.")

        df[col] = df[col].str.replace('\w*\d\w*', '')



    def drop_empty_records(self, df, col="seq"):
        if(self.verbose):
            print(f"- Dropping empty records.")

        df = df[df[col].str.contains("[a-zA-Z]")]


    def drop_duplicates(self, df, col="seq"):
        if(self.verbose):
            print(f"- Dropping duploicated.")

        df.drop_duplicates(inplace=True)


    def drop_nans(self, df, col="seq"):
        if(self.verbose):
            print(f"- Dropping NaNs.")

        nan_value = float("NaN")
        df.replace("", nan_value, inplace=True)
        df.dropna(inplace=True)


    def drop_written_by(self, df, col="seq"):
        if(self.verbose):
            print(f"- Dropping 'written by' rows.")

        # Remove written by
        df = df[~df[col].str.contains("written by")]
        # df[col] = df[col].str.replace(r'written by.*(?=\.\.)\.\.', '')


    def remove_stop_words(self, df, col="seq"):
        self.drop_nans(df)
        if self.verbose :
            print(f"- Removing stopwords.")

        df[col] = df[col].apply(lambda x: " ".join(x for x in x.split() if x not in stop))


    def remove_common_words(self, df, col="seq"):
        if self.verbose :
            print(f"- Removing common words.")

        freq = pd.Series(' '.join(df[col]).split()).value_counts()
        freq = freq[freq > 6000]

        freq = list(freq.index)
        df[col] = df[col].apply(lambda x: " ".join(x for x in x.split() if x not in freq))


    def remove_rare_words(self, df, col="seq"):
        if self.verbose :
            print(f"- Removing rare words.")

        freq = pd.Series(' '.join(df[col]).split()).value_counts()
        freq = freq[freq < 3]

        freq = list(freq.index)
        df[col] = df[col].apply(lambda x: " ".join(x for x in x.split() if x not in freq))


    def tokenize(self, df, col="seq"):
        if self.verbose :
            print(f"- Tokenizing lyrics.")

        df[col] = df[col].apply(lambda x: str(TextBlob(x).words))
