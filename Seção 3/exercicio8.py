letra = "Foi numa tarde de domingo Que alguém perguntando por ela chegou Deixando o meu coração tristonho Enciumado, morrendo de amor Eu falei, eu menti, eu chorei, eu sorri dizendo Eu falei, eu menti, eu chorei, eu sorri dizendo Que ela mora no meu peito E eu moro vizinho a ela E eu fico desse jeito Pensando nos beijos, nos carinhos dela Carolina, Carol, Carol, Carolina bela Carolina, Carol, Carol, Carolina bela Foi numa tarde de domingo Que alguém perguntando por ela chegou Deixando o meu coração tristonho Enciumado, morrendo de amor Eu falei, eu menti, eu chorei, eu sorri dizendo Eu falei, eu menti, eu chorei, eu sorri dizendo Que ela mora no meu peito E eu moro vizinho a ela E eu fico desse jeito Pensando nos beijos, nos carinhos dela Carolina, Carol, Carol, Carolina bela Carolina, Carol, Carol, Carolina bela Ca, Ca, Ca, Carol Ca, Ca, Carolina Ca, Ca, Ca, Carol Ca, Ca, Carolina Carolina, Carol, Carol, Carolina bela Carolina, Carol, Carol, Carolina bela Carolina, Carol, Carol, Carolina bela".lower()

qtd_letra = 0
letra_que_mais_aparece = ''
i = 0

while i < len(letra):
    letra_atual = letra[i]
    qtd_letra_atual = letra.count(letra[i])


    if letra_atual == " ":
        i +=1 
        continue

    quntas_vezes_carolina = letra.count("carolina")
    quntas_vezes_carol = letra.count("carol")

    if qtd_letra < qtd_letra_atual:
        qtd_letra = qtd_letra_atual
        letra_que_mais_aparece = letra_atual

    print(letra_atual)

    i += 1

print(f'\n O nome Carolina apareceu {quntas_vezes_carolina} vezes, e o nome Carol apareceu {quntas_vezes_carol} vezes')

print(f'\n Letra que mais apareceu nesta música: {letra_que_mais_aparece.upper()}'
      f'Quantidade de aparições: {qtd_letra}')