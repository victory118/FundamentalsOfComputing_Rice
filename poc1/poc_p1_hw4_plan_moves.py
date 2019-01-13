import poc_mancala_student
import poc_mancala_wrong1
import poc_mancala_wrong2
import poc_mancala_wrong3
import poc_mancala_wrong4
import poc_mancala_wrong5

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

TEST_CASES = [[0, 0, 1, 1, 3, 5, 0], \
                [0, 2], \
                [0, 1, 6], \
                [0, 2, 2], \
                [0, 3, 2, 3], \
                [0, 1, 2, 3, 3, 5]] # successfully passed
# grade code:2004349
#print TEST_CASES
game_ref = poc_mancala_student.SolitaireMancala()
game = poc_mancala_wrong5.SolitaireMancala()

ok = True

for seq_len in range(1, 10):
    for seq in gen_all_sequences(range(0, 11), seq_len):
        # print seq
        configuration = [0]
        configuration.extend(list(seq))
        game.set_board(configuration)
        other_list = game.plan_moves()
        game_ref.set_board(configuration)
        move_list = game_ref.plan_moves()
        try:
            assert move_list == other_list
        except AssertionError:
            print "test = ", configuration, ", out = ", other_list, ", expected = ", move_list
            ok = False
            break
    if not ok:
        break

# try:
#     assert 1 == 0
# except AssertionError:
#     print "not equal"