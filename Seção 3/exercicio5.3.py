primeiro_nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(primeiro_nome)

if tamanho_nome == 0:
    print('Você não digitou nada.')
elif tamanho_nome>0 and tamanho_nome<=4:
    print('Seu nome é curto.')
elif tamanho_nome>4 and tamanho_nome<7:
    print('Seu nome é normal.')
elif tamanho_nome>6:
    print('Seu nome é muito grande.')