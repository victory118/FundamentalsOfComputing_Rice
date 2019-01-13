"""
Clone of 2048 game.
"""

# codeskultor link
# http://www.codeskulptor.org/#user45_TwSZ5m25iV_4.py

# templates
# http://www.codeskulptor.org/#poc_2048_template.py

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    # create a new list with zero elements removed
    new_list = [num for num in line if num!=0]

    # iterate through new list and merge if two consecutive elements are equal
    # set the first element to twice its original value
    # set the second element equal to zero
    idx = 0
    while idx < len(new_list)-1:
        if new_list[idx]==new_list[idx+1]:
            new_list[idx] *= 2
            new_list[idx+1] = 0
            idx += 2
        else:
            idx += 1
    # create a new list by once again removing all zeros
    merged_list = [num for num in new_list if num!=0]
    # pad the new list with zeros so its the same length as the original list
    merged_list.extend([0 for num in range(0,len(line)-len(merged_list))])
    return merged_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._initial_tiles = {}
        self._initial_tiles[UP] = [(0, col) for col in range(grid_width)]
        self._initial_tiles[DOWN] = [(grid_height-1, col) for col in range(grid_width)]
        self._initial_tiles[LEFT] = [(row, 0) for row in range(grid_height)]
        self._initial_tiles[RIGHT] = [(row, grid_width-1) for row in range(grid_height)]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [ [0 for _ in range(self._grid_width)] for _ in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        prt_str = ''
        for idx in range(len(self._grid)):
            prt_str += str(self._grid[idx]) + '\n'
        return prt_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        start_tiles = self._initial_tiles[direction]
        
        if direction == UP or direction == DOWN:
            line_num_el = len(self._initial_tiles[LEFT])
        else:
            line_num_el = len(self._initial_tiles[UP])
        
        row_offset = OFFSETS[direction][0]
        col_offset = OFFSETS[direction][1]
        
        line_changed = False
            
        for tile in start_tiles:
            line = []
            for idx in range(line_num_el):
                line.append(self._grid[tile[0] + row_offset*idx][tile[1] + col_offset*idx])
            merged_list = merge(line)
            
            if line_changed:
                pass
            elif merged_list!= line:
                line_changed = True
            
            for idx in range(line_num_el):
                self._grid[tile[0] + row_offset*idx][tile[1] + col_offset*idx] = merged_list[idx]
        
        if line_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        # find all indices that contain zeros
        # loop through each nested list (row) for each element (column)
        zero_tiles = [(row, col) for row in range(self._grid_height) \
                      for col in range(self._grid_width) \
                      if self._grid[row][col] == 0]
        tiles_changed = 0
        while tiles_changed < min(1, len(zero_tiles)):
            new_tile_idx = zero_tiles[random.randrange(0, len(zero_tiles))]
            if self._grid[new_tile_idx[0]][new_tile_idx[1]] == 0:
                self._grid[new_tile_idx[0]][new_tile_idx[1]] = 2 if random.random() < 0.9 else 4
                tiles_changed += 1

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
game = TwentyFortyEight(3,4)
print str(game)
grid_height = 3
grid_width = 4

game.new_tile()
print str(game)

num_turns = 10
for i in range(num_turns):
   turn = random.randint(1,4)
   print turn
   game.move(turn)
   print str(game)

import poc_merge2048_mp2_testsuite
poc_merge2048_mp2_testsuite.run_suite(TwentyFortyEight)