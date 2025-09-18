import requests

url = "https://viacep.com.br/abc/"

r = requests.get(url)
print(r.text)
