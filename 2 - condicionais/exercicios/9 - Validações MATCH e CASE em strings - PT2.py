# Aqui foi utilizado o .strip() e .lower() para fazer o "tratamento" da string. Pois possa ser
# que o usuário digite sem fazer a identação carta, colocando letra maíuscula, etc.
jogo = input('Qual desses jogos é seu favorito? Dark Souls | Metal Gear | Xenoblade: ').strip().lower()

match jogo:
    case 'dark souls':
        print('Então você deve gostar de Soulslikes como Elden Ring, Nine Sols e Hollow Knight!')
    case 'metal gear':
        print('Então você gosta muito do Kojima!')
    case 'xenoblade':
        print('Sabia! Você deve gostar bastante de Persona então!')
    case _:
        print('Opção inválida! Digite o nome corretamente do jogo!')