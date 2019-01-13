"""
Bread-first search Project #2
Algorithmic Thinking (Part 1)
"""

from collections import deque
import alg_module2_graphs

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node
    and returns the set consisting of all nodes that are visited
    by a breadth-first search that starts at start_node.
    """

    # Initialize Q to an empty queue
    node_queue = deque()

    visited = set([start_node])
    node_queue.append(start_node)

    while len(node_queue) > 0:
        current_node = node_queue.popleft()

        for neighbor in ugraph[current_node]:
            if neighbor not in visited:
                visited = visited.union(set([neighbor]))
                node_queue.append(neighbor)
        
    return visited

# assert(bfs_visited(alg_module2_graphs.GRAPH0, 0) == set([0, 1, 2, 3]))
# assert(bfs_visited(alg_module2_graphs.GRAPH1, 0) == set([0, 1, 2, 3, 4]))
#assert(bfs_visited(alg_module2_graphs.GRAPH2, 0) == set([0, 1, 2, 3, 4]))
# print(bfs_visited(alg_module2_graphs.GRAPH0, 0))

def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, 
    where each set consists of all the nodes (and nothing else)
    in a connected component, and there is exactly one set in the 
    list for each connected component in ugraph and nothing else.
    """

    remaining_nodes = set(ugraph.keys())
    conn_comp_set = set()

    while len(remaining_nodes) > 0:
        current_node = remaining_nodes.pop()
        conn_comp = bfs_visited(ugraph, current_node)
        # print(cc)
        conn_comp_set.add(frozenset(conn_comp))
        # print(remaining_nodes)
        remaining_nodes.difference_update(conn_comp)
        # print(remaining_nodes)
    
    # print(cc_set)
    # print(list(cc_set))
    conn_comp_set = map(set,list(conn_comp_set))
    # print(cc_set)
    # print(list(map(set(),list(cc_set)))
    return conn_comp_set

# print(cc_visited(alg_module2_graphs.GRAPH0))

def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer)
    of the largest connected component in ugraph.
    """

    if len(ugraph) == 0:
        return 0

    conn_comp_set = cc_visited(ugraph)

    comp_lens = map(len, conn_comp_set)

    return max(comp_lens)

# print(largest_cc_size(alg_module2_graphs.GRAPH0))

def compute_resilience(u_graph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and
    iterates through the nodes in attack_order. For each node in the list,
    the function removes the given node and its edges from the graph and
    then computes the size of the largest connected component for the
    resulting graph. The function should return a list whose k+1th entry
    is the size of the largest connected component in the graph after the
    removal of the first k nodes in attack_order. The first entry (indexed by zero)
    is the size of the largest connected component in the original graph.
    """

    largest_cc_lst = [largest_cc_size(u_graph)]

    # make deep copy of u_graph
    u_graph2 = {}
    for key, val in u_graph.items():
        u_graph2[key] = set(val)

    for node in attack_order:
        # save all of node's neighbors in a list
        neighbor_lst = list(u_graph2[node])
        # remove node in attack_order if it exists
        u_graph2.pop(node)
        
        # remove edges from graph
        for neighbor in neighbor_lst:
            u_graph2[neighbor].discard(node)

        # print(u_graph2)
        largest_cc_lst.append(largest_cc_size(u_graph2))
        # print(largest_cc_lst)

    return largest_cc_lst

# print(compute_resilience(alg_module2_graphs.GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])) # expected [8, 7, 6, 5, 1, 1, 1, 1, 0]
# print(compute_resilience(alg_module2_graphs.GRAPH0, [1]))





