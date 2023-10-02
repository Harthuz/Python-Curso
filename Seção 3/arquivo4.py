nome = 'Hernandes Arthur'
altura = 1.75
peso = 65
imc = peso/altura**2
string = 'O {0} tem {1} de altura e pesa {2}, seu IMC é de {3:.2f}'
    
print(
    string.format(
    nome, altura, peso, imc
    )
)