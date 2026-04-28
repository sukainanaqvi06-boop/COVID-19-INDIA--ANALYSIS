import pandas as pd

df = pd.read_csv("covidindia.csv")

# find missing values
print("Missing Values")
print(df.isnull().sum())
# find duplicate
print("\nDuplicates values")
print(df.duplicated().sum())
# to check data type
print("\nData Type")
print(df.dtypes)

# 1. Change datatype 
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# 2. fill missing values
df.fillna(0, inplace= True)

# 3. Convert data type float to int
col_to_convert = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'new_tests', 'total_tests','positive_rate', 'total_vaccinations', 'people_vaccinated(1st Dose Only)', 'people_fully_vaccinated', 'new_vaccinations']
df[col_to_convert] = df[col_to_convert].astype(int)
print("Missing Values:")
print(df.isnull().sum())
print("\nData Type:")
print(df.dtypes)
print("\ncleaned Data")
print(df.head())

# 4. total cases
total_cases = df['new_cases'].sum()
print("Total Cases")
print(total_cases)

# 5. total deaths
total_deaths = df["new_deaths"].sum()
print("\nNumber of deaths")
print(total_deaths)

# 6 Which month has the highest cases
df['Month'] = df['date'].dt.month
monthly_case = df.groupby("Month")["new_cases"].sum().sort_values(ascending=False)
print("\nMonth wise cases")
print(monthly_case)

# 7. which month has the highest death rate
df['Month'] = df['date'].dt.month
monthly_death_rate = df.groupby("Month")["new_deaths"].sum().sort_values(ascending=False)
print("\n Month wise death rate")
print(monthly_death_rate)

# 8. which day has the highest casees
peak_day = df.groupby('date')["new_cases"].sum().sort_values(ascending=False)
print("\n Number of cases in a day ")
print(peak_day)

# 10. which day has the highest death rate
per_day_deaths = df.groupby('date')["new_deaths"].sum().sort_values(ascending=False)
print("\n Day wise death")
print(per_day_deaths)

df.to_csv("clean_covid.csv", index=False, encoding="utf-8-sig")
print("clean csv")

import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:mysql1332@localhost/covid_project')

df.to_sql('covid_data', engine ,if_exists="replace", index=False)
print("514 rows mysql")