import requests

headers = {
    'Authorization': 'Token 6e6ab3885e67fcc06fabc926a277b07c3bd86be8'
}
BASE_URL = 'http://localhost:8000/api/v2/'

novo_curso = {
    'titulo': 'Libras para cegos 2',
    'url': 'https://www.google.com/courses/libras-for-blind-people-2'
}

response = requests.post(f'{BASE_URL}cursos/', headers=headers, data=novo_curso)
response_json = response.json()

assert response.status_code == 201
assert response_json.get('titulo') == novo_curso.get('titulo'), response_json.get('url')[0]
