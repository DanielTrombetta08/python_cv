salario = float(input('Qual o salário do funcionário R$? '))

if salario <= 1.250:
    aumento = (salario * 15/100)
else:
    aumento = (salario * 10/100)

print('Seu salário novo é R${}'.format(salario + aumento))
