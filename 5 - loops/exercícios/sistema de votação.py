# Crie um sistema de votação onde o usuário escolhe entre:

# 1."Pizza"

# 2."Hambúrguer"

# 3."Sair"

# Enquanto ele não digitar "3", continue perguntando

# No final, mostre quantos votos cada item recebeu


voto_pizza = 0
voto_burg = 0

while True:
    voto = int(input('Digite seu voto: \n1. Pizza\n2. Hambúrger\n3. Sair: '))
    if voto == 1:
        voto_pizza += 1
    elif voto == 2:
        voto_burg += 1
    else:
        break

print(f'O valor total de votos é: Pizza: {voto_pizza}, Hambúrguer: {voto_burg}')