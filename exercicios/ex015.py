km = float(input('Quantidade de Km percorridos: '))
dias = int(input('Quantidade de dias: '))
d = 60
k = 0.15

print('Percorrendo {}Km em {} dias, você vai pagar R$ {}'.format(km,dias,(km * k) + (dias * d)))
