# Uma tupla é imutável, os valores dentro da mesma não podem mudar.

# Aqui, eu printo qual é a cor que está no index na posição [2]:
cores = ('azul', 'vermelho', 'verde')
print(cores[2])

# Aqui, vou tentar declarar outra cor para a tupla:

cores[2] = 'amarelo'

print(cores)

# Ele apresenta um erro pois uma tupla é imutável!