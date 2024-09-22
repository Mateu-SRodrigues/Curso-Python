# Q.50) Jogo da velha
lista = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
contar_jogadas = 0
jogador = 'X'

def imprimir_tab():
    print('\nJOGO DA VELHA\n')
    print('', lista[0][0], '|', lista[0][1], '|', lista[0][2])
    print('---+---+---')
    print('', lista[1][0], '|', lista[1][1], '|', lista[1][2])
    print('---+---+---')
    print('', lista[2][0], '|', lista[2][1], '|', lista[2][2])

def exect_jogada(jogada):
    if jogada == 1 and lista[0][0] == ' ':
        lista[0][0] = jogador
        return True
    elif jogada == 2 and lista[0][1] == ' ':
        lista[0][1] = jogador
        return True
    elif jogada == 3 and lista[0][2] == ' ':
        lista[0][2] = jogador
        return True
    elif jogada == 4 and lista[1][0] == ' ':
        lista[1][0] = jogador
        return True
    elif jogada == 5 and lista[1][1] == ' ':
        lista[1][1] = jogador
        return True
    elif jogada == 6 and lista[1][2] == ' ':
        lista[1][2] = jogador
        return True
    elif jogada == 7 and lista[2][0] == ' ':
        lista[2][0] = jogador
        return True
    elif jogada == 8 and lista[2][1] == ' ':
        lista[2][1] = jogador
        return True
    elif jogada == 9 and lista[2][2] == ' ':
        lista[2][2] = jogador
        return True

while contar_jogadas <= 9:
    imprimir_tab()
    jogada = input('Escolha uma posição entre 1 e 9: ')
    exect_jogada()
    contar_jogadas += 1
    break