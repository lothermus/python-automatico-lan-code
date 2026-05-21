# Crie um código onde o usuário deve inserir dois números e exiba a soma, subtração, multiplicação e divisão deles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

resultado_soma = num1 + num2
resultado_sub = num1 - num2
resultado_mult = num1 * num2
resultado_div = num1 / num2

print(f'A soma dos números é: {resultado_soma}, a subtração é: {resultado_sub}, a multiplicação é: {resultado_mult}, e a divisão é: {resultado_div}')