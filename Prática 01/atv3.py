import requests

url = "https://viacep.com.br/ws/"
uf = "MG"
cidade = "Ibirite"
logradouro = "Avenida Marechal Hermes"

formato = "/json/"

consulta_url = f"{url}{uf}/{cidade}/{logradouro}{formato}"

r = requests.get(consulta_url)

if r.status_code == 200:
    resultados = r.json()
    print(f'*********************************************************')
    print(f"\nListandos os {len(resultados)} resultados encontrados: ")
    print(f'\n*********************************************************')
    for item in resultados:
        print("CEP:       ", item.get("cep"))
        print("Logradouro:", item.get("logradouro"))
        print("Bairro:    ", item.get("bairro"))
        print("Cidade:    ", item.get("localidade"))
        print("Estado:    ", item.get("estado"))
        print("UF:        ", item.get("uf"))
        print("*********************************************************")
else:
    print("Não houve sucesso na requisição.")
