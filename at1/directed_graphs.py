"""
Algorithmic Thinking 1
Week 2 Homework
"""

# Example graphs

EX_GRAPH0 = {0:set([1,2]), 
             1:set([]),
             2:set([])}

EX_GRAPH1 = {0:set([1,4,5]), 
             1:set([2,6]),
             2:set([3]),
             3:set([0]),
             4:set([1]),
             5:set([2]),
             6:set([])}

EX_GRAPH2 = {0:set([1,4,5]), 
             1:set([2,6]),
             2:set([3,7]),
             3:set([7]),
             4:set([1]),
             5:set([2]),
             6:set([]),
             7:set([3]),
             8:set([1,2]),
             9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """Takes number of nodes and returns a dictionary corresponding to
    a complete directed graph with the specified number of nodes.

    A complete graph contains all possible edges subject to the restriction
    that self-loops are not allowed. The nodes of the graph should be 
    numbered 0 to num_nodes-1 when num_nodes is positive. Otherwise, 
    the function returns a dictionary corresponding to the empty graph.
    """

    digraph = {}
    for idx1 in range(num_nodes):
        digraph[idx1] = set([])
        for idx2 in range(num_nodes):
            if idx2 != idx1:
                digraph[idx1].add(idx2)
    
    return digraph

def make_complete_graph_test():
    """
    Unit tests for the make_complete_graph function
    """
    digraph1 = make_complete_graph(2)
    # print digraph1
    assert digraph1 == {0:set([1]),
                        1:set([0])}

# make_complete_graph_test()

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and
    computes the in-degrees for the nodes in the graph. The function
    should return a dictionary with the same set of keys (nodes) as
    digraph whose corresponding values are the number of edges whose
    head matches a particular node.
    """

    in_degrees = {}

    for key in digraph:
        in_degrees[key] = 0

    for _, heads in digraph.items():
        for head in heads:
            in_degrees[head] += 1

    return in_degrees

def compute_in_degrees_test():
    """
    Unit tests for the compute_in_degrees function
    """

    in_degrees0 = compute_in_degrees(EX_GRAPH0)
    # print in_degrees0
    assert in_degrees0 == {0:0,
                           1:1,
                           2:1}

    in_degrees1 = compute_in_degrees(EX_GRAPH1)
    # print in_degrees1
    assert in_degrees1 == {0:1,
                           1:2,
                           2:2,
                           3:1,
                           4:1,
                           5:1,
                           6:1}
    in_degrees2 = compute_in_degrees(EX_GRAPH2)
    # print in_degrees2
    assert in_degrees2 == {0:1,
                           1:3,
                           2:3,
                           3:3,
                           4:2,
                           5:2,
                           6:2,
                           7:3,
                           8:0,
                           9:0}

# compute_in_degrees_test()

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes
    the unnormalized distribution of the in-degrees of the graph. The function
    should return a dictionary whose keys correspond to the in-degrees of nodes
    in the graph. The value associated with each particular in-degree is the 
    number of nodes with that in-degree. In-degrees with no corresponding
    nodes in the graph are not included in the dictionary.
    """

    in_degrees = compute_in_degrees(digraph)
    in_degree_dist= {}

    for _, val in in_degrees.items():
        if val not in in_degree_dist:
            in_degree_dist[val] = 1
        else:
            in_degree_dist[val] += 1

    return in_degree_dist

def in_degree_distribution_test():
    """
    Unit tests for in_degree_distribution function
    """
    in_degree_dist0 = in_degree_distribution(EX_GRAPH0)
    # print in_degree_dist0
    assert in_degree_dist0 == {0:1,
                               1:2}
    in_degree_dist1 = in_degree_distribution(EX_GRAPH1)
    # print in_degree_dist1
    assert in_degree_dist1 == {1:5,
                               2:2}
    in_degree_dist2 = in_degree_distribution(EX_GRAPH2)
    # print in_degree_dist2
    assert in_degree_dist2 == {0:2,
                               1:1,
                               2:3,
                               3:4}

# in_degree_distribution_test()