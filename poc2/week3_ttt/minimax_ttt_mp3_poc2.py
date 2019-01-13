"""
Mini-max Tic-Tac-Toe Player
"""

# codeskulptor link: http://www.codeskulptor.org/#user45_3ngnpqtj8K8KhMu_29.py

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # if game is over, return score
    winner = board.check_win()
    if winner != None:
        return SCORES[winner], (-1, -1) 
      
    empty_squares = board.get_empty_squares()
    
    if len(empty_squares) > 0:
        best_score = -1*SCORES[player] # initialize with worst possible score
        best_move = (-1, -1)
        for square in empty_squares:
            board_copy = board.clone()
            board_copy.move(square[0], square[1], player)
            score, _ = mm_move(board_copy, provided.switch_player(player))
            
            if score*SCORES[player] == 1:
                # found best possible score, return that score and move
                return score, square
            elif player == provided.PLAYERX and score >= best_score:
                # update best_score and best_move if better than previous
                best_score = score
                best_move = square
            elif player == provided.PLAYERO and score <= best_score:
                # update best_score and best_move if better than previous
                best_score = score
                best_move = square
    
    return best_score, best_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# For console mode:
# play_game function simulates game between two AI players
# move_wrapper = function that calculates the move for each AI
# 1 = ntrials (used for Monte Carlo method, not for this one)
# provided.play_game(move_wrapper, 1, False)

# For gui mode:
# run_gui function allows you to play against an AI player
# 3 = board size
# provided.PLAYER0 = aiplayer
# move_wrapper = ai function that calculates optimal move for aiplayer
# False = choose whether to reverse (default = False)
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#winner = 'PLAYERX'
#print SCORES[getattr(provided,winner)]
#print provided.PLAYERX
#print SCORES[2]

#board = [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
#         [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
#         [provided.EMPTY, provided.PLAYERO, provided.EMPTY]]
#board = [[provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
#         [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
#         [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]]
#board = [[provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
#         [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
#         [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]]
#ttt_board = provided.TTTBoard(3, False, board)
#print ttt_board
#
#print mm_move(ttt_board, provided.PLAYERO)

#board = [[provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
#         [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
#         [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]]
#ttt_board = provided.TTTBoard(3, False, board)
#print ttt_board
#
#print mm_move(ttt_board, provided.PLAYERX)

