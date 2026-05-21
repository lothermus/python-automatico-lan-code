# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).

# Quando o usuário digitar 0, o programa para e mostra o total economizado.

total = 0

while True:
    valor = int(input('Insira um valor no cofrinho: '))
    if valor == 0:
        break
    total += valor
print(f'O valor total guardado no cofrinho é: {total} reais!')