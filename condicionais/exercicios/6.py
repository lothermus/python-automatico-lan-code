# Crie um menu com 3 opções:

# 1. Pizza

# 2. Sushi

# 3. Salada

# O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválida."

menu = int(input('Selecione qual prato você irá querer (1) Pizza - (2) Sushi - (3) Salada: '))
match menu:
    case 1:
        print('A opção escolhida foi Pizza!')
    case 2:
        print('A opção pedida foi Sushi!')
    case 3:
        print('A opção pedida foi Salada!')
    case _:
        print('Opção inválida!')

    
