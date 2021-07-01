from loader import Loader
from sklearn import model_selection, preprocessing, metrics
from vectorizer import Vectorizer


class Trainer:
    COUNT_VECTORS = 'Count Vectors'

    WORD_VECTORS = 'WordLevel TF-IDF'

    NGRAM_VECTORS = 'N-Gram Vectors'

    CHAR_VECTORS = 'CharLevel Vectors'

    def __init__(self, dataset_path, cols):
        self.learn_cols = cols
        self.df = self.load_data_frame(dataset_path, cols)
        self.train_x, self.valid_x, self.train_y, self.valid_y = self.split_into_train_valid()
        self.create_encoded_labels()

        self.vectorizer = Vectorizer(self.df, self.train_x, self.valid_x, cols[0])

    def split_into_train_valid(self):
        return model_selection.train_test_split(self.df[self.learn_cols[0]], self.df[self.learn_cols[1]])

    def create_encoded_labels(self):
        encoder = preprocessing.LabelEncoder()
        self.train_y = encoder.fit_transform(self.train_y)
        self.valid_y = encoder.fit_transform(self.valid_y)

    def train(self, classifier, train_on):
        if train_on == self.COUNT_VECTORS:
            train_x_vect, valid_x_vect = self.vectorizer.create_count_vectors()
        elif train_on == self.WORD_VECTORS:
            train_x_vect, valid_x_vect = self.vectorizer.create_word_level_tf_idf()
        elif train_on == self.CHAR_VECTORS:
            train_x_vect, valid_x_vect = self.vectorizer.create_character_level_tf_idf()
        elif train_on == self.NGRAM_VECTORS:
            train_x_vect, valid_x_vect = self.vectorizer.create_ngram_level_tf_idf()
        else:
            raise TypeError

        accuracy = self.train_model(classifier, train_x_vect, self.train_y, valid_x_vect)
        print(f"classifier {type(classifier).__name__}, {train_on}: {accuracy}")

    def train_model(self, classifier, feature_vector_train, label, feature_vector_valid, is_neural_net=False):
        # fit the training dataset on the classifier
        classifier.fit(feature_vector_train, label)

        # predict the labels on validation dataset
        predictions = classifier.predict(feature_vector_valid)

        if is_neural_net:
            predictions = predictions.argmax(axis=-1)

        return metrics.accuracy_score(predictions, self.valid_y)

    @staticmethod
    def load_data_frame(dataset_path, cols):
        loader = Loader()
        loader.read_csv(dataset_path, cols=cols)
        loader.convert_cols_to_dtype(cols, "string")
        return loader.get_df()
