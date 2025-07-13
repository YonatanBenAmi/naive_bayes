import pandas as pd
from Classes.get_data import GetData
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    t = Trainer()
    return t.df


class Trainer:
    # <<<<< Creating an instance >>>>>.
    get_data = GetData()
    # <<<<< Variables for DataFrame >>>>>
    df = get_data.get_df() # Full DataFrame.
    subset = get_data.get_last_colomn() # Last column.
    feature = get_data.get_other_columns() # The other columns.
    dict_unique_val = get_data.get_dict_unique_val() # A dictionary that holds all the unique values ​​for each column.
    # <<<<< Variables for sub DataFrame >>>>>
    sub_df = df.groupby(df.columns[-1]) # Group DataFrame by last column.
    dict_statistics = {} # Dictionary with statistics for each column.


    # <<<<< Filling dictionaries >>>>>

    for key, sub_group in sub_df:  # Enter values for dict_statistics(Variable).
        if key not in dict_statistics:
            dict_statistics[key] = {}

        for col in feature:
            if col not in dict_statistics[key]:
                dict_statistics[key][col] = {}

            for val in dict_unique_val[col]:  
                count = (sub_group[col] == val).sum() 
                # Addition in the numerator and denominator to prevent statistics from resetting.
                probability = (count + 1) / (len(sub_group) + len(dict_unique_val[col]))
                dict_statistics[key][col][val] = probability

    # print(dict_statistics)
    print(dict_unique_val)

        