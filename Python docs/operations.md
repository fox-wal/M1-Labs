tags: #python #docs 

---

# Operations

## [Numeric](variables#Numeric)

### Basic Arithmetic

Symbol|Operation
---|---
`+`|Add
`-`|Subtract
`/`|Divide
`//`|Integer division
`%`|Mod (remainder)
`*`|Multiply
`**`|Exponent

### Round

```python
round(number, decimal_places)
```

## [String](variables#String)

### Split

```python
sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.split())
```

### Concatenate

```python
print("Hello. " + sentence)
print(", ".join(["hi", "i", "like", "cake"]))
print("_".join(sentence.split()))
```

This is how NOT to concatenate strings. This code will create a tuple:
```python
my_tuple = "hi", "i", "like", "cake"
```

### Format

```python
variables = 79
f_string = f"Embed literal values {76895.70 + 7} and {variables} in a string."

my_string = "This could be {} when formatting strings {} from a file.".format("useful", "that are loaded")
```

- [ ] #todo/search research how % works

```python
print('You can also format numbers like %2f <-- that' %50.98765)
```