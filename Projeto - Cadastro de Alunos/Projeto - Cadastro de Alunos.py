
alunos = []

while True:

    inicio = int(input('Seja bem-vindo! Selecione uma opção: \n1.Adicionar Aluno\n2.Listar todos os Alunos\n3.Buscar Aluno pelo nome\n4.Remover Aluno\n5.Mostrar média geral das notas\n6.Sair: '))


    match inicio:
        case 1:
            while True:
                aluno = {
                'nome': '',
                'idade': '',
                'nota': ''
                }
                nome_aluno = input('Digite o nome do aluno a ser adicionado: ').lower()
                aluno['nome'] = nome_aluno 

                idade_aluno = input('Digite a idade do aluno: ')
                aluno['idade'] = idade_aluno

                while True: 
                    nota_aluno = float(input('Digite a nota do aluno: '))
                    if nota_aluno <= 10:
                        aluno['nota'] = float(nota_aluno)
                        break
                    else:
                        print('A nota precisa estar entre 0 e 10!')

                alunos.append(aluno)

                continuar = input('Você quer cadastrar outro aluno? S/N: ').lower()
                if continuar != 's':
                    break
        case 2:
            if not alunos:
                print('Não há alunos disponíveis.')

            else:
                for n in alunos:
                    print(f'Os alunos até agora são: Nome: {n["nome"].capitalize()} | Idade: {n["idade"]} anos, Nota: {n["nota"]}')
        case 3:
            while True:

                busca = input('Qual o nome do aluno que gostaria de buscar?: ').lower()

                encontrado = False

                for aluno in alunos:
                    if busca == aluno['nome'].lower():
                        encontrado = True
                        break
                        
                if encontrado:
                    print(f'O aluno {busca.capitalize()} está presente na lista de alunos!')
                else: 
                    print('Não existe esse aluno na lista de alunos.')

                busca_cont = input('Gostaria de buscar outro aluno? S/N: ').lower()
                if busca_cont != 's':
                    break

        case 4:
            while True:

                remove = (input('Qual aluno você quer remover?: ')).lower()

                pesq = False

                for aluno in alunos:

                    if remove == aluno['nome'].lower():
                        alunos.remove(aluno)
                        pesq = True

                        print('Aluno removido.')

                        break

                else:
                    print('Não existe esse aluno na lista de alunos.')
                
                pergunta = input('Gostaria de remover outro aluno? S/N: ').lower()

                if pergunta != 's':
                    break
        
        case 5:

            if not alunos:
                print('Não há alunos cadastrados.')

            else:

                print('O total de notas cadastradas no sistema é: ')

                for aluno in alunos:
                    print(aluno['nota'])

                soma_notas = 0

                for aluno in alunos:
                    soma_notas += aluno['nota']

                media = soma_notas / len(alunos)

                print(f'A soma de todas notas é: {soma_notas} e a média de todas as notas é: {media:2f}')

        case 6:
            print('Você saiu.')
            break

        case _:
            print('Digite uma opção válida!')