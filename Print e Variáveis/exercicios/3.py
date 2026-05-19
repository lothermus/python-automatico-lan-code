# Crie um código onde o usuário deve digitar três notas escolares e calcular a média delas.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

soma = nota1 + nota2 + nota3
media = soma / 3

print(f'A média das notas é: {media}!')