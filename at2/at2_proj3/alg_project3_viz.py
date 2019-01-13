"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import random
import urllib2
import alg_cluster
import time
import pickle

# conditional imports
if DESKTOP:
    import alg_project3_solution      # desktop project solution
    import alg_clusters_matplotlib
else:
    #import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
    import alg_clusters_simplegui
    import codeskulptor
    codeskulptor.set_timeout(30)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering
    
    Note that method may return num_clusters or num_clusters + 1 final clusters
    """
    
    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters)  / num_clusters
    
    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)
            
    return cluster_list
                

#####################################################################
# Code to load cancer data, compute a clustering and 
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    # data_table = load_data_table(DATA_3108_URL)
    # data_table = load_data_table(DATA_111_URL)
    # data_table = load_data_table(DATA_290_URL)
    data_table = load_data_table(DATA_896_URL)
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    start = time.time()     
    # cluster_list = sequential_clustering(singleton_list, 15)	
    # print "Displaying", len(cluster_list), "sequential clusters"

    # cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list[:4], 1)
    # cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 9)
    # print "Displaying", len(cluster_list), "hierarchical clusters"

    cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 3)
    print "Displaying", len(cluster_list), "k-means clusters"

    # batch hierarchical clustering
    # batch_hierarchical_clustering(singleton_list, data_table, "hc_distortion_111.pickle")
    # batch_hierarchical_clustering(singleton_list, data_table, "hc_distortion_290.pickle")
    # batch_hierarchical_clustering(singleton_list, data_table, "hc_distortion_896.pickle")

    # batch kmeans clustering
    # batch_kmeans_clustering(singleton_list, data_table, "kmeans_distortion_111.pickle")
    # batch_kmeans_clustering(singleton_list, data_table, "kmeans_distortion_290.pickle")
    batch_kmeans_clustering(singleton_list, data_table, "kmeans_distortion_896.pickle")

    end = time.time()
    run_time = end - start
    print("run_time = ", run_time)

    # calculate the distortion
    if True:
        distortion = compute_distortion(cluster_list, data_table)
        print("distortion = ", distortion)
            
    # draw the clusters using matplotlib or simplegui
    if DESKTOP:
        # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
        alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    else:
        alg_clusters_simplegui.PlotClusters(data_table, cluster_list)   # use toggle in GUI to add cluster centers

def compute_distortion(cluster_list, data_table):
    """
    Takes a list of clusters and uses cluster_error to compute its distortion.
    """
    distortion = 0.0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)

    return distortion

def batch_hierarchical_clustering(singleton_list, data_table, out_name):
    # pickle_out = open("hc_distortion_111.pickle","wb")
    # pickle_out = open("hc_distortion_290.pickle","wb")
    # pickle_out = open("hc_distortion_896.pickle","wb")
    pickle_out = open(out_name,"wb")
    output_clusters = range(20,5,-1)
    hc_distortion = [0 for _ in range(len(output_clusters))]

    for idx, num_cluster in enumerate(output_clusters):
        if num_cluster == 20:
            cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, num_cluster)
        else:
            cluster_list = alg_project3_solution.hierarchical_clustering(cluster_list, num_cluster)

        # calculate the distortion
        hc_distortion[idx] = compute_distortion(cluster_list, data_table)

    hc_dict = {'distortion':hc_distortion, 'output_clusters':output_clusters}
    pickle.dump(hc_dict, pickle_out)
    pickle_out.close()

def batch_kmeans_clustering(singleton_list, data_table, out_name):
    # pickle_out = open("kmeans_distortion_111.pickle","wb")
    # pickle_out = open("kmeans_distortion_290.pickle","wb")
    # pickle_out = open("kmeans_distortion_896.pickle","wb")
    pickle_out = open(out_name,"wb")
    output_clusters = range(20,5,-1)
    kmeans_distortion = [0 for _ in range(len(output_clusters))]

    num_iter = 5
    for idx, num_cluster in enumerate(output_clusters):
        cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, num_cluster, num_iter)

        # calculate the distortion
        kmeans_distortion[idx] = compute_distortion(cluster_list, data_table)

    kmeans_dict = {'distortion':kmeans_distortion, 'output_clusters':output_clusters}
    pickle.dump(kmeans_dict, pickle_out)
    pickle_out.close()

run_example()