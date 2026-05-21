# 🧪 Exercício 2 – Manipulando uma lista
# Dada a lista abaixo:

# livros = ["Python", "Java", "C++"]
# Realize as seguintes ações:

# Adicione o livro "JavaScript"

# Remova o livro "Java"

# Troque "Python" por "Go"

# Mostre o tamanho da lista

livros = ["Python", "Java", "C++"]

print('Adicionando JavaScript na lista:')
livros.append('JavaScript')
print(livros)
print('----------')

print('Removendo o livro Java: ')
print(f'O livro Java está na posição: {livros.index('Java')}')
livros.pop(1)
print('Agora a lista ficou com os livros restantes: ')
print(livros)
print('----------')

print('Trocando "Python" for "Go": ')
print(f'O livro Python está na posição {livros.index('Python')} da lista')
livros[0] = 'Go'
print(livros)
print('----------')

print('Fazendo a contagem de quantos itens possuem na lista: ')
print(f'A lista tem um tamanho total de: {len((livros))} itens.')