# Quiz 5b Solutions

### P1
`{}` and `dict()`

### P2
```python
favorites["fruit"] = "blackberry"
```

### P3
Strings, Booleans, Tuples, Numbers

### P4

Numbers, Dictionaries, Lists, Booleans, Strings, Tuples (All)

### P5

```python
my_dict.items()
```

### P6

#### First attempt

1. Storing `x` and `y` coordinates of 2-dimensional points taken from a function, so that each `x` coordinate occurs at most once.
2. Storing a sensor's data samples (should not be selected)
3. Storing where each person lives

#### Second attempt

1. Storing `x` and `y` coordinates of 2-dimensional points taken from a function, so that each `x` coordinate occurs at most once.
2. Storing where each person lives

### P7

```python
[number for number in my_list if is_even(number)]
[n for n in my_list if is_even(n)]
```

### P8
The source arguments in `draw_image` are incorrect. We are trying to load pixels that are not within the image, and thus the draw fails.

### P9
```python
import simplegui

frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    canvas.draw_image(image, [220, 100], [100, 100], 
                     [frame_size[0] / 2, frame_size[1] / 2], 
                     frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")
frame.start() # the word "tin" appears in the canvas
```
