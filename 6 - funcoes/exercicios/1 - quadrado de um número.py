# Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.

# Depois, use a função com um valor recebido via input() e exiba o resultado com print().

def quadrado(numero):
    num = numero * numero
    return num

numero = int(input('Digite um número para calcularmos seu quadrado: '))

print(f'O quadradado de {numero} é: {quadrado(numero)}')