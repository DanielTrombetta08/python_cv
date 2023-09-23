num = [[], []]
valor = 0

for c in range(1,5):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}')
