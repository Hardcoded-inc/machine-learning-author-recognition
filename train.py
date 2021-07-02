from sklearn import linear_model, naive_bayes, svm
from trainer import Trainer
from sklearn import ensemble
import xgboost
import warnings


def run():
    trainer = Trainer("checkpoint9.csv", ["seq", "artist"])

    trainer.train(naive_bayes.MultinomialNB(), Trainer.COUNT_VECTORS)

    trainer.train(linear_model.LogisticRegression(), Trainer.COUNT_VECTORS)
    trainer.train(linear_model.LogisticRegression(), Trainer.WORD_VECTORS)
    trainer.train(linear_model.LogisticRegression(), Trainer.NGRAM_VECTORS)
    trainer.train(linear_model.LogisticRegression(), Trainer.CHAR_VECTORS)

    trainer.train(svm.SVC(), Trainer.NGRAM_VECTORS)

    trainer.train(ensemble.RandomForestClassifier(), Trainer.COUNT_VECTORS)
    trainer.train(ensemble.RandomForestClassifier(), Trainer.WORD_VECTORS)

    trainer.train(xgboost.XGBClassifier(), Trainer.COUNT_VECTORS)
    trainer.train(xgboost.XGBClassifier(), Trainer.WORD_VECTORS)
    trainer.train(xgboost.XGBClassifier(), Trainer.CHAR_VECTORS)


if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        run()
