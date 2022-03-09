import requests

BASE_URL = 'http://localhost:8000/api/v2/'

# GET Avaliacoes
"""
response = requests.get(f'{BASE_URL}avaliacoes')

print(response)
print(response.status_code)

avaliacoes = response.json()

print(avaliacoes)
print(avaliacoes.get('count'))
print(avaliacoes.get('results'))
"""

# GET Cursos
headers = {
    'Authorization': 'Token 6e6ab3885e67fcc06fabc926a277b07c3bd86be8'
}
response = requests.get(f'{BASE_URL}cursos', headers=headers)
print(response.json().get('results'))
