import os
from random import randint

def cabecalho():
    print('******************************')
    print('*    Jogo da adivinhação     *')
    print('******************************')

def nivelDificuldade():
    numero_tentativas=0
    print('*** Escolha o Nivel ***') 
    print('1 - Facil\n'+'2 - Medio\n'+'3 - Dificil\n') 
    nivel = int(input())
    os.system('cls')
    if(nivel==1):
        numero_tentativas = 20
    elif(nivel==2):
        numero_tentativas = 10
    elif(nivel==3):
        numero_tentativas = 5
    return numero_tentativas

def numeroSecretoAleatorio():
    numero_secreto = randint(0,100)
    return numero_secreto

def desafio():
    # Declarando variaveis
    rodada = 1
    pontos = 0
    # Recebendo variaveis dos metodos
    numero_tentativas = nivelDificuldade()
    
    while(rodada==1):
        # Declarando variaveis
        numero_tentativa_atual = 1
        # Recebendo variaveis dos metodos
        numero_secreto = numeroSecretoAleatorio()
        for x in range(numero_tentativas):

            print('Tentativa {} de {}'.format(numero_tentativa_atual,numero_tentativas))
            numero_tentativa_atual = numero_tentativa_atual + 1
            chute = int(input ('Digite o seu numero: '))

            acertou = numero_secreto==chute
            maior   = chute>numero_secreto
            menor   = chute<numero_secreto

            if(x==numero_tentativas-1 and maior):
                print('You Lose! Menos')
                pontos = pontos - 1
                print('GAME OVER! O numero era: {}'.format(numero_secreto))
            elif(x==numero_tentativas-1 and menor):
                print('You Lose! Mais')
                pontos = pontos - 1
                print('GAME OVER! O numero era: {}'.format(numero_secreto))
            elif(acertou):
                print('You Win! O numero gerado foi: {}'.format(numero_secreto))
                pontos = pontos + 1
                break
            elif(maior):
                print('You Lose! Menos')
            elif(menor):
                print('You Lose! Mais')
        pass
        print('Sua pontuação é: {}'.format(pontos))

        print('Deseja melhorar sua pontuação?')
        print('1- Sim\n2- Não')
        rodada = int(input())
        os.system('cls')

    pass

if __name__ == "__main__":
    cabecalho()
    desafio()
    print('End of Game')
    pass