lista_um = []
mai = men = 0

for c in range(0,5):
    lista_um.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista_um[c]
    else:
        if lista_um[c] > mai:
            mai = lista_um[c]
        if lista_um[c] < men:
            men = lista_um[c]

print(f'Você digitou os valores {lista_um}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')

for i, v in enumerate(lista_um):
    if v == mai:
        print(f'{i}...')
print(f'O menor valor digitado foi {men} nas posições ', end='')

for i, v in enumerate(lista_um):
    if v == men:
        print(f'{i}...', end='')
