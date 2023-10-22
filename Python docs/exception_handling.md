tags: #python #docs

---

# Exception Handling

## Basics

### Handle

```python
try:
    # Code that could raise an error.
except <ErrorType> as e:
    # Deal with the exception you caught.
else:
    # [Optional]: Success! What to do if no errors were raised.
finally:
    # [Optional]: No matter what happened, this code will execute. Use this to
    # close files, write reports, etc.
```

### Raise

```python
raise <ErrorType>("Error message.")
```

## Choosing the Right One

### Common Existing Exceptions

|Exception|Description|Examples|
|---|---|---|
|ValueError|Raised when an argument is of a valid type but contains an invalid value.|`math.sqrt(-1)`  `int("hello")`  incorrect string format|
|FileNotFoundError|Raised when trying to open a file that does not exist (or where the specified path does not lead to a file).|
|ZeroDivisionError|Raised when you try to divide by zero.|`print(9/0)`|

### Custom Exceptions

- [ ] #todo/search Custom exception definitions.

Create a class based on the `Exception` class:

```python
class MyError(Exception):
    # Stuff
```

## Best Practices #conventions 

### 1. Be specific

...both when raising and catching exceptions. Generally try to avoid writing an `except` statement without specifying a specific error.

### 2. Do not ignore

Always handle the exceptions you catch.
