import pandas as pd

data = {
    "EmployeeID": ["E01", "E02", "E03", "E04"],
    "JoinYear": [2018, 2020, 2016, 2022],
    "Salary": [60000, 50000, 80000, 45000],
    "PerformanceScore": [3, 4, 5, 2]
}

df = pd.DataFrame(data)
#print(df)

current_year = 2026
df["Tenure"] = current_year - df["JoinYear"]
#print(df)

#print(df.info())
#print(df.describe())

df.loc[2, "Salary"] = None
#print(df.isnull().sum())

df["Salary"].fillna(df["Salary"].median())


df["SalaryPerYear"] = df["Salary"] / df["Tenure"]
df.to_csv("c:/Users/saurabh.patil/Desktop/AI/processed_hr_data.csv", index=False)

