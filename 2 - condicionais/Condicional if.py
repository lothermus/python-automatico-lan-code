# Iremos fazer uma condicional if, de que se digitado uma idade MAIOR que 18 anos, diremos que a pessoa é maior de idade.
idade = int(input('Qual é sua idade? '))
if idade > 17:
    print('Você é maior de idade!')

#Aqui, também vamos dizer de que se a idade for MENOR que 18 anos, diremos que a pessoa é menor de idade.
if idade < 18:
    print('Você é menor de idade!')

# Utilizando os operadores > (Maior que) e < (Menor que), também temos o >= (Maior ou igual) e <= (Menor ou igual) para filtrar um operador no "meio termo"
print('Para andar no brinquedo, você precisa ter no mínimo 1,65cm de altura!')
result = float(input('Digite aqui sua altura: '))

if result < 1.65:
    print('Você não pode andar no brinquedo!')

if result >= 1.65:
    print('Você pode andar no brinquedo!')