from merge2048 import merge

from poc_p1_hw4_plan_moves import gen_all_sequences

# def gen_all_sequences(outcomes, length)
suite.run_test(fun([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1: ")
    suite.run_test(fun([0, 0, 2, 2]), [4, 0, 0, 0], "Test #2: ")
    suite.run_test(fun([2, 2, 0, 0]), [4, 0, 0, 0], "Test #3: ")
    suite.run_test(fun([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0], "Test #4: ")
    suite.run_test(fun([8, 16, 16, 8]), [8, 32, 8, 0], "Test #5: ")

TEST_CASES = [[2, 0, 2, 4], \
                [0, 0, 2, 2], \
                [2, 2, 0, 0], \
                [2, 2, 2, 2, 2], \
                [8, 16, 16, 8]] # successfully passed
                # grade code: 0634386