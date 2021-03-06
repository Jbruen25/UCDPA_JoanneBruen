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

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt


London=pd.read_csv("London.csv")

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

# Check individual values for missing values
print(financial.isna())

# Check each column for missing values
print(financial.isna().any())

# Counting the number of missing values
print(financial.isna().sum())

# Import matplotlib.pyplot with alias plt

print(financial.index)

import matplotlib.pyplot as plt

# Bar plot of missing values by variables
financial.isna().sum().plot(kind="bar")

# Show plot
plt.show()

# Fill in the missing values with XXX
financial_filled = financial.fillna(0)



# Sort data by sector
financial_sector = financial.sort_values("Sector")

print(financial_sector.head())

# Sort data by Sector, then descending names
financial_sector_name = financial.sort_values(["Sector", "Name"], ascending=[True, False])

print(financial_sector_name.head())

# Setting the name as the index
name_financial = financial.set_index("Name")

print(name_financial)

# select the Name, Price/Earnings, Dividend Yield, EBITDA

financial_data = financial[["Name", "Price/Earnings", "Dividend Yield", "EBITDA"]]

print(financial_data.head())


# filter for rows where the sector is Financials and the Earnings/share is greater than 10

financial_finance_100 = financial[(financial["Earnings/Share"] > 10) & (financial["Sector"] == "Financials")]

# Plot the financial companies with a earning share greater than 10
financial_finance_100.set_index('Name', inplace=True)
financial_finance_100.plot(y='Earnings/Share', rot=90, kind='bar', title='Financial Earnings/Shares')

plt.show()

print(financial_finance_100)

# select the Name, Price/Earnings, Dividend Yield, EBITDA

financial_data = financial[["Name", "Sector", "Price/Earnings", "Dividend Yield", "EBITDA"]]

# print the maximum and minimum dividend yield for financial_data

print(financial_data["Dividend Yield"].max())

print(financial_data["Dividend Yield"].min())




# import numpy as np and create custom IQR function

def iqr(column):
    return column.quantile(0.75) - column.quantile(.25)

# Update to print IQR and median, min, max and mean of Price/Earnings, Dividend Yield, EBITDA
print(financial_data[["Price/Earnings", "Dividend Yield", "EBITDA"]].agg([iqr, np.median, np.min, np.max, np.mean]))





import matplotlib.pyplot as plt

data = pd.read_csv("financials.csv", index_col=2)

# Plot the dividend yield for each of the sectors

financial_data.plot(x='Sector', y='Dividend Yield', rot=90, kind='scatter', title='Dividend Yield')

plt.show()

# Plot the dividend yield for each of the sectors

financial_data.plot(x='Sector', y='EBITDA', rot=90, kind='scatter', title='EBITDA')

plt.show()

Supermarket=pd.read_csv("supermarket_sales - Sheet1.csv")

print(Supermarket)

#  looping data

x = Supermarket[["Branch", "City"]]


for x in ["Branch"] :

    print(x)


# iterrows data
itr = next(Supermarket.iterrows())[1]

print(itr)

Loan_payments=pd.read_csv("Loan payments data.csv")

print(Loan_payments)

# Create a dictorary

trns = {'loan_status' : 'PAIDOFF', 'Principal' : '300'}

print(trns['Principal'])

# Create a list

trnss = ['loan_status', 'Principal']

print(trnss)

Perth=pd.read_csv("Perth.csv")

print(Perth.head())

print(Perth.shape)

Melbourne=pd.read_csv("Melbourne_housing_FULL.csv")

print(Melbourne.head())

print(Melbourne.shape)

# inner join on suburb
suburb_city = Melbourne.merge(Perth, on='Suburb')
print(suburb_city.head(4))

print(suburb_city.shape)






















































