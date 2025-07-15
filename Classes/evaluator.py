import pandas as pd
from Classes.get_data import GetData
from Classes.data_trainer import Trainer
from Classes.classifier import Classifier


class Evaluator:
    def __init__(self, train_ratio=0.7):
        # <<<<< Creating an instance of GetData and loading full DataFrame >>>>>
        self.get_data = GetData()
        self.df = self.get_data.get_df()
        self.train_ratio = train_ratio

    # <<<<< Split DataFrame to train and test sets >>>>>
    def split_data(self):
        shuffled_df = self.df.sample(frac=1, random_state=1).reset_index(drop=True)

        train_size = int(len(shuffled_df) * self.train_ratio)

        train_set = shuffled_df.iloc[:train_size]
        test_set = shuffled_df.iloc[train_size:]

        return train_set, test_set

    # <<<<< Evaluate classifier accuracy >>>>>
    def evaluate(self):
        train_set, test_set = self.split_data()
        trainer = Trainer(train_set)
        classifier = Classifier(trainer)

        correct = 0

        for _, row in test_set.iterrows():
            if self.test_example(classifier, row):
                correct += 1

        accuracy = (correct / len(test_set)) * 100
        print(f"Accuracy: {accuracy:.2f}%")

    # <<<<< Test a single example and return True if prediction is correct >>>>>
    def test_example(self, classifier, row):
        example = row.iloc[:-1].to_dict()
        actual = row.iloc[-1]

        prediction = classifier.classify(example)
        return prediction == actual
