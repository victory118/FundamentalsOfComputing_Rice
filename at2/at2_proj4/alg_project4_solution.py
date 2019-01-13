"""
For Project 4, student will implement five functions:

build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)

"""

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Takes as input a set of characters alphabet and three scores diag_score, 
    off_diag_score, and dash_score. The function returns a dictionary of 
    dictionaries whose entries are indexed by pairs of characters in alphabet 
    plus '-'. The score for any entry indexed by one or more dashes is dash_score. 
    The score for the remaining diagonal entries is diag_score. Finally, 
    the score for the remaining o -diagonal entries is off_diag_score.
    """
    char_list = list(alphabet) + ['-']
    score_dict = {}

    for char1 in char_list:
        score_dict[char1] = {}
        for char2 in char_list:
            if char1 == '-' or char2 == '-':
                score_dict[char1][char2] = dash_score
            elif char1 == char2:
                score_dict[char1][char2] = diag_score
            else:
                score_dict[char1][char2] = off_diag_score
    
    return score_dict


def build_scoring_matrix_test():
    """
    Unit tests for build_scoring_matrix function
    """
    alphabet = set(['A', 'C', 'G', 'T'])
    diag_score = 5
    off_diag_score = 2
    dash_score = -4
    score_dict = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)

    return score_dict

# score_dict = build_scoring_matrix_test()
# print(score_dict)

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a 
    common alphabet with the scoring matrix scoring_matrix. The function 
    computes and returns the alignment matrix for seq_x and seq_y as 
    described in the Homework. If global_flag is True , each entry of the 
    alignment matrix is computed using the method described in Question 8 
    of the Homework. If global_flag is False , each entry is computed 
    using the method described in Question 12 of the Homework.

    Output: alignment_matrix[row][col] is a list of lists
    """
    # Commented for pylint
    # m = len(seq_x)
    # n = len(seq_y)

    alignment_matrix = [(len(seq_y)+1)*[0] for _ in range(len(seq_x)+1)]

    for idx in range(1,len(seq_x)+1):
        alignment_matrix[idx][0] = alignment_matrix[idx-1][0] + scoring_matrix[seq_x[idx-1]]['-']
        if global_flag is False and alignment_matrix[idx][0] < 0:
            alignment_matrix[idx][0] = 0
    
    for idx in range(1,len(seq_y)+1):
        alignment_matrix[0][idx] = alignment_matrix[0][idx-1] + scoring_matrix['-'][seq_y[idx-1]]
        if global_flag is False and alignment_matrix[0][idx] < 0:
            alignment_matrix[0][idx] = 0

    for idx_i in range(1,len(seq_x)+1):
        for idx_j in range(1,len(seq_y)+1):

            opt1 = alignment_matrix[idx_i-1][idx_j-1] + scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]
            opt2 = alignment_matrix[idx_i-1][idx_j] + scoring_matrix[seq_x[idx_i-1]]['-']
            opt3 = alignment_matrix[idx_i][idx_j-1] + scoring_matrix['-'][seq_y[idx_j-1]]

            alignment_matrix[idx_i][idx_j] = max(opt1, opt2, opt3)

            if global_flag is False and alignment_matrix[idx_i][idx_j] < 0:
                alignment_matrix[idx_i][idx_j] = 0
    
    return alignment_matrix

def compute_alignment_matrix_test():
    """
    Run unit tests for compute_alignment_matrix function
    """
    seq_x = 'AC'
    seq_y = 'TAG'

    alphabet = set(seq_x + seq_y)
    diag_score = 5
    off_diag_score = 2
    dash_score = -4
    scoring_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
    global_flag = True
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)

    return alignment_matrix

