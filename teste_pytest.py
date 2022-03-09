import requests


class TestCursos:
    headers = {
        'Authorization': 'Token 22c4f0770323557ee4d67258c66e9df5d7660fde'
    }

    BASE_URL = 'http://localhost:8000/api/v2/'

    def test_get_cursos(self):
        response = requests.get(f'{self.BASE_URL}cursos', headers=self.headers)
        assert response.status_code == 200, f'{response.status_code} - Não foi possível obter Cursos.'

    def test_get_curso(self):
        response = requests.get(f'{self.BASE_URL}cursos/2', headers=self.headers)
        assert response.status_code == 200, f'{response.status_code} - Não foi possível obter Cursos.'

    def test_post_curso(self):
        novo_curso = {
            'titulo': 'Libras índios',
            'url': 'https://www.google.com/courses/libras-para-indios'
        }
        response = requests.post(f'{self.BASE_URL}cursos/', headers=self.headers, data=novo_curso)
        response_json = response.json()

        assert response.status_code == 201
        assert response_json.get('titulo') == novo_curso.get('titulo'), response_json.get('url')[0]

    def test_put_curso(self):
        curso_atualizado = {
            'titulo': 'Libras para Refugiados',
            'url': 'https://www.google.com/courses/libras-para-refugiados-novo'
        }
        response = requests.put(url=f'{self.BASE_URL}cursos/2/', headers=self.headers, data=curso_atualizado)

        assert response.status_code == 200

    def test_put_titulo_curso(self):
        curso_atualizado = {
            'titulo': 'Libras para Refugiados',
            'url': 'https://www.google.com/courses/libras-para-refugiados'
        }
        response = requests.put(url=f'{self.BASE_URL}cursos/2/', headers=self.headers, data=curso_atualizado)
        response_json = response.json()

        assert response_json.get('titulo') == curso_atualizado.get('titulo'), response_json.get('url')[0]

    def test_delete_curso(self):
        response = requests.delete(url=f'{self.BASE_URL}cursos/5/', headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0
