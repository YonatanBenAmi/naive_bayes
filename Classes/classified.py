class Classifier:
    def __init__(self, trainer):
        self.statistics = trainer.dict_statistics
        self.feature = trainer.feature
        self.dict_unique_val = trainer.dict_unique_val

    def classify(self, example):
        """
        סיווג רגיל — מחזיר רק את הקטגוריה המנצחת
        """
        results = self._calculate_probabilities(example)
        return max(results, key=results.get)

    def classify_with_details(self, example):
        results = self._calculate_probabilities(example)
        total = sum(results.values())
        percentages = {category: (prob / total) * 100 for category, prob in results.items()}
        prediction = max(results, key=results.get)
        return prediction, results, percentages



    def _calculate_probabilities(self, example):
        """
        פונקציה פנימית שמחשבת את ההסתברויות לפי הדוגמה שניתנה
        """
        results = {}

        for category in self.statistics:
            probability = 1

            for col in self.feature:
                value = example.get(col)

                if value not in self.dict_unique_val[col]:
                    prob = 1 / (len(self.dict_unique_val[col]) + 1)
                else:
                    prob = self.statistics[category][col][value]

                probability *= prob

            results[category] = probability

        return results

