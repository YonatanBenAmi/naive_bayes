import pandas as pd
from Classes.get_data import GetData


class Trainer:
    def __init__(self, df=None):
        # <<<<< Creating an instance >>>>>.
        get_data = GetData()
        if df is None:
            self.df = get_data.get_df()  # Full DataFrame.
        else:
            self.df = df

        # <<<<< Variables for DataFrame >>>>>
        self.feature = get_data.get_other_columns()  # The other columns.
        self.dict_unique_val = get_data.get_dict_unique_val()  # A dictionary that holds all the unique values ​​for each column.

        # <<<<< Variables for sub DataFrame >>>>>
        self.sub_df = self.df.groupby(self.df.columns[-1])  # Group DataFrame by last column.
        self.dict_statistics = {}  # Dictionary with statistics for each column.

        # <<<<< Filling dictionaries >>>>>
        for key, sub_group in self.sub_df:  # Enter statistics for dict_statistics(Variable).
            self.dict_statistics[key] = {}

            for col in self.feature:
                self.dict_statistics[key][col] = {}

                for val in self.dict_unique_val[col]:
                    count = (sub_group[col] == val).sum()
                    # Addition in the numerator and denominator to prevent statistics from resetting.
                    probability = (count + 1) / (len(sub_group) + len(self.dict_unique_val[col]))
                    self.dict_statistics[key][col][val] = probability
