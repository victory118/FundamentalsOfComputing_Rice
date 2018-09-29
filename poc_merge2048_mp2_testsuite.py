"""
Template testing suite for merge 2048 game in mini-project 2 of Principles of Computing Part 1
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class(3, 4)
    
    # add tests using suite.run_test(....) here

    # test initial configuration of the grid
    suite.run_test(game.get_grid_height(), 3, "Test #0: get_grid_height")
    suite.run_test(game.get_grid_width(), 4, "Test #0: get_grid_width")

    # test the initial configuration of the board using the str method
    # suite.run_test(str(game), str([0]), "Test #0: init")

    # check the str and get_num_seeds methods
    # config1 = [0, 0, 1, 1, 3, 5, 0]    
    # game.set_board(config1)   
    # suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
    # suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    # suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    # suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")    
    
    # report number of tests and failures
    suite.report_results()