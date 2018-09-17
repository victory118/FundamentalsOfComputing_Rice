# Quiz 7a Solutions

### P1
```python
point = Point2D(3, 9)
point.translate(5, -2)
```

```python
point1 = Point2D(3, 9)
point2 = Point2D()
point2.translate(20, 4)
```

### P2

```python
points = [Point2D(2, 5), Point2D(8, 3), Point2D(0, 2)]
for point in points:
    point.translate(-1, -1)
```

### P3

```python
point = Point2D(3, 6)
s = str(point)
```

### P4

clockwise, radians

### P5

Add another call to the `Ship` constructor, assigning the result to another global variable.

```python
ship1 = Ship(…)
ship2 = Ship(…)
```

### P6

#### First attempt

Firefox and Chrome fully support MP3 audio files.

#### Second attempt

Safari and Chrome fully support MP3 audio files.

### P7

This can be modeled as a discrete time system:
$$
v[k+1] = cv[k] + a[k]
$$
where $c = 0.9$ because friction induces a deceleration that is 10% of the ship's velocity per second. Taking the z transform gives:
$$
zV(z) = 0.9V(z) + A(z)\\
V(z) = \frac{A(z)}{z-0.9}
$$
The acceleration $a[k]$ is constant so it can be represented as a step function of magnitude 10:
$$
A(z) = 10\frac{z}{z-1}
$$
We can calculate the steady state value of the velocity by using the final value theorem:
$$
\lim\limits_{z \to 1} (z-1)F(z) = (z-1)V(z) = (z-1) \frac{1}{z-0.9} \frac{10z}{z-1} = 100
$$
