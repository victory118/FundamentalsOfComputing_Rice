# POC Part 2 - Homework 2 Solutions

### P1
28

### P2

$\frac{1}{2} n(n+1)$

### P3

$n!$

### P4

```python
count = 0

def fib(num):
    global count
    count += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
    
fib(0)
print "count = ", count
count = 0

fib(1)
print "count = ", count
count = 0

fib(2)
print "count = ", count
count = 0

fib(3)
print "count = ", count
count = 0

fib(4)
print "count = ", count
count = 0

fib(5)
print "count = ", count
count = 0
```


$$
f(0) = 1 \\
f(1) = 1 \\
f(n) = f(n-1) + f(n-2) + 1
$$

### P5

```python
count = 0

def memoized_fib(num, memo_dict):
    global count
    count += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

memo_dict = {0: 0, 1: 1}
print memoized_fib(2,{0:0,1:1})
print "count = ", count
count = 0
print memoized_fib(3,{0:0,1:1})
print "count = ", count
count = 0
print memoized_fib(4,{0:0,1:1})
print "count = ", count
count = 0
print memoized_fib(5,{0:0,1:1})
print "count = ", count
count = 0
print memoized_fib(6,{0:0,1:1})
print "count = ", count
count = 0
```

$2n-1$

### P6

$$
p(0) = 1 \\
p(n) = np(n-1)
$$

### P7

$n!$

### P8

$n$

### P9

$$
t(1) = 1 \\
t(n) = 2t(\frac{n}{2}) + n
$$



### P10

$n \log{n}$









