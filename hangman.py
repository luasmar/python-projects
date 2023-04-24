import random

palavras = ['python', 'java', 'javascript', 'html', 'css']
palavra = random.choice(palavras)
acertos = []
erros = []

while len(erros) < 6:
    for letra in palavra:
        if letra in acertos:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

    palpite = input('Digite uma letra: ')
    if palpite in palavra:
        acertos.append(palpite)
    else:
        erros.append(palpite)
        print('Você errou! Restam', 6-len(erros), 'tentativas.')
    if set(acertos) == set(palavra):
        print('Parabéns, você venceu!')
        break

if len(erros) == 6:
    print('Game over! A palavra era', palavra)
