horario = input('Digite o horário (ex: 13): ')

try:
    int(horario)
except:
    print('Você não digitou um número, o programa não pode prosseguir :/')

horario = int(horario)

if horario>0 and horario<12:
    print('Bom dia')
elif horario>11 and horario<18:
    print('Boa tarde')
elif horario>17 and horario<24:
    print('Boa noite')
else:
    print('Digite um horario válido, de 0 a 23.')