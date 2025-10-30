import pandas as pd
class Initiation:
    def __init__(self):
        pass
    def import_my_data(self):
        print("Please enter your data path")
        path=input()
        data=pd.read_csv(path)
        return data
# Exploring the Dataset
print(data.head())
# To check the data types
print(data.info())
# Convering into lowercase and replacing spaces with '_'
data.columns=[col.lower().replace(" ","_") for col in data.columns]
# To check the missing values
print(data.isnull().sum())
# Converting to datetime
data['date']=pd.to_datetime(data['date'])
print(data.info())
# Show all column names for verification after renaming and cleaning.
print(data.columns)
# Display summary statistics (count, mean, min, max, quartiles) for all numerical columns.
print(data.describe())
# See the 10 smallest transactions for outlier or unusual value detection.
print(data.sort_values('amount').head(10))
# See the 10 largest transactions to spot possible outliers or errors.
print(data.sort_values('amount',ascending=False).head(10))
# Find and display all records where the amount is negative (potential data issues).
print(data[data["amount"] < 0])
# List all unique transaction types to check for typos or inconsistent formatting.
print(data["type"].unique())
# List all unique expense categories to check for spelling variations and standardization needs.
print(data["category"].unique())

