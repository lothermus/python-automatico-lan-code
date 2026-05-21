# Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:

# O valor da compra deve ser maior ou igual a 100

# E o cliente precisa estar cadastrado no programa de fidelidade

# Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"
# Caso contrário: "Frete não disponível gratuitamente."

compra = int(input('Digite aqui o valor da sua compra: '))

fidelidade = False #Aqui validamos se o cliente participa do programa de fidelidade.

if compra >= 100 and fidelidade == True: # Aqui,  código está fazendo uma 'assertividade' de que 'fidelidade' é True.
    print(f'O valor da sua compra foi de {compra} reais. Frete grátis aplicado!')

elif compra >= 100 and fidelidade == False: #Aqui, o código verifica se a fidelidade foi False.
    print(f'Sua compra foi de {compra} reais. Porém você não participa do plano de fidelidade.')

