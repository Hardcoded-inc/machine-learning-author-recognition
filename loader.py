import pandas as pd

class Loader:
    def __init__(self):
        self.fields = {}

    def read_csv(self, field_name, path, cols):
        self.fields[field_name] = pd.read_csv(path, usecols=cols)

    def rename_cols(self, field_name, cols):
        self.fields[field_name].rename(columns=cols, inplace=True)

    def merge_and_return(self, field_name1, field_name2, on_col):
        df = pd.merge(self.fields[field_name1],  self.fields[field_name2], on=on_col, how="inner")
        df.drop(columns=on_col, inplace=True)
        return df







