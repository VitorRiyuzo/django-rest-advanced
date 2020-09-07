import requests
headers = {'Authorization':'Token bdd8e7ad71223a468d3d0af97f06efd3b081090e'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
resultado = requests.get(url=url_base_cursos, headers= headers)

assert resultado.status_code == 200