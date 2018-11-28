# Homework 1 Solutions - Algorithmic Thinking 1

### P1
0

### P2

**1st Submit:**

6 (Wrong)

**2nd Submit:**

1

### P3

Connectivity (node #: # connected edges): {0: 3, 1: 3, 2: 3, 3: 2, 4: 2, 5: 1, 6: 4}

Degree distribution (# of connected edges: # of nodes that with): {0: 1, 1: 1, 2: 2, 3: 3, 4: 1}

Normalized (Total 8): {0: 1/8, 1: 1/8, 2: 2/8, 3: 3/8. 4: 1/8}

### P4

| Node # | In-degree | Out-degree |
| ------ | --------- | ---------- |
| 0      | 1         | 3          |
| 1      | 2         | 2          |
| 2      | 2         | 2          |
| 3      | 2         | 2          |
| 4      | 2         | 1          |
| 5      | 1         | 1          |
| 6      | 1         | 0          |
| 7      | 2         | 2          |

5 nodes have in-degree 2.

### P5

The entry A[2,1] of an adjacency matrix will be 1 if node 2 goes in to node 1 and 0 otherwise. Thus the value is 0.

### P6

4 nodes have out-degree 2.

### P7

n-1

### P8

**1st Submit:**

$\sum \limits_{k = 1}^{N-1} (k-1) = \frac{n(a_1+a_n)}{2}=(N-1)(0+N-2)/2=(N-1)(N-2)/2$ (Wrong)

**2nd Submit:**

$\sum \limits_{k = 1}^{n-1} (k) = \frac{1}{2}(n)(n-1)$

### P9

${n-1\choose k}$ counts how many different ways we can select k objects out of a set of n-1 objects when order doesn't matter. This represents the number of *combinations*. 

### P10

Lower = 0 and upper = n-1

### P11

0

### P12

There are ${10 \choose 2}=45$ possible pairs of nodes. ER(10,1) means that there is a 100% probability that each of the node pairs will be connected by an edge so the answer is 45.

### P13

**1st Submit:**

In P12, I found that there are ${n \choose 2}=n(n-1)/2$ possible pairs of nodes. If the probability of them being connected is $p$, then the expected value of the degree of a node in a graph $g$ is $p(n)(n-1)/2$.(Wrong) 

**2nd Submit:**

The expected value of the total number of edges is $p(n)(n-1)/2$. If each edge is divided evenly between each node and each edge gets counted twice (one for each vertice of an edge), then the expected value of the degree of a node is $p(n-1)$.

### P14

**1st Submit:**

The probability of getting exactly $k$ successes in $n$ trials is given by the probability mass function:
$$
Pr(k;n,p)={n \choose k}p^k(1-p)^{n-k}
$$
(Wrong)

**2nd Submit:**

Try: 
$$
Pr(k;n-1,p)={n-1 \choose k}p^k(1-p)^{n-1-k}
$$


### P15

The running time will be proportional to the number of possible nodes which is $n(n-1)/2$. Thus, the running time is proportional to $n^2$.

### P16

**1st Submit:**

The answer should be 0, but it could be $n^2$ depending on the interpretation of the question. (Wrong)

**2nd Submit:**

Try: Some constant $c>0$

**3rd Submit:**

Try: $n^2$ (I think the reasoning is you have to iterate through all possible edges anyway regardless of the probability $p$.)

### P17

If a graph $g$ representing an undirected graph has $n$ nodes and $m$ edges is given by its adjacency matrix, it would take order $n^2$ computations to compute the degree distribution of the graph.

### P18

If a graph $g$ representing an undirected graph has $n$ nodes and $m$ edges is given by its adjacency list, it would take order $m+n$ computations to compute the degree distribution of the graph. You would have to check each of the $n$ nodes and $m$ edges.









