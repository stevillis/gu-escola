import requests

headers = {
    'Authorization': 'Token 6e6ab3885e67fcc06fabc926a277b07c3bd86be8'
}
BASE_URL = 'http://localhost:8000/api/v2/'

response = requests.get(f'{BASE_URL}cursoss', headers=headers)
assert response.status_code == 200, f'{response.status_code} - Não foi possível obter Cursos.'
