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
    tabuleiro = f'{matriz[0][0]} {matriz[0][1]} {matriz[0][2]}\n{matriz[1][0]} {matriz[1][1]} {matriz[1][2]}\n{matriz[2][0]} {matriz[2][1]} {matriz[2][2]}'
    return tabuleiro

def logic(matriz):
    if(
        matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X' or # HORIZONTAL
        matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X' or # HORIZONTAL
        matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X' or # HORIZONTAL
        matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X' or # VERTICAL
        matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X' or # VERTICAL
        matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X' or # VERTICAL
        matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X' or
        matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X'
        ):
        return 1
    elif(
        matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O' or # HORIZONTAL
        matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O' or # HORIZONTAL
        matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O' or # HORIZONTAL
        matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O' or # VERTICAL
        matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O' or # VERTICAL
        matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O' or # VERTICAL
        matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O' or
        matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O'
    ):
        return 2

def game(play = 0, stop = 0):
    if stop == 0:
        while play < 9 :
            if play % 2 == 0:
                print('Player 1')
                coord_x, coord_y = getValue()
                if matriz[coord_x][coord_y] == '*':
                    matriz[coord_x][coord_y] = 'X'
                    tabuleiro = updateTabuleiro(matriz)
                    print('-----')
                    print(tabuleiro)
                    print('-----')
                    if(logic(matriz) == 1):
                        print('Player 1 Win!')
                        break
                        break
                else:
                    print('This local is used. Please, choose a other local.')
                    game(play)
            else:
                print('Player 2')
                coord_x, coord_y = getValue()
                if matriz[coord_x][coord_y] == '*':
                    matriz[coord_x][coord_y] = 'O'
                    tabuleiro = updateTabuleiro(matriz)
                    print('-----')
                    print(tabuleiro)
                    print('-----')
                    if(logic(matriz) == 2):
                        print('Player 2 Win!')
                        break
                        break
                else:
                    print('This local is used. Please, choose a other local')
                    game(play)
            
            if play == 8:
                return 0
            play += 1
    else:
        return 1

if __name__ == '__main__':
    matriz = [
        ['*','*','*'],
        ['*','*','*'],
        ['*','*','*'],
    ]

    tabuleiro = updateTabuleiro(matriz)

    print(f'X1 * * *\nX2 * * *\nX3 * * *\n   Y Y Y\n   1 2 3')
    game_play = game()
    if game_play == 0:
        print('Tie')
