valor_um = input('Digite o primeiro valor')
valor_dois = input('Digite o segundo valor')

if valor_um > valor_dois:
    print(f'{valor_um=} é maior do que {valor_dois=}')
elif valor_um == valor_dois:
    print('Os valores digitados são iguais')
elif valor_um < valor_dois:
    print(f'{valor_dois=} é maior do que {valor_um=}')