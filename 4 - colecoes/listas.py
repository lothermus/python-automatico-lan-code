# Esse é o exemplo de uma lista:
frutas = ['maçã', 'banana', 'laranja']

# Se quisermos pegar algum item dessa lista, podemos apenas utilizar o [] (index) para citar o item da lista
# Novamente, o index funciona:
# 'maçã' , 'banana', 'laranja
#  [0]       [1]        [2]

print(frutas[1])

# Se utilizado o index de forma negativa, é puxado também de trás pra frente.
print(frutas [-1]) #Faz com que o primeiro item do index de trás pra frente seja puxado


# Se utilizado o comando .append(), ele irá adicionar alguma outro string para a lista:
frutas.append('melancia')
print(frutas)

# Para remover um item da lista, utilizamos o .remove() na mesma:
frutas.remove('banana')
print(frutas)

# Para substituir um item de uma lista, declaramos a variável junto com a posição na lista, e declaramos o novo valor:

frutas[2] = 'uva' #Isso fará que o item 2 da lista seja substituído por 'uva'
print(frutas)

# O len() é utilizado para contar quantos itens possui dentro de uma lista:

print(f'A lista tem um total de {len(frutas)} frutas!')

# Também é possível utilizar o .insert() para adicionar um valor entre um index e outro:
# Se quisermos adicionar um item entre o index 1 e 2

print('-----------')
print('Exemplo de frutas.insert(1, "goiaba"): ')
frutas.insert(1, 'goiaba')
print(frutas)
print('-----------')

# É possível também remover com base no index, declarando qual iremos remover:

print('Exemplo de remoção pelo index utilizando o .pop(): ')
fruta_removida = frutas.pop(3)
print(frutas)

#É possível também extrair o item removido pelo .pop() e guardar ele em uma variável:

print(f'A fruta removida do index foi {fruta_removida}, as frutas restantes são: {frutas}')

# Para organizar uma lista, utilizamos o .sort()

frutas.sort()
print(frutas)

# Para descobrirmos em qual posição está o item na lista, utilizamos o .index()
print('--------------')
print('Mostrando em qual posição um item está dentro da lista:')
print(f'Essas são as frutas da nossa lista atual: {frutas}')
print(f'A fruta Laranja na lista está na posição {frutas.index('laranja')} do index')
print('--------------')

# Se fossemos contar quantas vezes um item aparece na lista:
print('Para contar quantas vezes um item aparece na lista utilizando o .count()')
print(f'A fruta Maçã aparece {frutas.count('maçã')} vezes dentro da lista!')
print('--------------')

# Se colocarmos uma variável dentro de outra, toda modificação feita na nova variável, irá modificar a original:
# print('Se for alterado uma variável dentro de outra, a original será alterada também: ')
# frutas2 = frutas
# frutas2.append('Melancia')
# frutas.append('Uva')

# print('Print da variável frutas:')
# print(frutas)
# print('Print da frutas2:')
# print(frutas2)

# print('--------------')

print('Se alterado utilizando o .copy(), não irá afetar a variável original:')

frutas2 = frutas.copy()
frutas2.append('Melancia')
frutas2.append('Uva')

print(f'A lista original é: {frutas}')
print(f'A lista alterada com .copy() é {frutas2}')

print('--------------')