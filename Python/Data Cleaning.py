import pandas as pd
import numpy as np

# Sample data for exercises
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eve', 'Alice'],
    'Age': [25, np.nan, 30, 22, 29, 25],
    'City': ['NY', 'LA', 'NY', np.nan, 'LA', 'NY'],
    'Score': [85, 90, np.nan, 88, 92, 85]
}
df = pd.DataFrame(data)

# 1. Handling missing values: Fill missing 'Age' with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 2. Handling missing values: Drop rows where 'Name' is missing
df = df.dropna(subset=['Name'])

# 3. Handling missing values: Fill missing 'City' with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])

# 4. Handling missing values: Fill missing 'Score' with median
df['Score'] = df['Score'].fillna(df['Score'].median())

# 5. Handling duplicates: Remove duplicate rows based on 'Name' and 'Age'
df = df.drop_duplicates(subset=['Name', 'Age'])

print(df)