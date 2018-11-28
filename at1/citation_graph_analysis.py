"""
Application #1 - Analysis of Citation Graphs

Algorithmic Thinking 1
"""

# Question 1
# 1. Compute the in-degree distribution for this citation grpah.
# 2. Normalize the distribution.
# 3. Compuate a log/log plot of the points in this normalized distribution

# Download data and save locally as pickle file if first time running

if False:
    import alg_load_graph

    # print alg_load_graph.CITATION_URL
    citation_graph = alg_load_graph.load_graph(alg_load_graph.CITATION_URL)

    import pickle

    pickle_out = open("citation_graph.pickle","wb")
    pickle.dump(citation_graph, pickle_out)
    pickle_out.close()

# Load the citation graph dictionary from pickle file
import pickle
pickle_in = open("citation_graph.pickle","rb")
citation_graph = pickle.load(pickle_in)