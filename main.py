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

data=pd.read_csv("London.csv")

print(data)

# Check individual values for missing values
print(data.isna())

# Check each column for missing values
print(data.isna().any())

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt


# Bar plot of missing values by variables
data.isna().sum().plot(kind="bar")

# Show plot
plt.show()




















