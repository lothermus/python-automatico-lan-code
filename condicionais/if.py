# idade = int(input('Qual é sua idade? '))
# if idade > 17:
#     print('Você é maior de idade!')

# if idade < 18:
#     print('Você é menor de idade!')

senha = 'batatinha'

tentativa_senha = input('Digite sua senha: ')
if tentativa_senha == senha:
    print('Senha correta!')
    print('Seja bem vindo!')
if tentativa_senha != senha:
    print('Senha incorreta')