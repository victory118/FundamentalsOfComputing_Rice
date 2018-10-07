# POC Part 1 - Homework 5 Solutions

### P1
0

### P2

100 + 100 + ... + 100 + 100 (with $d$ terms in the sum)

### P3

100*d

### P4

2

### P5

1000 + 2000 + 3000 + ... + 1000n

### P6

$\sum_{i=0}^{n} 1000i = 1000 \times \frac{1}{2}(n+1)(n) = 500(n^2 + n)$

where $n$ represents the total number of bribes. Given that each bribe happens every 10 days, we should substitute $n=d/10$. This means that every 10 days is equivalent to one extra bribe.

$500(n^2 + n) = 500((d/10)^2 + (d/10)) = 5d^2 + 50d$

### P7

No, the graph does not approach a straight line.

### P8

$e ^ {0.095d}$

### P9

$1.15^{n-1}$

### P10

The cost of an upgrade in Cookie Clicker grows faster than the cost of a bribe in the greedy boss scenario.

### P11

```python
TEST_CASES = [[2, 0, 2, 4], \
                [0, 0, 2, 2], \
                [2, 2, 0, 0], \
                [2, 2, 2, 2, 2], \
                [8, 16, 16, 8]] # successfully passed
                # grade code: 0634386 / 50% incorrect programs
```

```python
# generate random test cases from length 1 to 10
import random

TEST_CASES = []

for idx in range(1, 11):
    TEST_CASES.append([random.choice([0, 2, 4, 8, 16]) for _ in range(idx)])

print "TEST_CASES = ["
for idx in range(len(TEST_CASES)):
    print TEST_CASES[idx], ","
print "]"

# copy and paste the above output and submit to owltest
TEST_CASES = [
[16] ,
[4, 0] ,
[16, 0, 8] ,
[4, 8, 2, 4] ,
[4, 2, 0, 2, 8] ,
[16, 16, 4, 16, 4, 8] ,
[8, 0, 4, 2, 2, 0, 0] ,
[4, 2, 16, 16, 2, 16, 8, 16] ,
[16, 8, 4, 2, 0, 0, 16, 0, 4] ,
[4, 0, 8, 8, 8, 8, 4, 8, 8, 8] ,
]
# grade code: 2237842 / caught 80% incorrect programs
```











