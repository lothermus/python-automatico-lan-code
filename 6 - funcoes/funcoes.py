# def saudacao ():
#     print('Olá, seja bem vindo!')

# saudacao()

# def saudacao (nome): # Aqui é difinido a FUNÇÃO e o parâmetro dela é NOME
#     print(f'Olá {nome}, seja bem vindo!') # Aqui irá imprimir o 'nome' que colocaremos no argumento ao chamar a função

# saudacao('Wash') #Aqui é quando o argumento é enviado para a função

# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     print(f'O a soma de {numero1} e {numero2} é: {resultado}')

# somar(10, 10)


# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado # Retorna o valor de resultado

# resultado_soma = somar(10, 10)
# print(f'O resultado da soma é: {resultado_soma}')


def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100) # O desconto é o PREÇO X (VEZES) o desconto dividido por 100
    preco_final = preco - desconto # Aqui o preço final vai ser calculado com o preço - (MENOS) o desconto
    return preco_final

print(calcular_desconto(200, 34)) # Aqui colocamos o preço e o percentual de desconto: 200 reais / 34% de desconto