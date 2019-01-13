"""
Merge function for 2048 game.
"""
# codeskulptor url: http://www.codeskulptor.org/#user45_WQcUGDZebimj16c.py
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
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

import poc_merge2048_mp1_testsuite
poc_merge2048_mp1_testsuite.run_suite(merge)

# print(merge([2, 0, 2, 4]))
# print(merge([0, 0, 2, 2]))
# print(merge([2, 2, 0, 0]))
# print(merge([2, 2, 2, 2, 2]))
# print(merge([8, 16, 16, 8]))

# Tests:
# [2, 0, 2, 4] should return [4, 4, 0, 0]
# [0, 0, 2, 2] should return [4, 0, 0, 0]
# [2, 2, 0, 0] should return [4, 0, 0, 0]
# [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0]
# [8, 16, 16, 8] should return [8, 32, 8, 0]