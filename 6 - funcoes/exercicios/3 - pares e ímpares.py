# Crie uma função chamada verificar_par(numero) que retorna:

# "Par" se o número for par

# "Ímpar" se for ímpar

# Peça um número ao usuário com input(), chame a função e mostre o resultado.

def verificar_par(numero):
    if numero % 2 == 0:
        return 'Esse número é Par!'
    else:
        return 'Esse número é Ímpar'
    
numero = int(input('Digite um número e te direi se é Par ou Ímpar: '))

resultado = verificar_par(numero)

print(resultado)