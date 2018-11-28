# Homework 2 Solutions - Algorithmic Thinking 1

### P1
The set of all nodes that have degree 0.

### P2

$O(n)$ if the first node in the nested for loop is connected to the node in the outer for loop.

### P3

$O(n^2)$

### P4

$f(n)$ is $O(n^2)$

### P5

$f(n)$ is $O(1)$

### P6

$f(n)$ is $O(n)$

### P7

$f(n)$ is $O(n^3)$

### P8

$c = a_0 + a_1 + a_2 + a_3$

### P9

$c=a_0/8 + a_1/4 + a_2/2 + a_3$

### P10

**1st submit**

7 8 (wrong)

**2nd submit**

3 8

### P11

CC Visited returns a set containing all sets of connected nodes

Line 5: $g, i$

Line 8: $d_u \neq \infty$

Line 10: $CC \cup set([W])$

Line 11: $RemainingNodes-W$

### P12

**1st submit**

$O(m)$

Incorrect. The algorithm minimally has to examine all $n$ nodes.

**2nd submit**

$O(mn^2+n^3)$

Incorrect. There is a tighter bound among the alternative answers.

**3rd submit**

$O(n^2)$

### P13

Line 5: $g, i$

Line 6: $CC \cup set([W])$

Line 7: $RemainingNodes-W$

### P14

**1st submit**

$O(n^2)$

Incorrect. There are tighter bounds in the alternative answers.

**2nd submit**

$O(m+n)$ (linear running time)


### P15

The running time of **CC-Distance** is asymptotically slower than that of **CC-Visited** due to the initialization of $d$ in lines 2-3 of **BFS-Distance**.

### P16

$(A^k)[i,j]$

### P17

The length of the shortest path is the smallest non-negative integer $k$ such that $(A^k)[i,j]$ is non-zero.

### P18

$(A^k)[i,j]−(\hat{A}^k)[i,j]$ where $k$ is the length of the shortest path from node $i$ to node $j$ in $g$.









