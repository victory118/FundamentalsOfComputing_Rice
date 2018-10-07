# POC Part 1 - Homework 4 Solutions

### P1
$2^5=32$

### P2

Possible outcomes: (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)

Possible products: 1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16

Sum = 10 + 20 + 30 + 40 = 100

Expected value = sum/(possible outcomes) = 100/16  = 6.25

### P3

Possible outcomes = 01234, 12345, etc (6 outcomes for ascending order)

Total number outcomes = 12 (ascending + descending order)

Number of possible 5 digit sequences = 10^5

Probability = $12/10^5$ = 0.00012

### P4

Probability = $12 \times \frac{(10-5)!}{10!}​$ = 

### P5

```
Answer is ('b', 'e', 'c', 'd')
```

### P6

$\{\}, \{1\},$ and $\{1, 2\}$ are subsets of $\{1, 2\}$.

### P7

$2^n$

### P8

Possible 5 card hands = $\frac{52!}{(52-5)!}$

Possible 5 card hands of the same suit = $52\times \frac{12!}{8!}$

Probability of drawing 5 cards of the same suit = 0.00198079231693

### P9

$\frac{m!}{n!(m-n)!}$

### P10

```python
TEST_CASES = [[0, 0, 1, 1, 3, 5, 0], \
                [0, 2], \
                [0, 1, 6], \
                [0, 2, 2], \
                [0, 3, 2, 3], \
                [0, 1, 2, 3, 3, 5]] # successfully passed
\# grade code:2004349
```











