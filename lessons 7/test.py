import requests

data = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()
print(float(data[1]['buy']))