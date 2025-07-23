import requests

class Classifier:
    
    def __init__(self):
        # <<<<< Getting trainer data >>>>>
        respons = requests.get('http://127.0.0.1:8000/get_trainer')
        self.statistics = respons.json()
        self.feature = requests.get('http://127.0.0.1:8000/other_column').json()
        self.dict_unique_val = requests.get('http://127.0.0.1:8000/uniqe_val').json()

    # <<<<< Result answer >>>>>
    def classify(self, user_choices):
        results = self.calculate_probabilities(user_choices)
        return max(results, key=results.get)

    # <<<<< Result answer + statistics >>>>>
    def classify_with_stats(self, user_choices):
        results = self.calculate_probabilities(user_choices)  # dict(possible answer : statistics)
        prediction = max(results, key=results.get)
        return {
            "prediction": prediction, "results": results
        }

    # <<<<< Calculating statistics for user choices >>>>>
    def calculate_probabilities(self, user_choices):
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
