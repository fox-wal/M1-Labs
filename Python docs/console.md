tags: #python #docs 

---

# Using the Console

## Output

```python
print('Hello world!')
print('I can print strings\nOr numbers, like')
print(50)
print('Or lists, such as', [0, 1, 2, 3, 4])
print('I', 'can', 'also', 'split', 'things', 'up.')
```

*Note*: default `sep = ' '`.

See [here](Python%20docs/operations#Format) for string formatting options.

## Input

```python
print('To get an input')
input('Use this function: ')
print('You can also use it without a prompt:')
input()
```

*Note*: `input()` will always return a string. If the user simply presses `Enter`, an empty string will be returned.