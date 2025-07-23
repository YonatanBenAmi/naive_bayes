import pandas as pd

class GetData:

    csv_file = "data/data.csv"  # class attribute
    df = pd.read_csv(csv_file)
    feature = df.columns[:-1]
    dict_unique_val = {} # A dictionary that holds all the unique values ​​for each column.

    for col in feature: # Enter values for dict_unique_val(Variable).
        dict_unique_val[col] = []
        for unique_val in df[col].unique():
            dict_unique_val[col].append(unique_val)

    def get_df(self):
        return pd.read_csv(self.csv_file) 

    def get_last_colomn(self):
        df = self.get_df()
        return df[df.columns[-1]]

    def get_other_columns(self):
        df = self.get_df()
        return df.columns[:-1]
    
    def get_dict_unique_val(self):
        return self.dict_unique_val
