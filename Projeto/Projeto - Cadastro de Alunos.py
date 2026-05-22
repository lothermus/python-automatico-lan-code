
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
                nome_aluno = input('Digite o nome do aluno a ser adicionado: ')
                aluno['nome'] = nome_aluno 

                idade_aluno = input('Digite a idade do aluno: ')
                aluno['idade'] = idade_aluno

                nota_aluno = input('Digite a nota do aluno: ')
                aluno['nota'] = nota_aluno

                alunos.append(aluno)

                print(f'\nO aluno foi adicionado. Seguem os dados:')
                print(aluno)
                continuar = input('Você quer cadastrar outro aluno? S/N: ').lower()
                if continuar != 's':
                    break
        case 2:
            if not alunos:
                print('Não há alunos disponíveis.')

            else:
                for n in alunos:
                    print(f'Os alunos até agora são: Nome: {n['nome']} | Idade: {n['idade']}, Nota: {n['nota']}')

        case 3:
            while True:
                remove = input('Qual aluno você quer remover?: ').lower()
                if remove in alunos['nome']:
                    alunos.remove(remove)
                
                pergunta = input('Gostaria de remover outro aluno? S/N: ').lower()
                if pergunta != 's':
                    break
            
        case _:
            break