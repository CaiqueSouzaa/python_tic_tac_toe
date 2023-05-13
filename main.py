def getValue():
    try:
        coord_x = int(input('Type the coordinate X:'))
    except:
        print("-------------------\nInvalid value for coordinate X. Please, try again or type '69' for exit of game.\n-------------------")
        try:
            if coord_x == 69:
                game(0, 1)
        except:
            game()
        #print("This value isn't valid.")

    try:
        coord_y = int(input('Type the coordinate Y:'))
    except:
        print("Invalid value for coordinate Y. Please, try again or type '69' for exit of game.")
        try:
            if coord_y == 69:
                game(0, 1)
        except:
            game()

    return ((coord_x - 1), (coord_y - 1))

def updateTabuleiro(matriz):
    tabuleiro = f'X-1 {matriz[0][0]} {matriz[0][1]} {matriz[0][2]}\nX-2 {matriz[1][0]} {matriz[1][1]} {matriz[1][2]}\nX-3 {matriz[2][0]} {matriz[2][1]} {matriz[2][2]}'
    return tabuleiro

def game(play = 0, stop = 0):
    if stop == 0:
        while play < 9:
            if play % 2 == 0:
                print('Player 1')
                coord_x, coord_y = getValue()
                if matriz[coord_x][coord_y] == '*':
                    matriz[coord_x][coord_y] = 'X'
                    tabuleiro = updateTabuleiro(matriz)
                    print(tabuleiro)
                else:
                    print('This local is used. Please, choose a other local.')
                    game(play)
            else:
                print('Player 2')
                coord_x, coord_y = getValue()
                if matriz[coord_x][coord_y] == '*':
                    matriz[coord_x][coord_y] = 'O'
                    tabuleiro = updateTabuleiro(matriz)
                    print(tabuleiro)
                else:
                    print('This local is used. Please, choose a other local')
                    game(play)

            play += 1
    else:
        return 1


matriz = [
    ['*','*','*'],
    ['*','*','*'],
    ['*','*','*'],
]

tabuleiro = updateTabuleiro(matriz)

print(f'    -----\n{tabuleiro}\n    -----')
game_play = game()
