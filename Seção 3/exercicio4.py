# nome = input('Digite o seu nome: ')
# idade = input('Digite a sua idade: ')

# if nome == '':
#     print('Você naõ digitou seu nome.')
# elif idade == '':
#     print('Você naõ digitou a sua idade.')
# else:
#     print(f'Seu nome é: {nome}')
#     print(f'Seu nome invertido é: {nome[::-1]}')

#     if (' ' in nome):
#         print('Seu nome contém espaços')
#     else:
#         print('Seu nome não contém espaços')
        
#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A ultima letra do seu nome é {nome[(len(nome)-1)]}')

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade: # não precisa colocar != porque o Python interpreta uma variavel str vazia como False, e se tiver qualquer letra ele interpretará como True
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if (' ' in nome):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[(len(nome)-1)]}')
else:
    print('Desculpe, você deixou campos vazios')