# alignment_matrix = compute_alignment_matrix_test()
# print(alignment_matrix)

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common 
    alphabet with the scoring matrix scoring_matrix. This function computes a 
    global alignment of seq_x and seq_y using the global alignment matrix 
    alignment_matrix. The function returns a tuple of the form (score, align_x, align_y) 
    where score is the score of the global alignment align_x and align_y. Note 
    that align_x and align_y should have the same length and may include the 
    padding character '-'.
    """

    idx_i = len(seq_x)
    idx_j = len(seq_y)

    align_x = ''
    align_y = ''

    score = alignment_matrix[idx_i][idx_j]

    while idx_i != 0 and idx_j != 0:
        if alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j-1] + scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]:
            align_x = seq_x[idx_i-1] + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_i -= 1
            idx_j -= 1
        elif alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j] + scoring_matrix[seq_x[idx_i-1]]['-']:
            align_x = seq_x[idx_i-1] + align_x
            align_y = '-' + align_y
            idx_i -= 1
        else:
            align_x = '-' + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_j -= 1

    while idx_i != 0:
        align_x = seq_x[idx_i-1] + align_x
        align_y = '-' + align_y
        idx_i -= 1
    
    while idx_j != 0:
        align_x = '-' + align_x
        align_y = seq_y[idx_j-1] + align_y
        idx_j -= 1
    
    return score, align_x, align_y

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common 
    alphabet with the scoring matrix scoring_matrix. This function computes a 
    global alignment of seq_x and seq_y using the global alignment matrix 
    alignment_matrix. The function returns a tuple of the form (score, align_x, align_y) 
    where score is the score of the global alignment align_x and align_y. Note 
    that align_x and align_y should have the same length and may include the 
    padding character '-'.
    """

    # iterate over rows to find max value and row/col index
    max_score = 0
    idx_i = len(seq_x) # store row index of max value
    idx_j = len(seq_y) # store column index of max value

    for row_idx, row in enumerate(alignment_matrix):
        row_max = max(row)
        if row_max >= max_score:
            max_score = row_max
            idx_i = row_idx
            idx_j = row.index(row_max)

    align_x = ''
    align_y = ''

    score = max_score

    # remember to exit while loop when alignment_matrix value is 0
    while idx_i != 0 and idx_j != 0 and alignment_matrix[idx_i][idx_j] != 0:
        if alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j-1] + scoring_matrix[seq_x[idx_i-1]][seq_y[idx_j-1]]:
            align_x = seq_x[idx_i-1] + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_i -= 1
            idx_j -= 1
        elif alignment_matrix[idx_i][idx_j] == alignment_matrix[idx_i-1][idx_j] + scoring_matrix[seq_x[idx_i-1]]['-']:
            align_x = seq_x[idx_i-1] + align_x
            align_y = '-' + align_y
            idx_i -= 1
        else:
            align_x = '-' + align_x
            align_y = seq_y[idx_j-1] + align_y
            idx_j -= 1

    # while idx_i != 0:
    #     align_x = seq_x[idx_i-1] + align_x
    #     align_y = '-' + align_y
    #     idx_i -= 1
    
    # while idx_j != 0:
    #     align_x = '-' + align_x
    #     align_y = seq_y[idx_j-1] + align_y
    #     idx_j -= 1
    
    return score, align_x, align_y

def compute_local_alignment_test():
    """
    Run unit tests for compute_local_alignment function
    """
    # seq_x = 'AA'
    # seq_y = 'TAAT'
    # alphabet = set(seq_x + seq_y)
    # diag_score = 10
    # off_diag_score = 4
    # dash_score = -6

    seq_x = 'happypedestrianwalker'
    seq_y = 'sadpedesxtriandriver'
    alphabet = set(seq_x + seq_y)
    diag_score = 1
    off_diag_score = -1
    dash_score = -1

    scoring_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
    global_flag = False
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)
    # print(alignment_matrix)
    score, align_x, align_y = compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)

    return score, align_x, align_y

# score, align_x, align_y = compute_local_alignment_test()
# print("score = ", score)
# print("align_x = ", align_x)
# print("align_y = ", align_y)