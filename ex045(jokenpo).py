import time, random
itens= ('Pedra', 'Papel', 'Tesoura')
computador= random.randint (0, 2)
print('''Escolha sua jogada: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador= int (input ('Qual a sua escolha? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
print(':-' * 12)
print('O computador jogou {}'.format (itens[computador]) )
print('O jogador jogou {}'.format (itens[jogador]) )
print(':-' * 12)

if computador == 0: #pedra
    if jogador == 0:
        print ('--> EMPATE')
    elif jogador == 1:
        print ('--> JOGADOR VENCE')
    elif jogador == 2:
        print ('--> COMPUTADOR VENCE')
    else:
        print ('--> JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print ('--> COMPUTADOR VENCE')
    elif jogador == 1:
        print ('--> EMPATE')
    elif jogador == 2:
        print ('--> JOGADOR VENCE')
    else:
        print ('--> JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print ('--> JOGADOR VENCE')
    elif jogador == 1:
        print ('--> COMPUTADOR VENCE')
    elif jogador == 2:
        print ('--> EMPATE')
    else:
        print ('--> JOGADA INVALIDA')
