intuito = input('Você deseja entrar, S/N')

if intuito == 'S' or 's':
    print('Você entrou no sitema')
    senha = input('Digite a sua senha:')
    if senha == '123456':
        print('Senha correta, você está logado.')
    else:
        print('Senha incorreta, você foi bloqueado.')
elif intuito == 'N' or 'n':
    print('Você não entrou no sitema')