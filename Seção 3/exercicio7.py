while True:
    primeiro_numero = input('\n Digite o primeiro número: ')
    segundo_numero = input('\n Digite o segundo número: ')
    operador = input('\n Soma = + \n Subtração = - \n Divisão = / \n Multiplicação = * \n \n Digite o operador da conta: ')

    try:
        if operador == '+':
            resultado = float(primeiro_numero) + float(segundo_numero)
        elif operador == '-':
            resultado = float(primeiro_numero) - float(segundo_numero)
        elif operador == '*':
            resultado = float(primeiro_numero) * float(segundo_numero)
        elif operador == '/':
            resultado = float(primeiro_numero) / float(segundo_numero)

        print(f'\n {primeiro_numero} {operador} {segundo_numero} = {resultado}')

        finalizar = input('\n Deseja finalizar? (S/N): ').lower().startswith('s')
        if finalizar:
            break

    except:
        print('Você digitou algo invalido.')