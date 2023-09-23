num = (int(input('Número: ')), int(input('Número: ')), int(input('Número: ')), int(input('Número: ')))
print(f'Você digitou os valores: {num}')
print(f'9 apareceu {num.count(9)}')
if 3 in num:
    print(f'3 apareceu na posição {num.index(3)+1}')
else:
    print('Valor 3 não digitado')
print('Valores pares: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


