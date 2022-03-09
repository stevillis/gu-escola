import jsonpath
import requests

BASE_URL = 'http://localhost:8000/api/v2/'

# GET Avaliacoes
response = requests.get(f'{BASE_URL}avaliacoes')

# results = jsonpath.jsonpath(response.json(), 'results')
# results = jsonpath.jsonpath(response.json(), 'results[0]')
# results = jsonpath.jsonpath(response.json(), 'results[0].nome')


# Todos os nomes das pessoas que avaliaram o curso
nomes = jsonpath.jsonpath(response.json(), 'results[*].nome')
print(nomes)

# Todas as notas das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(response.json(), 'results[*].avaliacao')
print(notas)
