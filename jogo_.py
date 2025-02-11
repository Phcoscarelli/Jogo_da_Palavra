import os 

palavra_secreta = 'pessoa'
letras_corretas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_corretas += letra_digitada
    
    palavra_usuario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_usuario += letra_secreta
        else:
            palavra_usuario += '*'
    
    print('Letras corretas:', palavra_usuario)


    if palavra_usuario == palavra_secreta:
        os.system('cls')
        print('Você ganhou, parabéns!')
        print ('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_corretas = ''
        numero_tentativas = 0 