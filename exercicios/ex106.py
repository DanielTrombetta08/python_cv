c = ('\033[m',         # 0 sem cor
     '\033[0;30;41m',  # 1 vermelho
     '\033[0;30;42m'   # 2 verde
     );


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(f'{msg}')
    print(c[0], end='')


comando = ''
while True:
    titulo('Sistema de ajuda PyHelp')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)


