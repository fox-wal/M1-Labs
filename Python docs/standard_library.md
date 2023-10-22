tags: #python #docs #library

---

# Python Standard Library

## OS

1. Enables inspection of environment variables
2. Getting user- and process-related information

```python
import os

print('USERNAME environment variable:', os.environ['USERNAME'])
```

Several operations such as parsing and building paths can be done with `os.path`.

```python
import os.path
import time

print('File         :', __file__) # Path of current Python file.
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
```

## Platform

1. Contains information about the interpreter and machine where the process is running

```python
import platform
print('Machine network name:', platform.node())
print('Python version:', platform.python_version())
print('Operating system:', platform.system())
```

## Sys

1. Provides helpful system-specific information such as information about the runtime environment

```python
import sys
print('Python path:', sys.path)
# for command line arguments
print('Command to run Python:', sys.argv)
```

## DateTime and Time

Three types for:

1. Date
2. Time
3. Timestamps

```python
import datetime
import time

today = datetime.date.today()
print("Today's date is: ", today)

now = datetime.datetime.today() # we can also use the now() method
print("Current timestamp: ",now.strftime("%m/%d/%Y, %H:%M"))

print(time.time()) # Prints the number of elapsed seconds 
```

## Numbers

1. Defines an abstract hierarchy of numeric types.

## Math and CMath

1. Implementations of advanced mathematical functions.

## Random

1. Pseudorandom number generator.

Function|Description|Example
---|---|---
`randint`|Returns a random integer between the specified limits.|`r = random.randint(1, 101)`
`choice`|Returns a random member from a list.|`day = random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])`

## More

Book: Hellmann's The Python 3 Standard Library by Example