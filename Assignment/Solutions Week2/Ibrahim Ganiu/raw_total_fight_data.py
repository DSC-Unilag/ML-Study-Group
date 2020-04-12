import pandas as pd

df = pd.read_csv("raw_total_fight_data.csv",sep=";", parse_dates=["date"])



print(df.head(5)) # Q1
print(df.tail(5)) # Q1
print(pd.set_option("display.max_rows", len(df))) # Q2
print(df.shape) # Q3
index_4 = df.iloc[3] # Q4
print(df.describe()) # Q5

df.to_csv("processed_raw_total_fight_data_week2.csv")
