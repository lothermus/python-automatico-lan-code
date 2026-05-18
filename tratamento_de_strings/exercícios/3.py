# Exercício 3 – Detectando palavras proibidas
# Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

frase = input('Digite aqui uma frase: ')

if 'bomba' in frase:
    print('Essa palavra é proíbida!')
else:
    print('Frase aceita')