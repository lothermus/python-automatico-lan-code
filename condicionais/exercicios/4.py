# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:

# Nota 9 ou 10: "Excelente!"

# Nota 7 ou 8: "Muito bom"

# Nota 5 ou 6: "Regular"

# Menor que 5: "Ruim"

avaliacao = int(input('Digite a nota do filme: '))

if avaliacao >= 9:
    print('Excelente!')

elif avaliacao >= 7:
    print('Muito bom!')

elif avaliacao >= 5:
    print('Regular!')

else:
    print('Ruim!')