# O dicionário consegue armazenar uma série de informações, seja strings, valores, listas, etc.

pessoa = {
    'nome': 'Paulo',
    'idade': 40,
    'cidade': 'Divinópolis',
    'profissao': ['Programador', 'Pedreiro', 'Mecânico']
}

# Para consultarmos essas informações, declaramos o dicionário + a chave que está a informação que eu quero:
print('Valores que estão dentro da chave [profissao]: ')
print(pessoa['profissao'])

# Agora para acessar um index específico da chave, ao printar, selecionamos o index da chave que queremos:

print('------------')
print('Irei pegar somene o index [2] da chave: ')
print(pessoa['profissao'][2])
print('------------')

# Também podemos utilizar o comando .keys() para fazer a listagem das chaves dentro do dicionário:
print('Keys/Chaves dentro do dicionário: ')
print(pessoa.keys())
print('------------')

# É possível também citar os VALORES que estão armazenados dentro das chaves do nosso dicionário:
print('Valores que estão dentro das chaves do nosso dicionário: ')
print(pessoa.values())
print('------------')

# Também é possível encapsular e transformar a key em uma lista, para que possamos citar os mesmos através do index:
print('Encapsulando a chave para segmentar a mesma pela posição do index: ')
valores = list(pessoa.values())
print(valores[1])
print('------------')

# Se utlizarmos o .items() conseguimos também citar as keys com os conteúdos das mesmas

print('Encapsulamentos utilizando o .items()')
print(pessoa.items())

print('------------')

# Se tentarmos buscar uma chave que não existe no dicionário, buscamos utilizando o .get()
# E caso não tenha esse valor, será preenchido como "None" no console

print(pessoa.get('telefone', 'Não existe')) # Dando uma " , " e passando uma string, o erro é informado como a string!
print('------------')

# Também é possível remover uma chave do dicionário utilizando o .pop()
print('Removendo a key de "Profissões" utilizando o .pop(): ')
item_removido = pessoa.pop('profissao')
print(f'A key removida foi a {item_removido}')
print('O restante das chaves é: ')
print(pessoa)