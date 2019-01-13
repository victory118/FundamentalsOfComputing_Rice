"""
Monte Carlo Tic-Tac-Toe Player
"""
# http://www.codeskulptor.org/#user45_giN8EIWEBt_30.py
# http://www.codeskulptor.org/#poc_ttt_provided.py
# http://www.codeskulptor.org/#poc_ttt_template.py

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player
    by making random moves, alternating between players. The function 
    should return when the game is over. The modified board will contain
    the state of the game, so the function does not return anything.
    In other words, the function should modify the board input
    """
    empty = board.get_empty_squares()
    while board.check_win() is None:
        next_move = empty.pop(random.randrange(0, len(empty)))
        board.move(next_move[0], next_move[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same
    dimensions as the Tic-Tac-Toe board, a board from the completed game, 
    and which player the machine player is. The function should score the
    completed board and update the scores grid. As the function updates 
    the scores grid directly, it does not return anything.
    """
    if board.check_win() == player:
        player_score_val = SCORE_CURRENT
        opp_score_val = -SCORE_OTHER
    elif board.check_win() == provided.switch_player(player):
        player_score_val = -SCORE_CURRENT
        opp_score_val = SCORE_OTHER
    else:
        player_score_val = 0
        opp_score_val = 0

    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if player == board.square(row, col):
                scores[row][col] += player_score_val
            elif provided.switch_player(player) == board.square(row, col):
                scores[row][col] += opp_score_val
                
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function
    should find all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple. It is an error to call this
    function with a board that has no empty squares (there is no possible next
    move), so your function may do whatever it wants in this case. The case 
    where the board is full will not be tested.
    """
    
    empty_squares = board.get_empty_squares()
    
    if len(empty_squares) > 0:
        empty_scores = []
        for square in empty_squares:
            empty_scores.append(scores[square[0]][square[1]])
    
        max_squares = [empty_squares[idx] for idx in range(len(empty_squares)) \
                        if empty_scores[idx] == max(empty_scores)]
        return max_squares[random.randrange(0,len(max_squares))]
    else:
        return (0, 0)

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run. This function should use the
    Monte Carlo simulation described above to return a move for the
    machine player in the form of a (row, column) tuple.
    """
    scores = [[0 for _ in range(board.get_dim())] for _ in range(board.get_dim())]
    board_copy = board.clone()
    for _ in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
        
    return get_best_move(board, scores)
        

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

#game = provided.TTTBoard(3)
#print str(game)

#mc_trial(game, provided.PLAYERX)

#print str(game)