peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('SOBREPESO!')
elif 30 <= imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')

