Quiz 2a Solutions
==========

### P1
Some code that you didn't write which generates the event.

### P2
#### Submit 1
Unlimited, i.e., 0 or more
#### Submit 2
1

### P3
#### Submit 1
Title, Control Area, Canvas
#### Submit 2
Status Area, Control Area, Canvas

### P4
#### Submit 1
1. Define classes (2)
2. Initialize global variables (4)
3. Define helper functions (5)
4. Define event handlers (3)
5. Create frame (1)
6. Register event handlers (6)
7. Start frame and timers (7)
#### Submit 2
(At 6:54 mark in SimpleGUI lecture)
1. Initialize global variables (4)
2. Define helper functions (5)
3. Define classes (2)
4. Define event handlers (3)
5. Create frame (1)
6. Register event handlers (6)
7. Start frame and timers (7)

### P5
```python
def a(y):
    x = x + y
    return y
```

### P6
4

### P7
#### Submit 1
a, b
#### Submit 2
f, a, b (function is in global scope)

### P8
#### Submit 1
c
#### Submit 2
c, a (local variable is defined inside function when it is called)

### P9
```python
f = simplegui.create_frame("My Frame", 100, 100)
frame = simplegui.create_frame("Testing", 200, 200, 300)
```

### P10
```python
import simplegui

frame = simplegui.create_frame("My Frame", 100, 100)
frame.set_canvas_background("Red")
frame.start()
```
```python
import simplegui

frame = simplegui.create_frame("My Frame", 100, 100)
frame.set_canvas_background("#FF0000")
frame.start()
```