import requests
headers = {'Authorization':'Token bdd8e7ad71223a468d3d0af97f06efd3b081090e'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

novo_curso = {
    "titulo":"Gerencia",
    "url":"http://olamundo.com.br"
}
resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == 201
assert resultado.json()['titulo'] == novo_curso['titulo']