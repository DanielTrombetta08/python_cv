numero = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado...')
    else:
        print('Valor duplicado.')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(numero.sort())
print(f'Você digitou os valores {numero}')
