import requests

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)

resposta.status_code


dados = resposta.json()

dados

## Posições dos herois 

dados[0]['localized_name']


## Todos os nomes

for i in dados:
    print(i['localized_name'])


## Pandas

import pandas as pd

df = pd.DataFrame(dados)

df.to_csv("heroes_dota.csv", sep=";")


### --------------------- ###

## Api de partidas 

url = "https://api.opendota.com/api/proMatches"

data = requests.get(url).json()

df_partida = pd.DataFrame(data)
df_partida.to_csv("partidas_dota.csv", sep=";")

df_partida
