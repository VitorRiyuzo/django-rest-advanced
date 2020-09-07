import requests
class TesteCursos:
    headers = {'Authorization': 'Token bdd8e7ad71223a468d3d0af97f06efd3b081090e'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url = self.url_base_cursos, headers = self.headers)
        assert cursos.status_code == 200
    def test_get_curso(self):
        curso = requests.get(url = f'{self.url_base_cursos}2', headers = self.headers)
        assert curso.status_code == 200