import requests

headers = {
    'Authorization': 'Token 22c4f0770323557ee4d67258c66e9df5d7660fde'
}
BASE_URL = 'http://localhost:8000/api/v2/'

atualizacao = {
    'titulo': 'Libras para Refugiados',
    'url': 'https://www.google.com/courses/libras-para-refugiados'
}
curso_id = 2

response = requests.put(url=f'{BASE_URL}cursos/2/', headers=headers, data=atualizacao)
response_json = response.json()

print(response.status_code)
print(response.content)

assert response.status_code == 200
assert response_json.get('titulo') == atualizacao.get('titulo'), response_json.get('url')[0]
