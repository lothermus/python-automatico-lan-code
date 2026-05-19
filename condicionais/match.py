# Para fazermos uma especie de "assertação" em Python, utilizamos o match. De que caso Y esteja em X, mostra uma opção:

#O usuário escolhe uma opção, e a variável armazena essa opção:
opcao = int(input('Escolha uma opção de 1 a 3: '))
match opcao:
    case 1:
        print('Você escolheu a opção 1!')
    case 2:
        print('Você escolheu a opção 2!')
    case 3:
        print('Você escolheu a opção 3!')

# O match consegue fazer a distinção do que foi escolhido, e o CASE seria um CASO seja opção X > Mostra Y coisa.


# Em CASE também conseguimos colocar uma espécide de "filtro" de que se o input Z estiver entre X e Y, mostra algo:
nota = int(input('Digite uma nota:'))
match nota:
    case 10 | 9: #Aqui,  essa tubulação (| |) diz, se o input estiver entre 10 e 9, mostra o print ()
        print('Excelente!')
    case 8 | 7:
        print('Muito bom!')
    case 6 | 5:
        print('Dá pra ser melhor!')
    case 4 | 3 | 2 | 1:
        print('Reprovado!')
    case _: #A condicional CASE_ é algo como o ELSE, de que se não for nenhum dos casos, mostrará essa opção!
        print('Opção inválida!')