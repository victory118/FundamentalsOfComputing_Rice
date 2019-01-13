"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

# codeskulptor link: http://www.codeskulptor.org/#user45_p90Q475kJmF28bj_213.py

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        
        # Return false if any of these conditions are not met:
        
        
        # Tile zero is positioned at (i,j)
        if self.get_number(target_row, target_col) != 0:
            return False
        
        # All tiles in rows i + 1 or below are positioned at their solved location
        
        # initialize a puzzle object with all tiles in correct location
#        init_obj = Puzzle(self.get_height(), self.get_width())
        
        for idx in range(target_row + 1, self.get_height()):
#            print "checking row", idx
#            print range(self.get_width()*idx, self.get_width()*(idx + 1))
#            print self._grid[idx]
            
#            if init_obj._grid[idx] != self._grid[idx]:
#                return False
            if range(self.get_width()*idx, self.get_width()*(idx + 1)) != self._grid[idx]:
                return False
            
        # All tiles in row i to the right of position (i,j) are positioned at their solved location.
        if target_col < self.get_width() - 1:
            
#            print "checking target row"
#            rows_right = self.get_width() - target_col - 1
            
#            print range(self._grid[target_row][target_col + 1], self._grid[target_row][target_col + 1] + rows_right)
#            print range(self.get_width()*target_row + target_col + 1, self.get_width()*(target_row + 1))
    
            if range(self.get_width()*target_row + target_col + 1, self.get_width()*(target_row + 1)) != self._grid[target_row][target_col+1:]:
                return False
            
#            if range(self._grid[target_row][target_col + 1], self._grid[target_row][target_col + 1] + rows_right) != self._grid[target_row][target_col+1:]:
#                return False
        
        # Otherwise return True
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
#        print self
#        print target_row
#        print target_col
        assert self.lower_row_invariant(target_row, target_col)
        
        # find position of next_tile on the grid
        next_tile_pos = self.current_position(target_row, target_col)
        
        move_string = ''
        
        # next_tile is to the left of target_col
        if next_tile_pos[1] < target_col:
            
            # calculate horizontal distance between next_tile and target_col
            left_dist = target_col - next_tile_pos[1]
        
            if next_tile_pos[0] == target_row: # next_tile is also in target_row
            
                # move zero_tile to swap places with next_tile
                move_string += 'l'*left_dist
            
                # move next_tile right to target_col
                move_string += 'urrdl'*(left_dist-1)
                
            else: # next_tile is not in (above) target row
                
                # move zero_tile to same row as next_tile
                up_dist = target_row - next_tile_pos[0]
                move_string += 'u'*up_dist
                
                # move zero_tile left to swap places with next_tile
                move_string += 'l'*left_dist
                
                # move next_tile right to target_col
                move_string += 'drrul'*(left_dist-1)
                
                # move next_tile down to target_row
                move_string += 'druld'*up_dist
        
        # next_tile is in target_col
        elif next_tile_pos[1] == target_col:
            
            # move zero_tile up to swap places with next_tile
            up_dist = target_row - next_tile_pos[0]
            move_string += 'u'*up_dist
            
            # move zero_tile to left of next_tile
            move_string += 'ld'
            
            # move next_tile down to target_row
            move_string += 'druld'*(up_dist-1)
            
        elif next_tile_pos[1] > target_col: # next_tile is to the right of target_col
            
            up_dist = target_row - next_tile_pos[0]
            right_dist = target_col - next_tile_pos[1]
            
            # move zero_tile up to same row as next_tile
            up_dist = target_row - next_tile_pos[0]
            move_string += 'u'*up_dist
            
            # move zero_tile right to swap places with next_tile
            right_dist = target_col - next_tile_pos[1]
            move_string += 'r'*right_dist
            
            # move next_tile left to target_col
            if up_dist == 1: # next_tile is one row above target_row
                move_string += 'ulldr'*(right_dist-1)
                move_string += 'ulld'
            else: # next tile is two or more rows above target_row
                move_string += 'dllur'*(right_dist-1)
                move_string += 'dllu'
            
            # move next_tile down to target_row
            move_string += 'druld'*up_dist
        
        # update puzzle
