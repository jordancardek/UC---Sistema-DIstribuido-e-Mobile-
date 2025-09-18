import requests

url = 'https://viacep.com.br/ws/'
cep_inicial = 30180122
formato = '/xml/'

# loop de 5 CEPs
for i in range(5):
    cep = str(cep_inicial + i)

    r = requests.get(url + cep + formato)

    print(f'\n_________________________')
    print(f'\nCEP: {cep}  ')
    print(f'_________________________')
    if r.status_code == 200:
        print('XML:')
        print(r.text) 
    else:
        print('Não houve sucesso na requisição.')