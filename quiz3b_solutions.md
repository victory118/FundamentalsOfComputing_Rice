Quiz 3b Solutions
==========

### P1
Unlimited — It is called repeatedly until you stop the program.

### P2
1. Have a global counter for the number of timer calls.

	In the timer handler, increment the counter. In the timer handler, check the count and possibly stop the timer.

### P3
You can't. But, you can stop this timer, and start a new one with a different frequency and same handler.

### P4
Unlimited

### P5
Second

### P6
```python
import time

time1 = time.time()

minutes = int(time1/60)
hours = int(time1/60/60)
days = int(time1/60/60/24)
years = int(time1/60/60/24/365)

print years # 48
```

### P7
Square root of $n$

### P8
```python
# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = 217
iteration = 0
max_iterations = 20

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n

def get_next(current):
    """??? Part of mystery computation."""
    if current%2 == 0:
        return current/2.0
    else:
        return current*3.0 + 1

# timer callback

def update():
    """??? Part of mystery computation."""
    global iteration, result
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)
        print result

# register event handlers

timer = simplegui.create_timer(1, update)

# start program

init(result)
timer.start()
# max value is 736
```

### P9
To save resources, modern browsers only execute the Javascript associated with the topmost tab of a window. The animation freezes since the code tab and its associated Javascript is no longer the topmost tab.