"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        x_count = x_count + row.count(X)
        o_count = o_count + row.count(O)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    i = 0

    for row in board:
        j = 0

        for cell in row:
            if cell == EMPTY:
                possible_actions.add((i, j))
            j = j + 1
        i = i + 1

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("invalid move")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checks winner horizontally
    for row in board:
        if row.count(X) == 3:
            return X

    for row in board:
        if row.count(O) == 3:
            return O

    # checks winner vertically
    if (((board[0][0], board[1][0], board[2][0]).count(X) == 3) or
        ((board[0][1], board[1][1], board[2][1]).count(X) == 3) or
        ((board[0][2], board[1][2], board[2][2]).count(X) == 3)):
        return X

    if (((board[0][0], board[1][0], board[2][0]).count(O) == 3) or
        ((board[0][1], board[1][1], board[2][1]).count(O) == 3) or
        ((board[0][2], board[1][2], board[2][2]).count(O) == 3)):
        return O

    # checks winner diagonally
    if (((board[0][0], board[1][1], board[2][2]).count(X) == 3) or
        ((board[0][2], board[1][1], board[2][0]).count(X) == 3)):
        return X

    if (((board[0][0], board[1][1], board[2][2]).count(O) == 3) or
        ((board[0][2], board[1][1], board[2][0]).count(O) == 3)):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True
    else:
        return len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move


def max_value(board, alpha = float('-inf'), beta = float('inf')):
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    move = None
    for action in actions(board):
        lowest_value = min_value(result(board, action), alpha, beta)[0]

        possible_v = max(v, lowest_value)

        if possible_v > v:
            v = possible_v
            move = action

        if v >= beta:
            return v, move

        if v > alpha:
            alpha = v

    return v, move


def min_value(board, alpha = float('-inf'), beta = float('inf')):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    move = None
    for action in actions(board):
        highest_value = max_value(result(board, action), alpha, beta)[0]

        possible_v = min(v, highest_value)

        if possible_v < v:
            v = possible_v
            move = action

        if v <= alpha:
            return v, move

        if v < beta:
            beta = v

    return v, move
