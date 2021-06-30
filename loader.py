import pandas as pd

class Loader:
    def __init__(self, flags):
        self.fields = {}
        self.verbose = flags["verbose"]

    def read_csv(self, field_name, path, cols):
        if(self.verbose):
            print(f"- Loading {field_name}.")

        self.fields[field_name] = pd.read_csv(path, usecols=cols)


    def rename_cols(self, field_name, cols):
        if(self.verbose):
            print(f"- Renamming {field_name}.")

        self.fields[field_name].rename(columns=cols, inplace=True)


    def merge_and_return(self, field_name1, field_name2, on_col):
        df = pd.merge(self.fields[field_name1],  self.fields[field_name2], on=on_col, how="inner")
        if(self.verbose):
            print(f"- Merging {field_name1} with {field_name2}.")

        df.drop(columns=on_col, inplace=True)

        return df







