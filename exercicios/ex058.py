from random import randint
computador = randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Número de 0 a 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Acertou com {} tentativas'.format(palpites))
