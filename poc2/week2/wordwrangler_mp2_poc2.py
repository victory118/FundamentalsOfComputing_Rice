"""
Student code for Word Wrangler game
"""

# codeskulptor link: http://www.codeskulptor.org/#user45_n3dnx2EwBcxzCnr_12.py

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"
#WORDFILE = "http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    
    if list1 == []:
        return list1
    
    new_list = [list1[0]];
    prev_elem = list1[0];
    
    for elem in list1:
        if elem != prev_elem:
            new_list.append(elem)
            prev_elem = elem
            
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    
    idx1 = 0
    idx2 = 0
    
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            idx1 += 1
        elif list1[idx1] > list2[idx2]:
            idx2 += 1
        else:
            new_list.append(list1[idx1])
            idx1 += 1
            idx2 += 1
    
    # slow implementation
#    for item in list1:
#        if item in list2:
#            new_list.append(item)
            
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    new_list1 = list(list1)
#    new_list2 = list(list2)
    
    idx = 0
       
    for item in list2:
        
        while True:
            if item <= new_list1[idx]:
                new_list1.insert(idx, item)
                idx += 1
                break
            elif item > new_list1[idx] and idx == len(new_list1) - 1:
                new_list1.append(item)
                idx += 1
                break
            else:
                idx += 1
            
    return new_list1
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list(list1)
        
    return merge(merge_sort(list1[:len(list1)/2]), merge_sort(list1[len(list1)/2:])) 

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    
#    print "word = ", word
    
    if word == '':
        return ['']
    elif len(word) == 1:
        return ['', word] 
    
    first = word[0]
    rest = word[1:]

    rest_strings = gen_all_strings(rest)
#    print "first = ", first
#    print "rest_strings (gen) = ", rest_strings
    
    new_strings = []
    for item in rest_strings:
        for idx in range(len(item)+1):
#            print "item = ", item
#            print "idx = ", idx
            str_list = list(item)
#            print "str_list = ", str_list
#            print "first = ", first
            str_list.insert(idx, first)
#            print "str_list = ", str_list
            new_str = ''.join(str_list)
#            print "new_str", new_str
            new_strings.append(new_str)

#    print "new_strings = ", new_strings
    return rest_strings + new_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    word_list = []
    
    for line in netfile.readlines():
        word_list.append(line.strip('\n'))
#    print word_list
    return word_list

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)
    
def test_remove_duplicates():
    """
    test remove_duplicates()
    """
    
    print remove_duplicates([0, 0, 0])
    print remove_duplicates([0, 1, 1, 2, 3, 3, 3])
    
def test_intersect():
    """
    test intersect()
    """
    
    print intersect([0, 1, 2], [1, 2, 4])
    print intersect([0, 1, 2], [3, 4, 6])
    
def test_merge():
    """
    test merge(list1, list2)
    """
    
    print merge([0, 2, 4, 100], [1, 3, 4, 5])
    
def test_merge_sort():
    """
    test merge_sort(list1)
    """
    
    print merge_sort([5, 4, 8, 10, 8, 3])

def test_gen_all_strings():
    """
    test gen_all_strings(word)
    """
    
    print gen_all_strings('ab')
    print gen_all_strings('aab')
    
# Uncomment when you are ready to try the game
run()
#test_remove_duplicates()
#test_intersect()
#test_merge()
#test_merge_sort()
#test_gen_all_strings()

#item = 'b'
#idx = 0
#str_list = list(item.partition(item[:idx+1]))
#print str_list
#print len('')

#item = 'b'
#print item[0:0]
#
#item = 'test'
#print list(item)
#
#print list([''])

#item = 'test'
#lst = list(item)
#lst.insert(3, 't')
#print lst