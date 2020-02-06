import argparse
import sys
from board import Board
from player import Player


def check_value(variable, variable_name):
    if variable < 0:
        raise Exception("{} cannnot be negative".format(variable_name))


def make_move(player, board):
    print(board)
    print(str(player)+', please choose a column, from 0 to {}'.format(board.n_cols-1))
    right_input = False
    while not right_input:
        try:
            col_idx = int(input())
            board.drop_at(col_idx, player.id)
            right_input = True
        except Exception as e:
            print(e)


def game(args):
    for key, value in args.items():
        check_value(value, 'Number of ' + key)

    print('Initializing game with params: \n' +
    'rows: {}\ncols: {}\nplayers: {}\nwinning pieces: {}'.format(
        args['rows'], args['cols'], args['players'], args['pieces']))
        
    players = []
    for player_idx in range(args['players']):
        players.append(Player(player_idx + 1))

    board = Board(args['rows'], args['cols'], args['pieces'])
    game_on = True

    while game_on:
        for player in players:
            make_move(player, board)
            if board.check_win(player.id):
                print(board)
                print(str(player) + ' won the game!')
                game_on = False
                break
            if board.check_tie():
                print(board)
                print("No more blank cells.. it's a tie!")
                game_on = False
                break


if __name__=='__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-rows", type=int, default=6,
                        help="specify number of rows")
    parser.add_argument("-cols", type=int, default=7,
                        help="specify number of columns")
    parser.add_argument("-players", type=int, default=2,
                        help="specify number of players")
    parser.add_argument("-pieces", type=int, default=4,
                        help="specify number of winning pieces")

    args = parser.parse_args()
    game_args = {
        'rows': args.rows,
        'cols': args.cols,
        'players': args.players,
        'pieces': args.pieces
    }
    try:
        game(game_args)
    except Exception as e:
        print(str(e) + '\nTerminating..')
        sys.exit()
