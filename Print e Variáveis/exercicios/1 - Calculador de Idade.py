# Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.

data_nasc = int(input('Digite sua data de nascimento: '))
ano = int(input('Digite o ano atual: '))
nasc = ano - data_nasc

print(f'Você tem tem {nasc} anos de idade!')