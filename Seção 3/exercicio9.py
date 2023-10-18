print('\n Olá :) \n Seja bem vindo ao Adivinhord \n Para jogar apenas digite uma letra, e eu te direi se a letra digitada está na palavra que eu estou pensando... \n Vamos começar! \n')

palavra_secreta = "hernandes"
tamanho_palavra_secreta = len(palavra_secreta)
acertou = False
quantidade_letras_certas = 0
letras_certas = ""
tentativas = 0

while acertou != True:
    status_palavra = ""


    if quantidade_letras_certas < 1:
        chute = input('Digite a primeira letra: ')
    else:
        chute = input('Digite outra letra: ')

    if len(chute) > 1: # verificando se o usuário digitou mais que uma letra
        print('\n Digite apenas uma letra.\n')
        continue

    if chute in palavra_secreta:

        letras_certas += chute

        if quantidade_letras_certas == 0:
            print('\n Você acertou uma letra \n')
        if quantidade_letras_certas > 0:
            print('\n Você acertou outra letra \n')
        
        quantidade_letras_certas += 1

        if "h" and "e" and "r" and "n" and "a" and "n" and "d" and "e" and "s" in letras_certas:
            acertou = True

        
        
    else:
        if quantidade_letras_certas < 1:
            print('\n Vish \n Parece que você começou com o pé direito \n Tente novamente \n')
        elif quantidade_letras_certas == 1:
            print('\n Tente novamente \n')
        elif quantidade_letras_certas >1 and quantidade_letras_certas < 3:
            print('\n Tente novamente \n')
        elif quantidade_letras_certas >2 and quantidade_letras_certas < 5:
            print('\n Continue a nadar... continue a nadar... \n')
        elif quantidade_letras_certas == 5:
            print('\n Continue tentando, uma hora você consegue \n Ou não :/ \n')
        elif quantidade_letras_certas == 6:
            print('\n Parece que eu peguei pesado na palavra escolhida :| \n Mas não desista \n')
        elif quantidade_letras_certas == 20:
            print('\n Eu vou dormir, não aguento mais esperar \n')
        elif quantidade_letras_certas >20:
            print('\n Zzzzzzzzzzzzzzzzzz \n')
        else:
            print('\n Tente novamente \n')


    for chute in letras_certas:
        if chute in letras_certas:
            print(chute)
        else:
            print('*')
    
    print(f'{status_palavra} \n')

    tentativas += 1

print(f'\n Parabéns, você venceu \n A palavra era "{palavra_secreta}" \n você precisou de {tentativas} tentativas para acertar \n')

# não consegui imprimir a "status_palavra" do jeito que deveria e não criei uma verificação caso o usuário digite mais de uma letra