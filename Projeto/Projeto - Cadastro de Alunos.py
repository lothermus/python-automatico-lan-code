

inicio = print(input('Seja bem-vindo! Selecione uma opção: \n1.Adicionar Aluno\n2.Listar todos os Alunos\n3.Buscar Aluno pelo nome\n4.Remover Aluno\n5.Mostrar média geral das notas\n6.Sair: '))

nome_aluno = []

match inicio:
    case 1:
        nome = input('Digite o nome do aluno: ')
        nome_aluno = nome
    case _:
        
