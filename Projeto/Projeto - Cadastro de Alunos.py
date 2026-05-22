
while True:

    inicio = int(input('Seja bem-vindo! Selecione uma opção: \n1.Adicionar Aluno\n2.Listar todos os Alunos\n3.Buscar Aluno pelo nome\n4.Remover Aluno\n5.Mostrar média geral das notas\n6.Sair: '))

    aluno = {
        'nome': '',
        'idade': '',
        'nota': ''
    }

    alunos = []

    match inicio:
        case 1:
            nome_aluno = input('Digite o nome do aluno a ser adicionado: ')
            aluno['nome'] = nome_aluno 
            idade_aluno = input('Digite a idade do aluno: ')
            aluno['idade'] = idade_aluno
            nota_aluno = input('Digite a nota do aluno: ')
            aluno['nota'] = nota_aluno
            alunos.append(aluno)
            print(f'O aluno foi adicionado. Seguem os dados:')
            print(aluno)
            aluno{}
            print(alunos)
        case 2:
            print('Teste 2')
        case _:
            break