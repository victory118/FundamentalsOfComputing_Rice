# POC Part 2 - Homework 3 Solutions

### P1

None

### P2

$n$

### P3

```python
if self._parent is None:
    return self
else:
    return self._parent.get_root()
```

### P4

```python
if self._parent is None:
    return 0
else:
    return self._parent.depth() + 1
```

### P5

$2^n$

### P6

$$
\sum_{i=0}^{n} 2^{i} = 2^0 + 2^1 + 2^2 + ... + 2^n = 2^{n+1}-1
$$

### P7

$4 + 4^2 + 4^3=84$ 

### P8

height, children (wrong)

Should be selected: num_leaves, num_nodes

### P9

```python
[[[a], [b], c], [e], d]
```

### P10

In-order traversal









