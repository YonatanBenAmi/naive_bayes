import pandas as pd

# <<<<< Variables for DataFrame >>>>>
df = pd.read_csv("data.csv") # Full DataFrame.
subset = df[df.columns[-1]] # Last column.
feature = df.columns[:-1] # The other columns.
dict_unique_val = {} # A dictionary that holds all the unique values ​​for each column.
# <<<<< Variables for sub DataFrame >>>>>
sub_df = df.groupby(df.columns[-1]) # Group DataFrame by last column.
dict_statistics = {} # Dictionary with statistics for each column.


# <<<<< Filling dictionaries >>>>>

for col in feature: # Enter values for dict_unique_val(Variable).
    dict_unique_val[col] = []
    for unique in df[col].unique():
        dict_unique_val[col].append(unique)

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






# print("1-------", dict_unique_val)
# print("2-------", dict_statistics)
# print("3-------", subset.unique())

