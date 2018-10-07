"""
wrong implementation of plan_moves()
"""

class SolitaireMancala:

    def __init__(self):
        self.game_board = [0]

    def set_board(self, configuration):
        self.game_board = configuration[::]

    def __str__(self):
        game_board = self.game_board[::]
        game_board.reverse()
        return str(game_board)

    def get_num_seeds(self, house_num):
        return self.game_board[house_num]

    def is_game_won(self):
        if (self.game_board[1:].count(0) == len(self.game_board[1:])):
            return True
        return False

    def is_legal_move(self, house_num):
        if (house_num == 0):
            return False
        elif (self.game_board[house_num] == house_num):
            return True
        return False

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            self.game_board[house_num] = 0
            for num in range(house_num):
                self.game_board[num] += 1

    def choose_move(self):
        for num in self.game_board[1:]:
            if (self.game_board.index(num, 1) == num):
                return num
        return 0

    def plan_moves(self):
        ret = []
        while (not self.is_game_won()):
            check_num = self.choose_move()
            if (check_num != 0):
                ret.append(check_num)
            if (check_num == 0):
                break
            self.apply_move(check_num)
        return ret