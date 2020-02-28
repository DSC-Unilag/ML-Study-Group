import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cleaning of data
df = pd.read_csv('data.csv')
df.fillna(method='ffill') # Filling empty cells
df.fillna(method='bfill')


# Visualization of data using scatter plot,boxplot and histogram

# Scatter plot
plt.scatter(df['R_wins'], df['R_Reach_cms'], label='Red', marker='D')
plt.scatter(df['B_wins'], df['B_Reach_cms'], label='Blue', marker='.')
plt.xlabel("Age")
plt.ylabel("Fighter's Reach")
plt.grid()
plt.title("Fighter's Reach against Fighter Age")



# Boxplot
# plt.boxplot([ df['R_wins'] , df['B_wins'] ], labels=['Red wins', 'Blue wins'])


# Histogram
# plt.hist([df['R_wins'], df['B_wins']], label=['Red wins', 'Blue wins'], bins=10)

plt.legend()
plt.show()
