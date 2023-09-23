def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro Value/Type')
            continue
        except (KeyboardInterrupt):
            print('Entrada interrompida')
            return 0
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'O valor foi {num}')
