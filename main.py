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

# import numpy as np
import numpy as np


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


financial =pd.read_csv("financials.csv", index_col=3)

print(financial)

# summary statistics
print(financial.head())

print(financial.shape)

print(financial.describe())

print(financial.info())

print(financial.values)

print(financial.columns)

print(financial.index)

# Sort data by sector
financial_sector = financial.sort_values("Sector")

print(financial_sector.head())

# Sort data by Sector, then descending names
financial_sector_name = financial.sort_values(["Sector", "Name"], ascending=[True, False])

print(financial_sector_name.head())

# select the Name, Price/Earnings, Dividend Yield, EBITDA

financial_data = financial[["Name", "Price/Earnings", "Dividend Yield", "EBITDA"]]

print(financial_data.head())

# filter for rows where the sector is Financials and the Earnings/share is greater than 10

financial_Health_100 = financial[(financial["Earnings/Share"] > 10) & (financial["Sector"] == "Financials")]

print(financial_Health_100)

# select the Name, Price/Earnings, Dividend Yield, EBITDA

financial_data = financial[["Name", "Price/Earnings", "Dividend Yield", "EBITDA"]]

# print the maximum and minimum dividend yield for financial_data

print(financial_data["Dividend Yield"].max())

print(financial_data["Dividend Yield"].min())

# import numpy as np and create custom IQR function

def iqr(column):
    return column.quantile(0.75) - column.quantile(.25)

# Update to print IQR and median of Price/Earnings, Dividend Yield, EBITDA
print(financial_data[["Price/Earnings", "Dividend Yield", "EBITDA"]].agg([iqr, np.median, np.min, np.max, np.mean]))

# Find if there are missing values
print(financial.isnull().sum())

# Fill in the missing values with XXX
financial_filled = financial.fillna(0)

import matplotlib.pyplot as plt

data = pd.read_csv("financials.csv", index_col=2)

# create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

ax.bar(data.index, data["52 Week High"], label="52 Week High")
ax.set_xticklabels(data.index, rotation=90)
ax.set_ylabel('Price')
ax.legend()

plt.show()

fig, ax = plt.subplots()


ax.bar(data.index, data["52 Week Low"], label="52 Week Low")
ax.set_xticklabels(data.index, rotation=90)

ax.set_ylabel('Price')
ax.legend()

plt.show()

Supermarket=pd.read_csv("supermarket_sales - Sheet1.csv")

print(Supermarket)

# loops through income

for income in data['Branch']:print(income['income'])















































