# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

numeros = [] # Aqui vai armazenar os números

for n in range (1,6):
    numero = int(input('Digite um número: ')) # Aqui cria a variável que vai armazenar o que o usuário vai digitar
    numeros.append(numero) # Aqui adiciona o número digitado dentro da lista

resultado = 0 # Uma variável pra armazenar a soma dos resultados

for numero in numeros:
    resultado += numero # Aqui soma os números armazenados

print(f'O resultado da soma dos números é: {resultado}')