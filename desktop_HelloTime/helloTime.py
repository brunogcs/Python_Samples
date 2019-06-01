import time
import timeit

def mensagemSleep():
    print('Respeita meu\nparagrafo rapaz')
    time.sleep(1)
    pass

def mensagemMethod(msg):
    print(msg)
    return msg


if __name__ == "__main__":
    #Passar mensagem por parametro
    msg = 'Receba esta mensagem meu jovem'
    mensagemMethod(msg.upper())
    mensagemMethod(msg.lower())
    mensagemMethod(msg.capitalize())
    mensagemMethod('Aqui está o que foi digitado querido colaborador: {}'.format(msg))
    mensagemMethod('Digite seu nome meu amigo: ')
    mensagemMethod(input())

    # Quanto tempo demora para executar um modulo - mensagemSleep
    inicioTempo = time.time()
    mensagemSleep()
    fimTempo = time.time()
    estimativa = fimTempo-inicioTempo
    print('Tempo para finalizar o modulo mensagem: ' + str(estimativa))
    pass