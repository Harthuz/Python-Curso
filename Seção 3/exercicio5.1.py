numero_inteiro = input('Digite um número inteiro: ')

try:
    if int(numero_inteiro)%2==0:
        print('O número digitado é par')
    else:
        print('O número digitado é impar')
except:
    print('Você não digitou um número inteiro.')