#        print "Finished calculating move_string in solve_interior_tile"
        self.update_puzzle(move_string)
        
        assert self.lower_row_invariant(target_row, target_col-1)
        
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        
        # find position of next_tile on the grid
        next_tile_pos = self.current_position(target_row, 0)
        
        move_string = ''
        
        # next_tile in col0
        if next_tile_pos[1] == 0:
#            print "first if"
            # calculate vertical distance between next_tile row and target_row
            up_dist = target_row - next_tile_pos[0]
            
            # move zero_tile up to swap with next_tile
            move_string += 'u'*up_dist
            
            if up_dist > 1:
                # get zero_tile and next_tile into special position
                move_string += 'rdl'
                move_string += 'druld'*(up_dist-2)
                
                # execute move in special position
                move_string += 'ruldrdlurdluurddlur'
                
                # move zero_tile into next starting position
                move_string += 'r'*(self.get_width()-2)
            else:
                # move zero_tile into next starting position
                move_string += 'r'*(self.get_width()-1)
        elif next_tile_pos[0] == target_row - 1:
            # next_tile is in row directly above target_row
#            print "second if"
            
            # get zero_tile and next_tile into special position
            move_string += 'u'
            right_dist = next_tile_pos[1]
            
            if right_dist > 1:
                move_string += 'r'*right_dist
                move_string += 'ulldr'*(right_dist - 2)
                move_string += 'ulld'
                
            # execute move in special position
            move_string += 'ruldrdlurdluurddlur' 
            
            # move zero_tile into next starting position
            move_string += 'r'*(self.get_width-2)
            
        else: # next_tile is not in col0 and not in target_row-1
#            print "third if"
#            print self
            # get zero_tile and next_tile into special position
            up_dist = target_row - next_tile_pos[0]
            right_dist = next_tile_pos[1]
                
            if right_dist > 1:
                move_string += 'u'*up_dist
                move_string += 'r'*right_dist
                move_string += 'dllur'*(right_dist-2)
                move_string += 'dlu'
            else:
                move_string += 'u'*(up_dist-1)
                move_string += 'ru'
                    
            move_string += 'lddru'*(up_dist-2)
            move_string += 'ld'
            
            # execute move in special position
            move_string += 'ruldrdlurdluurddlur' 
            
            # move zero_tile into next starting position
            move_string += 'r'*(self.get_width()-2)
        
        # update puzzle
        self.update_puzzle(move_string)
        
        assert self.lower_row_invariant(target_row-1, self.get_width()-1)
        
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        
        # check that tile zero is at (0, j)
#        print "row0_invariant test1"
        if self._grid[0][target_col] != 0:
            return False
        
        # check that all positions to the right of (0, j) on row 0 are solved
#        print "row0_invariant test2"
#        print range(self.get_width() + target_col, 2*self.get_width())
#        print self._grid[1][target_col:]
        if target_col <= self.get_width() - 2:
            
#            print range(target_col + 1, self.get_width())
#            print self._grid[0][target_col+1:]
            
            if range(target_col + 1, self.get_width()) != self._grid[0][target_col+1:]:
                return False
            
        # check that all positions to starting on (1,j) to the right are solved
