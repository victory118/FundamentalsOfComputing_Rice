"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster

import random
# from copy import deepcopy


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    (min_dist, min_idx1, min_idx2) = (float('inf'), -1, -1)
    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                (dist,_,_) = pair_distance(cluster_list, idx1, idx2)
                if dist < min_dist:
                    (min_dist, min_idx1, min_idx2) = (dist, idx1, idx2)
    
    return (min_dist, min_idx1, min_idx2)



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    # number of clusters
    n_clusters = len(cluster_list)

    if n_clusters <= 3:
        dist_tup = slow_closest_pair(cluster_list)
    else:
        mid = int(n_clusters/2) # take the floor of result
        # partition cluster_list into two halves
        left_clusters = list(cluster_list[:mid])
        right_clusters = list(cluster_list[mid:n_clusters])

        # print("left_clusters = ", left_clusters)
        # print("right_clusters = ", right_clusters)

        # call fast_closest_pair recursively on each half of list
        left_dist_tup = fast_closest_pair(left_clusters)
        right_dist_tup = fast_closest_pair(right_clusters)

        # slow_right_dist = slow_closest_pair(right_clusters)

        # print("left_dist_tup = ", left_dist_tup)
        # print("right_dist_tup =", right_dist_tup)
        # print("slow_right_dist = ", slow_right_dist)

        # find the closest pair from the previous recursive call
        if left_dist_tup[0] <= right_dist_tup[0]:
            dist_tup = left_dist_tup
        else:
            dist_tup = (right_dist_tup[0], right_dist_tup[1] + mid, right_dist_tup[2] + mid)
        
        # print("dist_tup = ", dist_tup)

        # calculate mid-point of x_mid and x_{mid-1} (center of strip)
        x_mid = 0.5*(cluster_list[mid].horiz_center() + cluster_list[mid-1].horiz_center())
        # print("x_mid = ", x_mid)

        # find minimum among left and right halves and inside strip
        strip_dist_tup = closest_pair_strip(cluster_list, x_mid, dist_tup[0])

        # print("strip_dist_tup = ", strip_dist_tup)

        if strip_dist_tup[0] < dist_tup[0]:
            dist_tup = strip_dist_tup
        # print("dist_tup = ", dist_tup)

    return dist_tup


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """

    # closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), 
    # alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 1.5, 1.0)
    # expected one of the tuples in set([(1.0, 1, 2)]) but received (1.0, 0, 1)

    # filter cluster_list such that {i:abs(x_i-horiz_center) < half_width}
    strip_idx_list = [idx for idx in range(len(cluster_list)) 
                    if abs(cluster_list[idx].horiz_center()-horiz_center) < half_width]
    # strip_list = list(filter(lambda x: abs(x.horiz_center()-horiz_center) < half_width, cluster_list))
    # print(strip_idx_list)

    # sort the indices in strip_idx non-decreasing order of the vertical (y) coordinates of associated points
    strip_idx_list.sort(key = lambda idx: cluster_list[idx].vert_center())

    # print("strip_idx_list = ", strip_idx_list)

    strip_cluster_list = [cluster_list[idx] for idx in strip_idx_list]
    # print("strip_cluster_list = ", strip_cluster_list)
    
    # number of clusters in strip_
    num_strip = len(strip_idx_list)

    (min_dist, min_idx1, min_idx2) = (float('inf'), -1, -1)

    for idx1 in range(num_strip-1):
        for idx2 in range(idx1+1, min(idx1+4,num_strip)):
            (dist,_,_) = pair_distance(strip_cluster_list, idx1, idx2)
            # print("dist = ", dist)
            # print("idx1 = ", idx1)
            # print("idx2 = ", idx2)
            if dist < min_dist:
                # print("min_dist = ", dist)
                # print("min_idx1 = ", strip_idx_list[idx1])
                # print("min_idx2 = ", strip_idx_list[idx2])
                (min_dist, min_idx1, min_idx2) = (dist, strip_idx_list[idx1], strip_idx_list[idx2])
    if min_idx1 > min_idx2:
        return (min_dist, min_idx2, min_idx1)

    return (min_dist, min_idx1, min_idx2)
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    while len(cluster_list) > num_clusters:

        # sort cluster_list in nondecreasing order of their horizontal x-coordinates
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())

        # find two clusters in the list whose distance is the smallest
        (_, idx1, idx2) = fast_closest_pair(cluster_list) # input must be sorted!
        # print("idx1 = ", idx1)
        # print("idx2 = ", idx2)
        # merge two clusters together
        # print("before merge = ", cluster_list)
        cluster_list[idx1].merge_clusters(cluster_list[idx2]) # mutates idx1 cluster in place
        # print("merged_cluster = ", new_cluster)
        # print("after merge = ", cluster_list)
        # append merged cluster to cluster_list (no need)
        # remove individual clusters that were merged from cluster_list
        cluster_list.pop(idx2)
        # print ("after pop", cluster_list)

    return cluster_list


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    num_pts = len(cluster_list)

    # make a deep copy of the cluster_list because we may not mutate it
    cl_copy = [cluster_list[idx].copy() for idx in range(num_pts)]
    # cluster_list_copy = deepcopy(cluster_list)

    # position initial clusters at the location of clusters with largest populations
    cl_copy.sort(key = lambda cluster: cluster.total_population(), reverse=True)
    center_list = [cl_copy[idx].copy() for idx in range(num_clusters)]

    for _ in range(num_iterations):
        # initialize k empty sets (clusters)
        k_cluster_list = [alg_cluster.Cluster(set(), 0, 0, 0, 0) for _ in range(num_clusters)]
        
        # iterate through all points
        for point in cluster_list:
            min_dist = float('inf')
            min_idx_c = -1
            # iterate through all centers to find closest to point
            for idx_c, center in enumerate(center_list):
                dist = center.distance(point)
                if dist < min_dist:
                    min_dist = dist
                    min_idx_c = idx_c
            
            # add point to the closest cluster
            k_cluster_list[min_idx_c].merge_clusters(point)

        # update center_list
        center_list = [k_cluster_list[idx].copy() for idx in range(num_clusters)]

    return k_cluster_list