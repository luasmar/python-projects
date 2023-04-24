import requests

# access the api that fetches the currency rates
url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url)
data = response.json()

moedas = list(data['rates'].keys())

print('Selecione a moeda de origem:')
for i, moeda in enumerate(moedas):
    print(i+1, '-', moeda)
origem = int(input('Escolha uma opção: ')) - 1

print('Selecione a moeda de destino:')
for i, moeda in enumerate(moedas):
    print(i+1, '-', moeda)
destino = int(input('Escolha uma opção: ')) - 1

valor = float(input('Digite o valor a ser convertido: '))

taxa = data['rates'][moedas[destino]] / data['rates'][moedas[origem]]

valor_convertido = valor * (data['rates'][moedas[destino]] / data['rates'][moedas[origem]])

print(f'{valor} {moedas[origem]} equivale a {valor_convertido:.2f} {moedas[destino]}')
