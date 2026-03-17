import pandas as pd
import numpy as np
import os

# 1. Load CSV and Excel files if they exist, else create sample DataFrames
if os.path.exists('sample.csv'):
    df_csv = pd.read_csv('sample.csv')      # Replace with your CSV file path
else:
    data_csv = {
        'column1': np.random.randint(1, 100, 10),
        'column2': np.random.randint(1, 100, 10),
        'column3': np.random.randint(1, 100, 10),
        'column4': np.random.randint(1, 100, 10),
        'group_col': np.random.choice(['A', 'B'], 10),
        'column5': np.random.randint(1, 100, 10)
    }
    df_csv = pd.DataFrame(data_csv)

if os.path.exists('sample.xlsx'):
    df_excel = pd.read_excel('sample.xlsx') # Replace with your Excel file path
else:
    data_excel = {
        'A': np.random.randn(10),
        'B': np.random.randn(10),
        'C': np.random.randint(1, 50, 10)
    }
    df_excel = pd.DataFrame(data_excel)

# 2. Explore data
print("CSV DataFrame Head:\n", df_csv.head())
print("Excel DataFrame Info:\n")
df_excel.info()
print("CSV DataFrame Description:\n", df_csv.describe())

# 3. DataFrame Exercises

# Exercise 1: Select a column and calculate mean
if 'column1' in df_csv.columns:
    print("Mean of column1:", df_csv['column1'].mean())

# Exercise 2: Filter rows where a column value > threshold
filtered = df_csv[df_csv['column2'] > 50]  # Replace 'column2' and 50 as needed
print("Filtered rows:\n", filtered.head())

# Exercise 3: Add a new column based on existing columns
if {'column3', 'column4'}.issubset(df_csv.columns):
    df_csv['sum_col'] = df_csv['column3'] + df_csv['column4']
    print("Added sum_col:\n", df_csv[['column3', 'column4', 'sum_col']].head())

# Exercise 4: Group by a column and get mean
if 'group_col' in df_csv.columns:
    group_mean = df_csv.groupby('group_col').mean(numeric_only=True)
    print("Group by mean:\n", group_mean)

# Exercise 5: Sort DataFrame by a column
if 'column5' in df_csv.columns:
    sorted_df = df_csv.sort_values(by='column5', ascending=False)
    print("Sorted DataFrame:\n", sorted_df.head())