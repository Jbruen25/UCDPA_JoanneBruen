# import requests for USD and EUR
import requests
request=requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=EEOAN1214S09QCDE')
print(request.status_code)
print(request.text)

request=requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=f3610f12f1cea961a8ac655c769df8a8')
print(request.status_code)
print(request.text)








