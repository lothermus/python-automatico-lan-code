# Montando um sistema de votação de popularidade dos Jogos:

dark_souls = 0
metal_gear = 0
xenoblade = 0

while True:
    voto = int(input('Vote em seu jogo favorito: \n1. Dark Souls\n2. Metal Gear\n3. Xenoblade\n4. Sair: '))
    match voto:
        case 1:
            dark_souls += 1
        case 2:
            metal_gear += 1
        case 3:
            xenoblade += 1
        case 4:
            break
        case _:
            print('Opção inválida!')

print(f'Os votodos totais são:\nDark Souls: {dark_souls} votos.\nMetal Gear: {metal_gear} votos.\nXenoblade: {xenoblade} votos.')