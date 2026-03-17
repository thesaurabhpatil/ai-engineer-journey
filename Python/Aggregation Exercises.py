import pandas as pd

# Sample sales data
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
    'Sales': [100, 150, 200, 120, 180, 160, 140, 190],
    'Quantity': [5, 3, 8, 4, 6, 7, 5, 9]
}

df = pd.DataFrame(data)

# Exercise 1: Filter sales greater than 150
exercise1 = df[df['Sales'] > 150]
print("Exercise 1 - Sales > 150:")
print(exercise1)

# Exercise 2: Group by Region and sum Sales
exercise2 = df.groupby('Region')['Sales'].sum()
print("\nExercise 2 - Total Sales by Region:")
print(exercise2)

# Exercise 3: Filter North region and calculate average Sales
exercise3 = df[df['Region'] == 'North']['Sales'].mean()
print("\nExercise 3 - Average Sales in North:")
print(exercise3)

# Exercise 4: Group by Region and get max Sales per region
exercise4 = df.groupby('Region')['Sales'].max()
print("\nExercise 4 - Max Sales by Region:")
print(exercise4)

# Exercise 5: Filter Sales > 150, group by Region, count records
exercise5 = df[df['Sales'] > 150].groupby('Region').size()
print("\nExercise 5 - Count of Sales > 150 by Region:")
print(exercise5)