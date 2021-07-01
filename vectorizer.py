from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


class Vectorizer:

    def __init__(self, df, train_x, valid_x, train_col):
        self.df = df
        self.train_x = train_x
        self.valid_x = valid_x
        self.train_col = train_col

    def create_count_vectors(self):
        count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
        count_vect.fit(self.df[self.train_col])

        train = count_vect.transform(self.train_x)
        valid = count_vect.transform(self.valid_x)

        return train, valid

    def create_word_level_tf_idf(self):
        tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)
        tfidf_vect.fit(self.df[self.train_col])

        train = tfidf_vect.transform(self.train_x)
        valid = tfidf_vect.transform(self.valid_x)

        return train, valid

    def create_ngram_level_tf_idf(self):
        tfidf_vect_ngram = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2, 3),
                                           max_features=5000)
        tfidf_vect_ngram.fit(self.df[self.train_col])

        train = tfidf_vect_ngram.transform(self.train_x)
        valid = tfidf_vect_ngram.transform(self.valid_x)

        return train, valid

    def create_character_level_tf_idf(self):
        tfidf_vect_ngram_chars = TfidfVectorizer(analyzer='char', ngram_range=(2, 3),
                                                 max_features=5000)
        tfidf_vect_ngram_chars.fit(self.df[self.train_col])

        train = tfidf_vect_ngram_chars.transform(self.train_x)
        valid = tfidf_vect_ngram_chars.transform(self.valid_x)

        return train, valid
