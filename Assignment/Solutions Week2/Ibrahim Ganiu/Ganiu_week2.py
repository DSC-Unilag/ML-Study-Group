import pandas as pd

def feetInches_to_centimeters(n):
	feet = 0
	value = ''
	for i in n:
		if i=="'":
			feet = value
			value = ''
		else:
			value += i

	result = eval(feet) * 30.48
	result += eval(value) * 2.54
	return result

def inches_to_centimeters(n):
	n = n.replace('"', '')
	return eval(n)*2.54



df = pd.read_csv("raw_fighter_details.csv", parse_dates=["DOB"])
df.fillna(method="ffill", inplace=True)
df.fillna(method="bfill", inplace=True)

df.replace({
	'Weight': '[A-Za-z.]',
	'Reach': '["]',
	'Height': '["]',
	}, '', regex=True, inplace=True)

for i in range(len(df.Reach)):
	df.Reach[i] = inches_to_centimeters(df.Reach[i])
	df.Height[i] = feetInches_to_centimeters(df.Height[i])


print(df.head(5)) # Q1
print(df.tail(5)) # Q1
print(pd.set_option("display.max_rows", len(df))) # Q2
print(df.shape) # Q3
index_4 = df.iloc[3] # Q4
print(df.describe()) # Q5

df.to_csv("processed_raw_fighter_details_week2.csv")
