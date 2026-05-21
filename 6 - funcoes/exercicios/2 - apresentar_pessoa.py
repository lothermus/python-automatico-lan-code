# Crie uma função chamada apresentar_pessoa(nome, idade) que exibe a seguinte mensagem:

# "Nome: <nome> | Idade: <idade> anos"
# Chame a função passando valores diferentes.


def apresentar_pessoa(nome, idade): # A função espera receber nome e idade
    print(f' Nome: {nome} | Idade: {idade} anos.') # Aqui imprimimos e colocamos os valores do parâmetro da função

nome = input('Digite seu nome: ') # Criamos o input que pede o nome da pessoa
idade = int(input('Digite sua idade: ')) # Criamos o input que pede a idade da pessoa
apresentar_pessoa(nome, idade) # Aqui "resgatamos" o print lá de cima, e mostramos tudo formatado


