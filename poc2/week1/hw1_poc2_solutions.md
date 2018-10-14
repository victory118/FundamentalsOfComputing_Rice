# POC Part 2 - Homework 1 Solutions

### P1
$n^2$

### P2

$n\log (n)$ comparisons is the minimum for sorting

### P3

$n$

### P4

1. The last element pushed onto the stack is the first element popped off of the stack.
2. The first element pushed onto the stack is the last element popped off of the stack.

### P5

1. The first element enqueued into the queue is the first element dequeued out of the queue.
2. The last element enqueued into the queue is the last element dequeued out of the queue.

### P6

```python
grid_height = 6
grid_width = 9

def fun1(row, col):
    up = (row - 1) % grid_height
    down = (row + 1) % grid_height
    left = (col - 1) % grid_width
    right = (col + 1) % grid_width
    return [[up, col], [down, col], [row, left], [row, right]]

print fun1(1,0)
print fun1(0,6) # gives the correct output

def fun2(row, col):
    up = (row - 1) % (grid_height - 1)
    down = (row + 1) % (grid_height - 1)
    left = (col - 1) % (grid_width - 1)
    right = (col + 1) % (grid_width - 1)
    return [[up, col], [down, col], [row, left], [row, right]]

print fun2(1,0)
print fun2(0,6)

def fun3(row, col):
    up = (row - 1) % (grid_height - 1)
    down = (row + 1) % (grid_height - 1)
    left = (col - 1) % (grid_width - 1)
    right = (col + 1) % (grid_width - 1)
    return [[up, col], [down, col], [row, left], [row, right]]

print fun3(1,0)
print fun3(0,6)

def fun4(row, col):
    up = (row - 1) % (grid_height - 1)
    down = (row + 1) % (grid_height - 1)
    left = (col - 1) % (grid_width - 1)
    right = (col + 1) % (grid_width - 1)
    return [[up, col], [down, col], [row, left], [row, right]]


print fun4(1,0)
print fun4(0,6)
```

### P7

```python
if self.is_empty(neighbor[0], neighbor[1]):
```

### P8

$m n$

### P9

```python
"""
Stack class
"""

class Stack:
    """
    A simple implementation of a FILO stack.
    """

    def __init__(self):
        """ 
        Initialize the stack.
        """
        self._items = []

    def __len__(self):
        """
        Return number of items in the stack.
        """
        return len(self._items)

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return str(self._items)

    def push(self, item):
        """
        Push item onto the stack.
        """        
        self._items.append(item)

    def pop(self):
        """
        Pop an item off of the stack
        """
        self._items.pop()

    def clear(self):
        """
        Remove all items from the stack.
        """
        self._items = []

############################
# test code for the stack

my_stack = Stack()
my_stack.push(72)
my_stack.push(59)
my_stack.push(33)
my_stack.pop()
my_stack.push(77)
my_stack.push(13)
my_stack.push(22)
my_stack.push(45)
my_stack.pop()
my_stack.pop()
my_stack.push(22)
my_stack.push(72)
my_stack.pop()
my_stack.push(90)
my_stack.push(67)
print my_stack
while len(my_stack) > 4:
    my_stack.pop()
print my_stack
my_stack.push(32)
my_stack.push(14)
my_stack.pop()
my_stack.push(65)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.push(34)
my_stack.push(38)
my_stack.push(29)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print my_stack
print my_stack.pop() # this returns None, but the number popped is 77

```



### P10

#### 1st attempt

a, d

#### 2nd attempt

a, b, d











