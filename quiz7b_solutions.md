# Quiz 7b Solutions

### P1
The radius corresponds to the third argument which is 35.

### P2

one `ImageInfo` object, ten `Sprite` objects

### P3

#### First attempt (partial credit)

Add a size attribute in the `ImageInfo` class and a size parameter to `ImageInfo.__init__`. Use this attribute when drawing the sprite.

#### Second attempt

Add a size attribute in the `Sprite` class and a size parameter to `Sprite.__init__`. Use the size attribute when drawing the sprite.

### P4

0 to 1

### P5

* The given URL exists, but is inaccessible due to network problems.
* No file is found with the given URL.
* Your browser is loading a big sound file. Wait longer.
* A file found with the given URL isn't a sound file recognized by your browser.
* You have set the volume level to 0.

### P6

#### First attempt

"rgb(0, 0, 255)", "#0000FF"

"Blue" should also be selected

#### Second attempt

"rgb(0, 0, 255)", "#0000FF", "Blue"

### P7

```python
def move_dimension(dimension, position, vector):
    """Moves the position component by the given vector component in 1D toroidal space."""
    position[dimension] = (position[dimension] + vector[dimension]) % SCREEN_SIZE[dimension]

def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    move_dimension(0, position, vector)
    move_dimension(1, position, vector)
```

```python
NUM_DIMENSIONS = 2
def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    for d in range(NUM_DIMENSIONS):
        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]
```

### P8

You only need to get the code correct *once*.

### P9

Appearing on *An Introduction to Interactive Programming in Python*