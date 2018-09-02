# Quiz 4b Solutions

### P1
tuple

### P2
#### First submit

Strings, Tuples (wrong)

#### Second submit

Numbers, Booleans, Strings, Tuples

### P3
function2

### P4
```python
y = x
x[2] = 10
```

```python
y = x
y[-3] = 10
```

### P5

The + operator on lists does not mean addition of the numbers in a list.

### P6

3

### P7

yes

### P8
#### First attempt

Unpredictable

#### Second attempt

A nonlinear smooth curve

#### Third attempt

A straight line

### P9
```python
# http://www.codeskulptor.org/#user45_MRdBGcVGkk_5.py

import simplegui
val = 5
count = 0
message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"
    
def keydown(key):
    global val
    val *= 2
    
def keyup(key):
    global val, count
    val -= 3
    count += 1
    print 'val = ', val
    print 'count = ', count

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start the frame animation
frame.start()
# after 12 separate key presses, val = 8195
```

