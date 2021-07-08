# import requests for USD and EUR
import matplotlib
import requests
from matplotlib import pyplot as plt

request=requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=EEOAN1214S09QCDE')
print(request.status_code)
print(request.text)
# import requests for Russia
request=requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=f3610f12f1cea961a8ac655c769df8a8')
print(request.status_code)
print(request.text)

# import Pandas as pd

import pandas as pd

London=pd.read_csv("London.csv")

# Print the 1st 5 rows of the information
print(London.head())

# number of columns and rows
print(London.shape)

# Check individual values for missing values
print(London.isna())

# Check each column for missing values
print(London.isna().any())

# Counting the number of missing values
print(London.isna().sum())

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Bar plot of missing values by variables
London.isna().sum().plot(kind="bar")

# Show plot
plt.show()

#

# Fill in the missing values with XXX
London_filled = London.fillna(0)


# print the columns
print(London.columns)

# print the index
print(London.index)

# setting a column as index
London_ind = London.set_index("House Type")
print(London_ind)


data=pd.read_csv("financials.csv")

print(data)


data=pd.read_csv("Loan payments data.csv")

print(data)

# Print the 1st 5 rows of the information
print(data.head())

# number of columns and rows
print(data.shape)

# import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

data = pd.read_csv("Loan payments data.csv", index_col=3)

# create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

ax.bar(data.index, data["loan_status"])
ax.set_xlabel('terms')
ax.set_ylabel('loan_status')

plt.show()
