#        print "row0_invariant test3"
#        print range(self.get_width() + target_col, 2*self.get_width())
#        print self._grid[1][target_col:]
        if range(self.get_width() + target_col, 2*self.get_width()) != self._grid[1][target_col:]:
                return False
            
        # All tiles in rows i + 1 or below are positioned at their solved location
                
        for idx in range(2, self.get_height()):

            if range(self.get_width()*idx, self.get_width()*(idx + 1)) != self._grid[idx]:
                return False
        
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        
        # Returns true if both conditions are met:
        # 1) tile zero is at (1, j)
        # 2) all positions either below or to the right of this position are solved
        
        # Tile zero is positioned at (1,j) and all positions below and to the right of 
        # (1,j) on row 1 are solved
        if not self.lower_row_invariant(1, target_col):
            return False
        
        # check that all positions above and to the right of (1,j) are solved
        if target_col <= self.get_width() - 2:
            if range(target_col + 1, self.get_width()) != self._grid[0][target_col+1:]:
                return False
            
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        # find position of next_tile on the grid
        next_tile_pos = self.current_position(0, target_col)
        
        move_string = ''
        
        left_dist = target_col - next_tile_pos[1]
        
        # if next_tile was at (0,j-1), then you're done
        if next_tile_pos[0] == 0 and left_dist == 1:
            move_string += 'ld'
            
            # update puzzle
            self.update_puzzle(move_string)
            assert self.row1_invariant(target_col-1)
            
            return move_string
        
        # else move next_tile to pos (1,j-1) and zero_tile to (1,j-2)
        if next_tile_pos[0] == 0: # next_tile in row0
            
            # move zero_tile to next_tile col
            move_string += 'l'*left_dist
            
            # move into special position before executing move*
            move_string += 'dru'
            
            if left_dist == 2:
                move_string += 'ld'
            else:
                move_string += 'rdl'
                move_string += 'urrdl'*(left_dist-3)
            
        else: # next_tile in row1
            
            if next_tile_pos[1] == target_col - 1:
                move_string += 'lld'
            else:
                move_string += 'ld'
                # move zero_tile left to swap with next_tile
                move_string += 'l'*(left_dist-1)
                
                # move into special position before executing move*
                move_string += 'urrdl'*(left_dist-2)
        
        # execute special move
        move_string += 'urdlurrdluldrruld'
        
        # update puzzle
        self.update_puzzle(move_string)
        assert self.row1_invariant(target_col-1)      
        
        return move_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        # find position of next_tile on the grid
        next_tile_pos = self.current_position(1, target_col)
        
        move_string = ''
        
        left_dist = target_col - next_tile_pos[1]
        
        if left_dist == 0:
            move_string += 'u'
            assert self.row1_invariant(target_col)
            self.update_puzzle(move_string)
            assert self.row0_invariant(target_col) 
            return move_string
            
        # move zero_tile to next_tile col
        move_string += 'l'*left_dist
        
        # if next_tile is in row0
        if next_tile_pos[0] == 0:
            
            # move zero_tile up to swap
            move_string += 'u'
            
            # move next_tile right one space
            move_string += 'rdl'
        
        # move next_tile right into solved position
        move_string += 'urrdl'*(left_dist-1)
        
        # move zero_tile into invariant position
        move_string += 'ur'
        
        # update puzzle
        assert self.row1_invariant(target_col)
        self.update_puzzle(move_string)
        assert self.row0_invariant(target_col)      
        
        return move_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        
        move_string = ''
        move_list = ['l','u','r','d']
        move_count = 0
        
        while not self.row0_invariant(0):
            next_move = move_list[move_count % 4]
            move_string += next_move
            self.update_puzzle(next_move)
            move_count += 1
            
        return move_string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        
        move_string = ''
        
        if self.row0_invariant(0):
            return move_string
        
        # move zero_tile to bottom right corner
        zero_tile_pos = self.current_position(0, 0)
        right_dist = self.get_width() - zero_tile_pos[1] - 1
        down_dist = self.get_height() - zero_tile_pos[0] - 1
        
        move_string += 'r'*right_dist + 'd'*down_dist
        
        self.update_puzzle(move_string)
        
        assert self.lower_row_invariant(self.get_height()-1, self.get_width()-1)
        
        # Phase one
#        print "Phase One"
        for row in range(self.get_height()-1, 1, -1):
            for col in range(self.get_width()-1, -1, -1):
#                print "(row, col) = ", row, ",", col
                assert self.lower_row_invariant(row, col)
                if col > 0:
                    move_string += self.solve_interior_tile(row, col)
                    assert self.lower_row_invariant(row, col-1)
                else:
                    move_string += self.solve_col0_tile(row)
                    assert self.lower_row_invariant(row-1, self.get_width()-1)
        
        # Phase two
