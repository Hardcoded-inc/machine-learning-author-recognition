import pandas as pd

class Loader:
    def __init__(self, flags):
        self.fields = {}
        self.verbose = flags["verbose"]


    def read_csv(self, path, cols):
        if(self.verbose):
            print(f"- Loading {path}.")

        self.dataset = pd.read_csv(path, usecols=cols)


    def convert_cols_to_dtype(self, cols, dtype):
        if(self.verbose):
            print(f"- Converting {cols} dtypes to {dtype}.")

        for col in cols:
            self.dataset[col] = pd.Series(self.dataset[col], dtype=dtype)



    def get_df(self, ):
        return self.dataset





