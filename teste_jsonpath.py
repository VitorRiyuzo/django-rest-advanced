import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#print(resultados)
primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(primeira)