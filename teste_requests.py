import requests

#GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
#Acessando o código de status HTTP
#print(avaliacoes.status_code)

#Acessando os dados da resposta
print(avaliacoes.json())

#Acessando a quantidade de registros
print(avaliacoes.json()['next'])