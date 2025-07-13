class Classifier:
    def __init__(self, trainer):
        # <<<<< Getting trainer data >>>>>
        self.statistics = trainer.dict_statistics
        self.feature = trainer.feature
        self.dict_unique_val = trainer.dict_unique_val

    # <<<<< Result answer >>>>>
    def classify(self, user_choices):
        results = self._calculate_probabilities(user_choices)
        return max(results, key=results.get)

    # <<<<< Result answer + statistics >>>>>
    def classify_with_stats(self, user_choices):
        results = self._calculate_probabilities(user_choices)  # dict(possible answer : statistics)
        prediction = max(results, key=results.get)
        return prediction, results

    # <<<<< Calculating statistics for user choices >>>>>
    def _calculate_probabilities(self, user_choices):
        results = {}
        for category in self.statistics:  # category = possible answer.
            probability = 1
            for col in self.feature:
                value = user_choices.get(col)  # dict(key: value) -> value
                if value not in self.dict_unique_val[col]:  # Statistics not found
                    prob = 1 / (len(self.dict_unique_val[col]) + 1)
                else:
                    prob = self.statistics[category][col][value]
                probability *= prob
            results[category] = probability
        return results
