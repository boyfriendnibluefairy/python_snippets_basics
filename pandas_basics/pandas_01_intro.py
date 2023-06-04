## Load the pandas library
## Dont forget to pip install pandas
import pandas as pd
import numpy as np

# Read csv file into pandas dataframe
df_hi = pd.read_csv("free_csv_data_heat_index.csv")
#print(df_hi)

## Check the dimensions of the data set
print(df_hi.shape)

## List columns and their data types
df_hi.info()

## Preview the first few records
num_rows : int = 10
print(df_hi.head(num_rows))

## Sort values in the data frame
df_sorted = df_hi.sort_values("2017", ascending=False)
#print(df_sorted)

## Select specific rows and columns based on position
print(df_hi.iloc[3:6, 2:5])

## Select elements based on list
print(df_hi.iloc[3:6,[1,3,5]])

## Select column based on name and select rows based on conditions
print(df_hi.head())
print(df_hi[df_hi["2016"] > 30.0])

## Select subset of columns based on their names
print(df_hi.head())
print(df_hi[["Date", "2016", "2022"]])

## Drop unnecessary columns
df_reduced = df_hi.drop(columns=["2016"])
#print(df_reduced)

## Rename a column ## columns={ "old_name":"new_name" }
df_renamed = df_hi.rename(columns={"Date":"Day"})
#print(df_renamed.head())

## Determine the data type of column
print(df_hi["Date"].dtype)

## Copy a data frame
df_temp = df_hi.copy()

## Convert columns into appropriate data types
df_temp["Date"] = pd.to_numeric(df_temp["Date"], errors="coerce")

## Check if some elements are null values
print(df_temp.isnull().sum())

## How to replace all null values with zero in any columns
df_replaced = df_temp.fillna(0)
#print(df_replaced[df_replaced["2019"] > 30.0].head())

## Drop records that contains  null values. Be careful
df_cleaned = df_temp.dropna()
#print(df_cleaned.isnull().sum())

## Check for any duplicate records
print(sum(df_temp.duplicated(df_temp.columns)))

## Delete duplicates of records
df_temp = df_temp.drop_duplicates(df_temp.columns, keep="last")
#print(sum(df_temp.duplicated(df_temp.columns)))

## Display descriptive statistics for numeric columns
print(df_temp.describe())

## Filter records based on conditions in one column
df_filtered = df_temp[df_temp['2016'] > 30]
#print(df_temp.shape)
#print(df_filtered.shape)

## Create new field or column
## Count number of columns
df_temp["7_yr_ave"] = df_temp.iloc[:,1:-1].sum()/len(df_temp.columns)

## Randomly select 3 samples with 33 records each
sample01 = df_hi.sample(n=33)
sample02 = df_hi.sample(n=33)
sample03 = df_hi.sample(n=33)

## Append rows
concat_samples = pd.concat(sample01,sample02,sample03)

## Export data frame into csv files using Google Colab
from google.colab import files
df_temp.to_csv("heat_index_data_frame.csv")
files.download("heat_index_data_frame.csv")
























