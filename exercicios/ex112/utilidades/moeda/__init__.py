def aumentar(preco = 0,taxa = 0):
    res =  preco + (preco * taxa/100)
    return res


def diminuir(preco = 0 , taxa = 0):
    res =  preco - (preco * taxa/100)
    return res


def dobro(preco = 0):
    res = preco * 2
    return res

def metade(preco = 0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.', ',')


def resumo(preco=0,taxa=10,taxar=5):
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Metade do Preço: {metade(preco, True)}')



