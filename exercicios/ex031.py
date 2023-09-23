d = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))

if d <= 200:
    passagem = 0.50
    print('Você pagará R${} por essa viagem!'.format(d*passagem))
else:
    passagem = 0.45
    print('Você pagará R${} por essa viagem!'.format(d * passagem))
