import requests
import sqlite3
from datetime import datetime

# Configuração
API_KEY = "ad548c7d"  
URL = f"https://api.hgbrasil.com/finance?format=json-cors&key=ad548c7d"

# Requisição
resposta = requests.get(URL)
if resposta.status_code == 200:
    dados = resposta.json()

    # Cotações desejadas
    dolar = dados['results']['currencies']['USD']['buy']
    euro = dados['results']['currencies']['EUR']['buy']
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Data: {data_atual}")
    print(f"Dólar: {dolar}")
    print(f"Euro: {euro}")

    # Conectando com banco de dados
    conexao = sqlite3.connect("C:/Users/Koda/Desktop/UC---Sistema-DIstribuido-e-Mobile-/Prática 02/bdcotacoes.db")

    cursor = conexao.cursor()

    conexao.commit()
    conexao.close()

    print("Cotações salvas com sucesso no banco de dados!")
else:
    print("Erro ao acessar a API")
