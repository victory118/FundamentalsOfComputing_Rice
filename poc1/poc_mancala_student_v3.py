Looking for Python 3? Try py3.codeskulptor.org!

Run (Accesskey R)
  
Save (Accesskey S)
  
Download
  
Fresh URL
  
Open Local
  
Reset (Accesskey X)
 CodeSkulptor 
Docs
  
Demos
  
Viz Mode
 
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.board = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        temp = list(self.board)
        temp.reverse()
        return str(temp)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[house_num]
​
    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return True
​
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        pass
​
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        return 0
    
    def plan_moves(self):
        """
        Return sequence of shortest legal moves until none are available
        Not used in GUI version, only for machine testing
        """
        return []
 
# import test suite and run
import poc_mancala_testsuite_v2 as poc_mancala_testsuite
poc_mancala_testsuite.run_suite(SolitaireMancala)
    
​
​

Ran 5 tests. 0 failures.
CodeSkulptor was built by Scott Rixner and is based upon CodeMirror and Skulpt.