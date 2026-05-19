# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

nota = int(input('Digite sua nota: '))
nota_minima = int(6)

if nota == 10: #O "==" é um operador em Python que verifica se o valor é EXATO ao que for digitado
    print(f'Você tirou {nota}! Você tirou a nota mínima!')

if nota > 10:
    print(f'Você tirou {nota}! Ela foi maior que a média!')

if nota < 10:
    print(f'Sua nota foi {nota}! Ela infelizmente foi menor que a média!')