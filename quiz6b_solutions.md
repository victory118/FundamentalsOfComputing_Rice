# Quiz 6b Solutions

### P1
(36.5, 49)

### P2

#### First attempt

$(73.0/2 + 73.0*12, 98.0/2 + 98.0\\times3)$ = (912.5, 343)

#### Second attempt

I entered in a `,` instead of a space to separate the values.

### P3

Replace `www` with `dl`.

### P4

No `return` statement is needed in `__init__`.

### P5

#### First attempt

```python
def list_extend_many(lists):
    result = []
    for i in range(len(lists)):
        result.extend(lists[i])
    return result

# This should not be selected 
# This loops over all the items in the list, but in the reverse order. Sometimes that is fine, but here it the result is in reversed.
def list_extend_many(lists):
    result = []
    for i in range(len(lists) - 1, -1, -1):
        result.extend(lists[i])
    return result

def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists):
        i += 1
        result.extend(lists[i])
    return result
```

#### Second attempt

Omit the second option.

### P6

```python
n = 1001
while n != 0:
    …     # Assume this doesn't modify n.
    n -= 2
```

```python
n = 127834876
while n >= 0:
    …     # Assume this doesn't modify n.
    n //= 2
```



### P7

```python
n = 1000

numbers = range(2,n)

results = []
print len(results)

while len(numbers) > 0:
    results.append(numbers[0])
    for num in numbers:
        if num % results[-1] == 0:
            numbers.remove(num)
            
print len(results) # 168
```

### P8
```python
years = 100

slow = 1000
fast = 1

for i in range(1, years):
    print("year: " + str(i) + ", slow: " + str(slow) + ", fast: " + str(fast))
    if fast > slow:
        break
    slow = slow*2*0.6
    fast = fast*2*0.7
# 46
```

Incorrect Response 

You're off by one, which means that you likely looked at the populations at the beginning of the year, instead of the end.

#### Second attempt

Enter in 45 instead of 46.