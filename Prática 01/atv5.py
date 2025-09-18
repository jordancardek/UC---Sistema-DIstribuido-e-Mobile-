import requests

r = requests.get('http://www.google.com/search',params={'q': 'elson de abreu'})

if r.status_code == 200:
    with open("resultado.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("Requisição bem-sucedida")
else:
    print("Não houve sucesso na requisição.")
