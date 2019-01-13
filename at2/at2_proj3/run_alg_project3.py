import alg_project3_solution
import alg_cluster


# Test case 1

# closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), 
    # alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 1.5, 1.0)
    # expected one of the tuples in set([(1.0, 1, 2)]) but received (1.0, 0, 1)

# cluster_list = [alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), 
#                 alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)]
# x_mid = 1.5
# half_width = 1.0

# Test case 2

# closest_pair_strip([alg_cluster.Cluster(set([]), 1.0, 1.0, 1, 0), alg_cluster.Cluster(set([]), 1.0, 5.0, 1, 0),
#  alg_cluster.Cluster(set([]), 1.0, 4.0, 1, 0), alg_cluster.Cluster(set([]), 1.0, 7.0, 1, 0)], 1.0, 3.0)
#  expected one of the tuples in set([(1.0, 1, 2)]) but received (1.0, 2, 1)

# cluster_list = [alg_cluster.Cluster(set([]), 1.0, 1.0, 1, 0), alg_cluster.Cluster(set([]), 1.0, 5.0, 1, 0), 
#                 alg_cluster.Cluster(set([]), 1.0, 4.0, 1, 0), alg_cluster.Cluster(set([]), 1.0, 7.0, 1, 0)]
# x_mid = 1.0
# half_width = 3.0

# Test case 3

# closest_pair_strip([alg_cluster.Cluster(set([]), -4.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 0.0, -1.0, 1, 0), 
# alg_cluster.Cluster(set([]), 0.0, 1.0, 1, 0), alg_cluster.Cluster(set([]), 4.0, 0.0, 1, 0)], 0.0, 4.123106) 
# expected one of the tuples in set([(2.0, 1, 2)]) but received (4.123105625617661, 0, 1)

# cluster_list = [alg_cluster.Cluster(set([]), -4.0, 0.0, 1, 0), alg_cluster.Cluster(set([]), 0.0, -1.0, 1, 0), 
#                 alg_cluster.Cluster(set([]), 0.0, 1.0, 1, 0), alg_cluster.Cluster(set([]), 4.0, 0.0, 1, 0)]
# x_mid = 0.0
# half_width = 4.123106

# (d, i, j) = alg_project3.closest_pair_strip(cluster_list, x_mid, half_width)
# print((d,i,j))

# fast_closest_pair
# Test case 1

# fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), 
# alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)]) 
# expected one of the tuples in set([(1.0, 1, 2), (1.0, 0, 1), (1.0, 2, 3)]) but received (inf, -1, -1)

# cluster_list = [alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0),
#                 alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)]
# (d, i, j) = alg_project3.fast_closest_pair(cluster_list)
# print((d,i,j))

# fast_closest_pair([alg_cluster.Cluster(set([]), 0.02, 0.39, 1, 0), alg_cluster.Cluster(set([]), 0.19, 0.75, 1, 0), 
# alg_cluster.Cluster(set([]), 0.35, 0.03, 1, 0), alg_cluster.Cluster(set([]), 0.73, 0.81, 1, 0), 
# alg_cluster.Cluster(set([]), 0.76, 0.88, 1, 0), alg_cluster.Cluster(set([]), 0.78, 0.11, 1, 0)]) 
# expected one of the tuples in set([(0.07615773105863904, 3, 4)]) but received (0.07615773105863904, 0, 1)

# cluster_list = [alg_cluster.Cluster(set([]), 0.02, 0.39, 1, 0), alg_cluster.Cluster(set([]), 0.19, 0.75, 1, 0),
#                 alg_cluster.Cluster(set([]), 0.35, 0.03, 1, 0), alg_cluster.Cluster(set([]), 0.73, 0.81, 1, 0),
#                 alg_cluster.Cluster(set([]), 0.76, 0.88, 1, 0), alg_cluster.Cluster(set([]), 0.78, 0.11, 1, 0)]
# (d, i, j) = alg_project3.fast_closest_pair(cluster_list)
# print((d,i,j))

# hierarchical_clustering
# Test case 1

cluster_list = [alg_cluster.Cluster(set([]), 0.02, 0.39, 1, 0), alg_cluster.Cluster(set([]), 0.19, 0.75, 1, 0),
                alg_cluster.Cluster(set([]), 0.35, 0.03, 1, 0), alg_cluster.Cluster(set([]), 0.73, 0.81, 1, 0),
                alg_cluster.Cluster(set([]), 0.76, 0.88, 1, 0), alg_cluster.Cluster(set([]), 0.78, 0.11, 1, 0)]

alg_project3_solution.hierarchical_clustering(cluster_list, 1)

print(cluster_list)
