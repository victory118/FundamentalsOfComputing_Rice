"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# codeskulptor link: http://www.codeskulptor.org/#user45_UmaIj91t93_21.py

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

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


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    max_score = 0
    for num in set(hand):
        score_val = num*hand.count(num)
        if score_val > max_score:
            max_score = score_val
        
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    # Tests
    # held dice = (1,)
    # num_free_dice = 1
    # num_die_sides = 2
    # possible_hands = (1, 1), (1, 2)
    # expected_value = (score((1,1)) + score((1,2)))/len(possible_hands)
    possible_rolls = list(gen_all_sequences(range(1, num_die_sides +1), num_free_dice))
#    print "possible rolls: ", possible_rolls
    score_sum = 0
#    for hand in possible_hands
    for roll in possible_rolls:
#        print "roll: ", roll
#        print list(roll)
#        print "held dice: ", list(held_dice)
        hand = list(held_dice)
        hand.extend(list(roll))
#        print "hand: ", hand
#        print "score(hand) = ", score(hand)
        score_sum += score(hand)
#    print "score_sum = ", score_sum
#    print "len(possible_rolls) = ", len(possible_rolls)
    return float(score_sum)/len(possible_rolls)
#        print hand
#    return 0.0


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    possible_hands = []
    for mask in gen_all_sequences([0, 1], len(hand)):
        temp_hand = [list(hand)[idx] for idx in \
                     range(len(hand)) if list(mask)[idx]]
        possible_hands.append(tuple(temp_hand))
#        print mask
#        print temp_hand
#    print possible_hands
#    print set(possible_hands)
            
    return set(possible_hands)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    max_exp_score = 0
    best_hold = hand
    
    for held_dice in all_holds:
#        print held_dice
        num_free_dice = len(hand) - len(held_dice)
        exp_score = expected_value(held_dice, num_die_sides, num_free_dice)
        if exp_score > max_exp_score:
            best_hold = held_dice
            max_exp_score = exp_score
    return (max_exp_score, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

# Tests for score(hand) function
assert score((1, 1, 1, 5, 6)) == 6
assert score((2, 4, 4, 5, 6)) == 8
assert score((3, 3, 3, 4, 6)) == 9

#outcomes = [0,1]
#length = 3
#print gen_all_sequences(outcomes, length)
#print gen_all_holds((1, 1, 2))

# Tests for expected_value(held_dice, num_die_sides, num_free_dice)
assert expected_value(tuple([1]), 2, 1) == 2
assert expected_value(tuple([]), 2, 1) == 1.5 

# Tests for strategy(hand, num_die_sides)
#print strategy(tuple([2, 2]), 2)
#print strategy(tuple([1, 2]), 2)
#print strategy(tuple([1, 1]), 2)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

# combination: order doesn't matter
# permutation: order matters (no reptitions)
                                       
    
    
    



