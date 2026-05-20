# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

# Se o usuário e a senha estão corretos → "Login bem-sucedido"

# Senão → "Usuário ou senha incorretos"

credenciais = {
    'usuario': 'wash',
    'senha': 1234
}

login = {
    'usuario': input('Digite seu usuário: ').lower(),
    'senha': int(input('Digite sua senha: '))
}

if login ['usuario'] == credenciais ['usuario'] and login['senha'] == credenciais ['senha']:
    print('Usuário logado')
else:
    print('Credenciais inválidas, tenta novamente!')