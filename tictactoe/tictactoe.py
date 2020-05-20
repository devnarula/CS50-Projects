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
    scorex = 0
    scoreo = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                scorex += 1;
            elif board[i][j] == O:
                scoreo += 1
    if scorex > scoreo:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibl = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibl.add((i, j))
    return possibl
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x = action[0]
    y = action[1]
    if board[x][y] != EMPTY:
        raise NameError("Invalid Action")
    else:
        copyboard = copy.deepcopy(board)
        copyboard[x][y] = player(board)
        return copyboard
    # raise NotImplementedError


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[2][0]
    return None
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True
    # raise NotImplementedError


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    raise NotImplementedError


# def finalscore(board, isMaximizing):
#     win = winner(board)
#     if win != 0:
#         return utility(board)
#     if (isMaximizing): #playing for AI
#         bestscore = -10000
#         allactions = actions(board)
#         for action in allactions:
#             newboard = result(board,action)
#             score = finalscore(newboard,False)
#             bestscore = max(score,bestscore)
#         return bestscore
#     else: # Playing for Human
#         bestscore = 10000
#         allactions = actions(board)
#         for action in allactions:
#             newboard = result(board, action)
#             score = finalscore(newboard,True)
#             bestscore = min(score,bestscore)
#         return bestscore
#
# def minimax(board):
#     bestscore = -10000
#     possibl = actions(board)
#     move = ()
#     for action in possibl:
#         newboard = result(board,action)
#         print(newboard)
#         print("HI")
#         score = finalscore(newboard,False)
#
#         if score > bestscore:
#             bestscore = score
#             move = action
#     return move

def max_value(board):
    if terminal(board):
        return utility(board)
    bestscore = float('-inf')
    for action in actions(board):
        bestscore = max(bestscore, min_value(result(board,action)))
    return bestscore
def min_value(board):
    if terminal(board):
        return utility(board)
    bestscore = float('inf')
    for action in actions(board):
        bestscore = min(bestscore, max_value(result(board,action)))
    move = action
    return bestscore

def minimax(board):
    if player(board) == X:
        bestscore = float('-inf')
        for action in actions(board):
            score = max(bestscore, min_value(result(board, action)))
            if score > bestscore:
                bestscore = score
                move = action
        return move
    elif player(board) == O:
        bestscore = float('inf')
        for action in actions(board):
            score = min(bestscore, max_value(result(board, action)))
            if score < bestscore:
                move = action
                bestscore = score
        return move