#Uma variável consegue armazenar números, guardando eles dentro de "caixinhas"

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

print(f'O primeiro número é: {primeiro_numero}')
print(f'O segundo número é: {segundo_numero}')

# No caso de númeors inteiros, é possível fazer operações matemáticas com esses números:
soma = primeiro_numero + segundo_numero

print(f'A soma de {primeiro_numero} e de {segundo_numero} é: {soma}')

#O f utilizado no print() é pra indicar uma "formatação" durante o print. O que me permite colocar variáveis dentro de uma string (ou texto)