# import requests for USD and EUR
import requests
request=requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=EEOAN1214S09QCDE')
print(request.status_code)
print(request.text)







