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


def game(n_rows, n_cols, n_players):
    check_value(n_rows, 'Number of rows')
    check_value(n_cols, 'Number of columns')
    check_value(n_players, 'Number of players')

    print('Initializing game with params: \n' +\
    'n_rows: {}\nn_cols: {}\nn_players {}'.format(n_rows, n_cols, n_players))
    players = []
    for player_idx in range(n_players):
        players.append(Player(player_idx + 1))

    board = Board(n_rows, n_cols)
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

    args = parser.parse_args()
    try:
        game(args.rows, args.cols, args.players)
    except Exception as e:
        print(str(e) + '\nTerminating..')
        sys.exit()
