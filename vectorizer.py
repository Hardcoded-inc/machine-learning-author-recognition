from sklearn.feature_extraction.text import CountVectorizer

class Vectorizer:

    def __init__(self, col1="seq"):
        self.col1 = col1

    def vectorize(self, df, train_x, valid_x):

        count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
        count_vect.fit(df[self.col1])

        xtrain_count = count_vect.transform(train_x)
        xvalid_count = count_vect.transform(valid_x)

        return xtrain_count, xvalid_count