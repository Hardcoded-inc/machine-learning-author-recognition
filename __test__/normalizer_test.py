from unittest import TestCase
from normalizer import Normalizer
import pandas as pd

class NormalizerTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.normalizer = Normalizer()

    def test_lowercase(self):
        df = pd.DataFrame({"some_col": ["Some Text WITH UPPERCASed letters"]})
        self.normalizer.lowercase(df, col="some_col")

        result_val = "some text with uppercased letters"
        self.assertEqual(df.iloc[0]["some_col"], result_val )

    def test_remove_inbrackets_text(self):
        df = pd.DataFrame({"some_col": ["Some text in {curly braces}, (parentheses), [and brackets]"]})
        self.normalizer.remove_inbrackets_text(df, col="some_col")

        result_val = "Some text in , , "
        self.assertEqual(df.iloc[0]["some_col"], result_val )

    def test_remove_punctuations(self):
        df = pd.DataFrame({"some_col": ["Some - text with: punctuation, I'll put_here an *, what about questions? God! It should #work ^^%NICE%^^"]})
        self.normalizer.remove_punctuations(df, col="some_col")

        result_val = "Some  text with punctuation Ill puthere an  what about questions God It should work NICE"
        self.assertEqual(df.iloc[0]["some_col"], result_val )
