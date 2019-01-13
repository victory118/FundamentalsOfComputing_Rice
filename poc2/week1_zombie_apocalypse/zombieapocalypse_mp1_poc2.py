"""
Student portion of Zombie Apocalypse mini-project
"""
# codeskulptor link: http://www.codeskulptor.org/#user45_IhWbHRN1Q9_58.py

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        
        distance_field = [[self._grid_width*self._grid_height for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        
        boundary = poc_queue.Queue()
#        way = FOUR_WAY # FOUR_WAY or EIGHT_WAY
        
        if entity_type == HUMAN:
            for cell in self._human_list:
#                print cell
#                print visited
                boundary.enqueue(cell)
                visited[cell[0]][cell[1]] = FULL
                distance_field[cell[0]][cell[1]] = 0
#            way = EIGHT_WAY
        elif entity_type == ZOMBIE:
            for cell in self._zombie_list:
                boundary.enqueue(cell)
                visited[cell[0]][cell[1]] = FULL
                distance_field[cell[0]][cell[1]] = 0
        
#        print boundary
#        print visited
#        print distance_field
        
#        for _ in range(2):
        while len(boundary) > 0:
            
            cell = boundary.dequeue()
#            print "cell = ", cell
#            if way == FOUR_WAY:
#                neighbors = self.four_neighbors(cell[0], cell[1])
#            elif way == EIGHT_WAY:
#                neighbors = self.eight_neighbors(cell[0], cell[1])
            neighbors = self.four_neighbors(cell[0], cell[1]) 
#            print "neighbors = ", neighbors    
            for neighbor in neighbors:
#                print "neighbor = ", neighbor
                passable = self.is_empty(neighbor[0], neighbor[1])
#                print "passable = ", passable
                if not visited[neighbor[0]][neighbor[1]] and passable:
#                    print "updating"
                    visited[neighbor[0]][neighbor[1]] = FULL
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
                    boundary.enqueue(neighbor)
#                print "visited = ", visited
#                print "distance_field = ", distance_field
#                print "boundary = ", boundary
                
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_list = []
        # move each human in human_list
        for cell in self.humans():
            distances = []
            neighbors = self.eight_neighbors(cell[0], cell[1])
            
            # for each neighbor cell, check distance to nearest zombie
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    distances.append(zombie_distance_field[neighbor[0]][neighbor[1]])
                else:
                    distances.append(-1)
            
            # for current cell, check distance to nearest zombie
            neighbors.append(cell)
            distances.append(zombie_distance_field[cell[0]][cell[1]])
            
            # find maximum distance all zombies
            max_distance = max(distances)
            
            best_moves = []
            # keep track of all possible moves that maximize distance to all zombies
            for idx in range(len(distances)):
                if distances[idx] == max_distance:
                    best_moves.append(neighbors[idx])
            
            # choose best move randomly
            new_list.append(best_moves[random.randrange(0, len(best_moves))])
            
        self._human_list = new_list
            
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_list = []
        # move each zombie in zombie_list
        for cell in self.zombies():
            distances = []
            neighbors = self.four_neighbors(cell[0], cell[1])
            
            # for each neighbor cell, check distance to nearest human
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]):
                    distances.append(human_distance_field[neighbor[0]][neighbor[1]])
                else:
                    distances.append(float('inf'))
            
            # for the current cell, check distance to nearest human
            neighbors.append(cell)
            distances.append(human_distance_field[cell[0]][cell[1]])
            
            # find minimum distance to all humans
            min_distance = min(distances)
            
            best_moves = []
            
            # keep track of all possible moves that minimize distance to a human
            for idx in range(len(distances)):
                if distances[idx] == min_distance:
                    best_moves.append(neighbors[idx])
            
            # choose best move randomly
            new_list.append(best_moves[random.randrange(0, len(best_moves))])
            
        self._zombie_list = new_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))

#a = Apocalypse(5, 5, [(2, 2)], [(0, 1)], [(3, 3)]) # obstacle_list, zombie_list, human_list
#
#for row in a.compute_distance_field(ZOMBIE):
#    print row

def test_move_humans():
    """
    test move_humans() method
    """
    
    obj = Apocalypse(5, 5, [(2, 2)], [(0, 1)], [(3, 3)]) # obstacle_list, zombie_list, human_list

    for row in obj.compute_distance_field(ZOMBIE):
        print row
    
    print "before move:"
    for human in obj.humans():
        print human
        
    obj.move_humans(obj.compute_distance_field(ZOMBIE))
    
    print "after move:"
    for human in obj.humans():
        print human
        
def test_move_zombies():
    """
    test move_zombies() method
    """
    
    obj = Apocalypse(5, 5, [(2, 2)], [(0, 1)], [(3, 3)]) # obstacle_list, zombie_list, human_list

    for row in obj.compute_distance_field(HUMAN):
        print row
    
    print "before move:"
    for zombie in obj.zombies():
        print zombie
        
    obj.move_zombies(obj.compute_distance_field(HUMAN))
    
    print "after move:"
    for zombie in obj.zombies():
        print zombie
        
#test_move_humans()
#test_move_zombies()