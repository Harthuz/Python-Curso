nome = input('Qual é o seu nome?')
sexo = input('Você se identifica com o sexo masculino (M) ou feminino (F)')

if sexo == 'M':
    print(f'O aluno {nome} passou de ano')
elif sexo == 'F':
    print(f'A aluna {nome} passou de ano')
else:
    print('Digite uma opção válida.')