#        print "Phase Two"
        assert self.row1_invariant(self.get_width()-1)
        for col in range(self.get_width()-1, 1, -1):
#            print "(row, col) = ", 1, ", ", col
#            print self
            move_string += self.solve_row1_tile(col)
#            print "(row, col) = ", 0, ", ", col
#            print self
            move_string += self.solve_row0_tile(col)
            
        # Phase three
#        print "Phase Three"
        move_string += self.solve_2x2()
        
        return move_string

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

def lower_row_variant_test():
    """
    Unit test results for lower_row_variant function
    """
    print "Unit Tests for lower_row_variant"
    
    print "Test 1"
    obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    assert obj.lower_row_invariant(2, 2) == True
    
    print "Test 2"
    obj = Puzzle(4, 5, [[15, 11, 10, 9, 8], [7, 6, 5, 4, 3], [2, 1, 0, 13, 14], [12, 16, 17, 18, 19]])
    assert obj.lower_row_invariant(2, 2) == False
    
    print "Test 3"
    obj = Puzzle(4, 5, [[12, 11, 10, 9, 8], [7, 6, 5, 4, 3], [2, 1, 0, 13, 14], [15, 16, 17, 18, 19]])
    assert obj.lower_row_invariant(2, 2) == True
    
def row1_invariant_test():
    """
    Unit Tests for row1_invariant function
    """
    print "Unit test results for row1_invariant"
    
    obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
    assert obj.row1_invariant(1) == True
    
def row0_invariant_test():
    """
    Unit Tests for row0_invariant function
    """
    print "Unit test results for row0_invariant"
    
    obj = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    assert obj.row0_invariant(0) == True
    
    obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
    assert obj.row0_invariant(2) == False
    
def solve_interior_tile_test():
    """
    Unit tests for solve_interior_tile function
    """
    print "Unit test results for solve_interior_tile"
    
    obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    assert obj.lower_row_invariant(2, 2)
    obj.solve_interior_tile(2, 2)
    assert obj.lower_row_invariant(2, 1)
    
def solve_col0_tile_test():
    """
    Unit tests for solve_col0_tile function
    """
    print "Unit test results for solve_col0_tile"
    
    obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])
    obj.solve_col0_tile(2)
    
def solve_row1_tile_test():
    """
    Unit tests for solve_row1_tile function
    """
    print "Unit test results for solve_row1_tile"
    
    obj = Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]])
    obj.solve_row1_tile(2)
    
def solve_row0_tile_test():
    """
    Unit tests for solve_row0_tile function
    """
    print "Unit test results for solve_row0_tile:"
    
    obj = Puzzle(3, 3, [[2, 4, 0], [1, 3, 5], [6, 7, 8]])
    obj.solve_row0_tile(2)
    print "Test 1 passed"
    
    obj = Puzzle(4, 5, [[1, 2, 0, 3, 4], [6, 5, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
    obj.solve_row0_tile(2)
    print "Test 2 passed"
    print obj
    
def solve_2x2_test():
    """
    Unit tests for solve_2x2 function
    """
    print "Unit test results for solve_2x2:"
    obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
    obj.solve_2x2()
    
def solve_puzzle_test():
    """
    Unit tests for solve_2x2_puzzle function
    """
    print "Unit test results for solve_puzzle:"
    obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    obj.solve_puzzle()
    print "Test 1 succeeded"
    print obj
    
    obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
    obj.solve_puzzle()
    print "Test 2 succeeded"
    print obj
    
#lower_row_variant_test()
#row1_invariant_test()
#row0_invariant_test()
#solve_interior_tile_test()
#solve_col0_tile_test()
#solve_row1_tile_test()
#solve_row0_tile_test()
#solve_2x2_test()
#solve_puzzle_test()

#obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
#poc_fifteen_gui.FifteenGUI(obj)

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

#puzzle=Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
#poc_fifteen_gui.FifteenGUI(puzzle)
#sol=puzzle.solve_puzzle()
#print sol
#print len(sol)
