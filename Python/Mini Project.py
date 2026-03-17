import pandas as pd
import numpy as np
from datetime import datetime

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eve'],
    'Age': [25, 30, 28, None, 35],
    'Salary': [50000, 60000, 55000, 62000, 58000],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR'],
    'Join_Date': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-11-05', '2020-07-22']
}

df = pd.DataFrame(data)

# Data Cleaning
print("=== Original Data ===")
print(df)
print("\n")

# Check for missing values
print("=== Missing Values ===")
print(df.isnull().sum())
print("\n")

# Handle missing values
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Data Analysis
print("=== Cleaned Data ===")
print(df)
print("\n")

print("=== Data Summary ===")
print(f"Average Age: {df['Age'].mean():.2f}")
print(f"Average Salary: ${df['Salary'].mean():,.2f}")
print(f"\nDepartment Distribution:")
print(df['Department'].value_counts())
print("\n")

# Convert Join_Date to datetime
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

print("=== Data Info ===")
print(df.info())