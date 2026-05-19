# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

# Se o usuário e a senha estão corretos → "Login bem-sucedido"

# Senão → "Usuário ou senha incorretos"

credenciais = {
    'usuario': 'wash',
    'senha': '1234'
}

login = input('Digite aqui seu login: ').lower()
password = (input('Digite aqui sua senha: '))

if login == credenciais['usuario'] and password == credenciais['senha']:
    print('Login bem-sucedido')

else:
    print('Usuário ou senha incorretos')