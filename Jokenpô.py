from time import sleep
from colorama import init,Fore
from random import randint
init(autoreset=True)
while True:
    print(Fore.YELLOW +'-' * 30 + 'JO,KEN,PO!!!' + '-' * 30)
    itens = 'Pedra', 'Papel','Tesoura'
    computador = randint(0,2)
    print('''Vamos Jogar! Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
    jogador = int(input('Qual é a sua jogada?'))
    if jogador < 0 or jogador > 2:
        print(Fore.RED + '\nERRO: Jogada inválida! Você deve escolher 0, 1 ou 2.')
        print(Fore.RED + 'O programa foi encerrado. Tente rodar novamente.')
    else:# O código só chega aqui se o jogador digitou 0, 1 ou 2
        print(Fore.YELLOW + 'JO')
        sleep(0.5)
        print(Fore.BLUE + 'KEN')
        sleep(0.5)
        print(Fore.RED + 'PO!!!')
        sleep(0.5)
        print('-=' * 20)
        print('O computador jogou {}{}.'.format(Fore.CYAN,itens[computador]))
        print('O jogador jogou {}{}.'.format(Fore.MAGENTA, itens[jogador]))
        print('-=' * 20)
    if computador == 0: #O computador jogou pedra.
        if jogador == 0:
            print('EMPATE.')
        elif jogador == 1:
            print('JOGADOR VENCE.')
        elif jogador == 2:
            print('COMPUTADOR VENCE.')
    elif computador == 1: #Computador jogou papel.
        if jogador == 0:
            print('COMPUTADOR VENCE.')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE.')
    elif computador == 2: # O computador jogou tesoura.
        if jogador == 0:
            print('JOGADOR VENCE.')
        elif jogador == 1:
            print('COMPUTADOR VENCE.')
        else:
            print('EMPATE!')
#Pergunta se quer jogar de novo.
    replay = str(input('Queres jogar de novo?')).strip().upper()
    if replay == 'NÃO':
        print(Fore.CYAN +'Obrigado por jogar.Até a próxima!')
        break#O comando break encerra o loop.
