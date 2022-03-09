import requests

headers = {
    'Authorization': 'Token 22c4f0770323557ee4d67258c66e9df5d7660fde'
}
BASE_URL = 'http://localhost:8000/api/v2/'

response = requests.delete(url=f'{BASE_URL}cursos/4/', headers=headers)

assert response.status_code == 204
assert len(response.text) == 0
