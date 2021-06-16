'''Elabore um jogo de pedra papel tesoura, em que o úsuario pode escolher se quer jogar com um amigo ou
contra o computador. Gere na tela de saida o jogador que venceu, e uma pergunta se ele deseja jogar uma
nova rodada.'''

import random

def jogada(player1,player2):
    if player1 == 'pedra' and player2 == 'tesoura':
        return player1
    elif player1 == 'pedra' and player2 == 'papel':
        return player2
    elif player1 == 'papel' and player2 == 'tesoura':
        return player2
    elif player1 == 'papel' and player2 == 'pedra':
        return player1
    elif player1 == 'tesoura' and player2 =='papel':
        return player1
    elif player1 == 'tesoura' and player2 == 'pedra':
        return player2
    elif player1 == player2:
        return 0
def menu_multiplayer (round,name):
    print (f'\nrodada numero {round}')
    print (f'Vez do jogador: {name}')
    print('1-pedra\n2-papel\n3-tesoura')
    selecionar=int (input('Selecione: '))
    return selecionar
def menu_computador (round):
    print (f'\nrodada numero {round}')
    print('1-pedra\n2-papel\n3-tesoura')
    selecionar=int (input('Selecione: '))
    return selecionar


if __name__ == '__main__':


    opcoes=['pedra','papel','tesoura']
    nome=[]

    print ('PEDRA PAPEL TESOURA GAME')
    print ('Deseja jogar contra o computador ou multiplayer?')
    print ('1-Computador\n2-Multiplayer')
    modo=int (input ('insira o modo de jogo: '))
    if modo == 1:
        rodada=1
        while True:
            jogada_computador=random.choice(opcoes)
            selecao=menu_computador(rodada)
            jogada_jogador=opcoes[selecao-1]
            vitorioso=jogada(jogada_computador,jogada_jogador)
            print ('=-'*30)
            print (f'{jogada_computador} X {jogada_jogador} = {vitorioso}')
            if jogada_computador == vitorioso:
                print ('COMPUTADOR VENCEU')
            elif jogada_jogador == vitorioso:
                print ('VOCE VENCEU')
            else:
                print ('EMPATE')
            print ('\nDeseja jogar mais uma rodada?')
            print ('1-sim\n2-nao e sair do jogo')
            new_game=int (input ())
            if new_game == 2:
                break
            else:
                rodada+=1
    else:
        rodada=1
        for b in range (2):
            nome_jogadores= str (input(f'Insira o nome do {b+1}º jogador: '))
            nome.append(nome_jogadores)
        while True:
            print ('\n')
            #primeiro jogador
            selecao1=menu_multiplayer(rodada,nome[0])
            jogada_1=opcoes[selecao1-1]

            print ('\n'*100)
            #segundo jogador
            selecao2=menu_multiplayer(rodada,nome[1])
            jogada_2=opcoes[selecao2-1]

            vitorioso=jogada(jogada_1,jogada_2)
            print ('=-'*30)
            print (f'{jogada_1} X {jogada_2} = {vitorioso}')
            if jogada_1 == vitorioso:
                print (f'{nome[0]} VENCEU')
            elif jogada_2 == vitorioso:
                print (f'{nome[1]} VENCEU')
            else:
                print ('EMPATE')
            print ('\nDeseja jogar mais uma rodada?')
            print ('1-sim\n2-nao e sair do jogo')
            new_game=int (input ())
            if new_game == 2:
                break
            else:
                rodada +=1


