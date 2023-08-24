import requests
import json

cotacoes = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
)
cotacoes = cotacoes.json()
cotacoes_Euro = cotacoes["EURBRL"]["low"]
# print(cotacoes)
print(cotacoes_Euro)
