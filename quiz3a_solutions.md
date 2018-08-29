Quiz 3a Solutions
==========

### P1
`+`

### P2
The canvas

### P3
Some or none of the text is shown. Conceptually, the text is drawn at whatever coordinates are given, but only whatever text fits within the canvas coordinates is shown.

### P4
```python
canvas.draw_line((200, 300), (0, 0), 10, "Green")
```

### P5
```python
str(month)+"/"+str(day)
```

### P6
```python
test = '1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1'

print test.count('l') # 60
```

### P7
In a draw handler, or a helper function called from it

### P8
```python
int("5")
float("5.4")
```

### P9
```python
import simplegui

# define draw handler
def draw(canvas):
    #canvas.draw_text("Hello!",[100, 100], 24, "White")
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210, 200], 20, 10, "White")
    canvas.draw_line([55, 180], [250, 180], 40, "Red")
    canvas.draw_line([55, 170], [90, 120], 5, "Red")
    canvas.draw_line([90, 120], [130, 120], 5, "Red")
    canvas.draw_line([180, 108], [180, 160], 140, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 300)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start() # Drawing of a truck (automobile)
```

### P10
Largest first