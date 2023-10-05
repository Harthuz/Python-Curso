nome = input('Digite seu nome: ')

tamanho_do_nome = len(nome)
contador = 0
nome_final = ""

while contador<tamanho_do_nome:
    nome_final += "*" + nome[contador]
    contador += 1

print(nome_final)