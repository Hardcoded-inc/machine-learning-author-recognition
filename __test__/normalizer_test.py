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

    def test_remove_phrases_with_numbers(self):
        df = pd.DataFrame({"some_col": ["123456789 some text with numbers I_should_be_deleted_2 987654321"]})
        self.normalizer.remove_phrases_with_numbers(df, col="some_col")

        result_val = " some text with numbers  "
        self.assertEqual(df.iloc[0]["some_col"], result_val)

    def test_drop_empty_records(self):
        df = pd.DataFrame({"some_col": ["abc", '', '']})
        df = self.normalizer.drop_empty_records(df, col="some_col")

        self.assertEqual(len(df.some_col), 1)

    def test_drop_written_by(self):
        df = pd.DataFrame({"some_col": ["written by some author", 'something is being written', 'made by me']})
        df = self.normalizer.drop_written_by(df, col="some_col")

        self.assertEqual(len(df.some_col), 2)

    def test_remove_stop_words(self):
        df = pd.DataFrame({"some_col": ['All of the stopwords should do a magic trick and disappear.']})
        self.normalizer.remove_stop_words(df, col="some_col")

        result_val = 'All stopwords magic trick disappear.'

        self.assertEqual(df.iloc[0]["some_col"], result_val)
