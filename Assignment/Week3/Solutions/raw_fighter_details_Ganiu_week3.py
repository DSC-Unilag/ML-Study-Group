import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def feetInches_to_centimeters(n):
	""" Converts feet-inches to centimeters e.g 5'4" """
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
	""" Converts inches to centimeters e.g 4" """
	n = n.replace('"', '')
	return eval(n)*2.54

def extractYearOfBirthFromDOB(date):
	""" Computes the age using full date passed [date] """
	return datetime.datetime.now().year-date.year

# Loading and Cleaning of data
df = pd.read_csv("raw_fighter_details.csv", parse_dates=["DOB"])
df.fillna(method="ffill", inplace=True)
df.fillna(method="bfill", inplace=True)

df.replace({
	'Weight': '[A-Za-z.]',
	'Reach': '["]',
	'Height': '["]',
	}, '', regex=True, inplace=True)

# Converting Height in feet-inches to centimeter and Reach in inches to centimeters
df['Height'] = df['Height'].apply(feetInches_to_centimeters)
df['Reach'] = df['Reach'].apply(inches_to_centimeters)
df['Age'] = df['DOB'].apply(extractYearOfBirthFromDOB)


# Visualization of data using scatter plot,boxplot and histogram

# Boxplot
plt.boxplot(df['Height'], labels=["Fighter's Height"])



# Scatter plot
# plt.scatter(df['Reach'], df['Weight'], marker='.', color='g')
# plt.xlabel("Fighter's Height")
# plt.ylabel("Fighter's Reach")
# plt.grid()
# plt.title("Fighter's Reach against Fighter Weight")


# Pie chart and Bar chart
# stances = list( set(df.Stance) )
# stances_frequency = []
# for i in stances:
# 	stances_frequency.append(len(df.Stance[df.Stance==i]))

# Pie chart
# plt.pie(stances_frequency, labels=stances, startangle=90)
# plt.title('Ratio of Stance of fighters')
# plt.show()

# Bar chart
# x = range(len(stances))
# plt.yticks(x, stances)
# plt.title('Fighters Stance frequency')
# plt.xlabel('Stances')
# plt.ylabel('Frequency')
# plt.bar(x,height=stances_frequency, color='g')

plt.legend()
plt.show()
