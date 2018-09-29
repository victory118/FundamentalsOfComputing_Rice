# POC Part 1 - Homework 3 Solutions

### P1
sample space

### P2

0.25

### P3

4

### P4

```python
random.randrange(6) + 1
random.randrange(1, 7)
```

### P5

1/17

### P6

$0.3*4 + 0.4*3 + 0.2*2 + 0.1*1 = 2.9$

### P7

Odd + odd = even

odd + even = odd

even + odd = odd

even + even = even

Probability of sum being even or odd are both 0.5. Thus $E[x] = 0.5*1 + 0.5*1 = 0$.

### P8

(n-1)/2

### P9

#### First attempt

pi

#### Second attempt

pi/4

### P10

TEST_CASES = [0, 11, 321, 613, 111, 101, 10, 700, 670, 5276]

code: **3202207**

```python
def format(t):
    D_tenthSec = t % 10
    C_sec = (t/10) % 10
    B_tenSec = (t/100) % 6
    A_min = t/600
    
    return str(A_min) + ":" + str(B_tenSec) + str(C_sec) + "." + str(D_tenthSec)

def format1(t):
    a = (t // 600)
    b = (((t % 600) / 10) / 10)
    c = '0'
    if (t > 10):
        c = str(t)[(-2)]
    d = str(t)[(-1)]
    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
    return formatedTime

def format2(run_time):
    global run_time_str, d_run_time
    bc_run_time = (run_time / 10)
    d_run_time = (run_time % 10)
    if (bc_run_time > 59):
        a_run_time = (bc_run_time / 60)
        bc_run_time = (bc_run_time - (60 * a_run_time))
    else:
        a_run_time = 0
    if (bc_run_time > 10):
        str_current_time = ((((str(a_run_time) + ':') + str(bc_run_time)) + '.') + str(d_run_time))
    else:
        str_current_time = (((((str(a_run_time) + ':') + '0') + str(bc_run_time)) + '.') + str(d_run_time))
    return str_current_time

def format3(t):
    if (t <= 9):
        A = '0'
        B = '0'
        C = '0'
    elif (len(str(t)) == 2):
        A = '0'
        B = '0'
        C = (t // 10)
    else:
        A = (t // 600)
        t = (t % 600)
        if (len(str(t)) == 3):
            B = ((t // 10) // 10)
            C = ((t // 10) % 10)
        elif (len(str(t)) < 3):
            if (t <= 59):
                B = '0'
                C = (t // 10)
            else:
                B = (((t % 60) // 10) % 10)
                C = (t // 10)
    D = (t % 10)
    return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))

print "format1"
for run_time in range(6000):
    if format(run_time) != format1(run_time):
        print run_time
        print format(run_time)
        print format1(run_time)

print "format2"
for run_time in range(6000):
    if format(run_time) != format2(run_time):
        print run_time
        print format(run_time)
        print format2(run_time)
        
print "format3"
for run_time in range(6000):
    if format(run_time) != format3(run_time):
        print run_time
        print format(run_time)
        print format3(run_time)
```











