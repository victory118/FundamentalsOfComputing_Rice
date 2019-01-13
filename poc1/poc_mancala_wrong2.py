"""
wrong implementation of plan_moves()
"""

class SolitaireMancala:

    def __init__(self):
        self.configuration = [0]

    def set_board(self, configuration):
        self.configuration = configuration[0:len(configuration)]

    def __str__(self):
        return str(self.configuration[::(-1)])

    def get_num_seeds(self, house_num):
        return self.configuration[house_num]

    def is_game_won(self):
        if (sum(self.configuration[1:]) == 0):
            return True
        else:
            return False

    def is_legal_move(self, house_num):
        if ((self.configuration[house_num] == len(self.configuration[:house_num])) and (house_num != 0)):
            return True
        else:
            return False

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for i in range(0, house_num):
                self.configuration[i] += 1
            self.configuration[house_num] = 0

    def choose_move(self):
        for i in range(1, len(self.configuration)):
            if self.is_legal_move(i):
                return i
        return 0

    def plan_moves(self):
        plan = []
        while (not self.is_game_won()):
            if (self.choose_move() > 0):
                print self.choose_move()
                plan.append(self.choose_move())
                print plan
                self.apply_move(self.choose_move())
                print str(self)
            else:
                return []
        return plan