# Quiz 8a Solutions

### P1
`set([])`, `set([1, 2, 3])`

### P2

`s.remove(x)`, `s.symmetric_difference_update(t)`

### P3

#### First attempt

`s.union(t.difference(s))`, `s.intersection(s.union(t))`

#### Second attempt

`s.union(s.symmetric_difference(t))`, `s.union(t.difference(s))`

### P4

#### First attempt

Names for everyone taking this course, Group of distinct cities

#### Second attempt

Group of distinct cities

### P5

Modern movies: 24 fps

CodeSkulptor: 60 fps

### P6

age

### P7

60

### P8

```python
def next(x):
    return (x ** 2 + 79) % 997

x_set = set([])

x = 1
for i in range(1000):
    print x
    x_set.add(x)
    x = next(x)
    
print(len(x_set)) # 46
```

### P9

Scott