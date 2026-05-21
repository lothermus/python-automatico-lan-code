# Para fazer o sclicing (ou fatiamento) em Python, a primeira parte da string é sempre 0, e a última é última do tamanho da frase.

# No exemplo 'Melancia', o Python se comporta assim:
#  M   E   L   A   N   C   I   A
# [0] [1] [2] [3] [4] [5] [6] [7]                                          

fruta = 'Melancia'

print(fruta[0]) #Irá printar apenas a letra A

print(fruta[0:3]) #Irá printar de [0] até a casa [3] porém não incluirá a casa [3]

print(fruta[3:]) #Irá começar a printar da casa [3] até o final da frase.


# frase = 'Eu amo python!'
# frase_tamanho = len(frase)

# print(f'A frase tem o tamanho de {frase_tamanho} caractéres!')

# frase = 'Eu amo Pyhton!'

# contagem = frase.count('o')

# print(contagem)

#frase = 'Eu amo Python!'

# print(frase.find('m'))

# if 'python' in frase:
#     print('Tem Python na frase!')
# else:
#     print('Python não está na frase')

# print(frase.upper())
# print(frase)
# print(frase.lower())

#print(frase.title())