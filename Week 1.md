# Python as a Calculator

## Task 1

```cmd
>>> print('hello')
hello
>>> input('favourite book title')
favourite book titleyo
'yo'
>>> input('favourite book title\n')
favourite book title

''
>>> print(3+5)
8
>>> 2**4
16
>>> 15//4
3
>>> 6%5
1
>>> 1-0.99
0.010000000000000009
>>> 13//2
6
>>> 13%2
1
>>> 7.5**2
56.25
```
![](Uni/1.1%20-%20Programming%20Fundamentals/W1T1.png)

```python
print(13//2)
print(13%2)
print(1-0.99)
print(7.5**2)
```

```Output
6
1
0.010000000000000009
56.25
```

## Task 2

```python
hours = float(input('Hours [float, 0-24]: '))
minutes = hours * 60
print("Time in minutes:", minutes)
```

```Output
Hours [float, 0-24]: 16.19
Time in minutes: 971.4000000000001
```

## Task 3

```python
print("Enter how much you spend on each of these every month:")
rent = float(input('rent: £'))
transport = float(input('transport: £'))
groceries = float(input('groceries: £'))
eatingOut = float(input('eating out: £'))

total = rent + transport + groceries + eatingOut
print('Total: £', total.__round__(2), sep="")
```

```Output
Enter how much you spend on each of these every month:
rent: £600
transport: £50
groceries: £200
eating out: £53.789
Total: £903.79
```

# String Operations

```python
weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, with plenty of winter sunshine developing. However, patchy cloud and isolated showers may move in from the west later in the afternoon."
```

## Task 1: Split

```python
lines = weather.split('\n')
words = weather.split(' ')
phrases = weather.split(',')
sentences = weather.split('.')
```

## Task 2

```python
print(len(weather))
```

```Output
207
```

## Task 3: Lowercase

```python
weather_lc = weather.lower()
```

## Task 4: Sunshine

```python
if weather.find("sunshine") == -1:
    print("There will not be sunshine on Friday.")
else:
    print("There will be sunshine on Friday.")
```

```Output
There will be sunshine on Friday.
```

## Output

![](Uni/1.1%20-%20Programming%20Fundamentals/W1T2.png)