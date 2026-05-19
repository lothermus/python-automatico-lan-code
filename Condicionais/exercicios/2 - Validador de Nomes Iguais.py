# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.

print('Vou te falar se os nomes digitados são diferentes ou iguais!')
nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')

if nome1 == nome2: # Novamente, verifica se o Nome 1 é igual "==" ao Nome 2
    print('Esses nomes são iguais!')

if nome1 != nome2: # Esse "!=" é um operador equivalente ao <>. De que se a resposta for DIFERENTE da esperada.
    print('Os nomes digitados são diferentes!')