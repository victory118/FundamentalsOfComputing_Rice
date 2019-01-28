"""
Fundamentals of Computing
Capstone Exam
Question 17
"""

def pick_a_number(board):
    """
    Recursive function that chooses from 
    beginning or end of list to maximize score
    """

    best_score1 = 0
    best_score2 = 0

    if len(board) == 2:
        return max(board), min(board)
    else:
        
        if len(board) % 2 == 0:
            for idx in [0, -1]:
                board_copy = list(board)
                add_score = board_copy.pop(idx)
                score1, score2 = pick_a_number(board_copy)

                if add_score + score1 >= best_score1:
                    best_score1 = score1 + add_score
                    best_score2 = score2
        else:
            for idx in [0, -1]:
                board_copy = list(board)
                add_score = board_copy.pop(idx)
                score1, score2 = pick_a_number(board_copy)

                if add_score + score2 >= best_score2:
                    best_score2 = score2 + add_score
                    best_score1 = score1

    return best_score1, best_score2

print pick_a_number([3, 5, 2, 1])
print pick_a_number([1, 2, 5, 3])
# arr = [12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
arr = [12, 9, 7, 3, 4, 7, 4, 7, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
pick_a_number(arr)
print pick_a_number(arr)
print pick_a_number(list(reversed(arr)))
print(sum(arr))