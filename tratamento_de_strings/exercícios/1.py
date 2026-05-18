# Exercício 1 – Primeira e Última Letra
# Peça ao usuário para digitar uma palavra. Mostre:

# A primeira letra

# A última letra

req = input('Digite uma palavra: ')

first = req[0]
last = req[-1]

print(f'A primeira letra da palavra é: {first} e a segunda é: {last}')