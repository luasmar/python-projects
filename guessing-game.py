import random

print('Jogo de Adivinhação')
print('===================')

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativas += 1
    chute = int(input('Digite um número entre 1 e 100: '))
    if chute == numero_secreto:
        print(f'Parabéns! Você acertou em {tentativas} tentativas.')
        break
    elif chute > numero_secreto:
        print('O número é menor. Tente novamente.')
    else:
        print('O número é maior. Tente novamente.')
