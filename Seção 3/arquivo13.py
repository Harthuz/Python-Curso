# try exept

numero = input('Digite um número: ')

try:
    numero_float = float(numero)
    print(numero_float)
except:
    print('Você não digitou um número válido.')