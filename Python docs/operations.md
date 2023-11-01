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

```python
x.bit_length()
```

--> number of bits necessary to represent this integer

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

|   |   |   |
|---|---|---|
|`:<`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder1)|Left aligns the result (within the available space)|
|`:>`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder2)|Right aligns the result (within the available space)|
|`:^`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder3)|Center aligns the result (within the available space)|
|`:=`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder4)|Places the sign to the left most position|
|`:+`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder5)|Use a plus sign to indicate if the result is positive or negative|
|`:-`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder6)|Use a minus sign for negative values only|
|`:`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder7)|Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)|
|`:,`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder8)|Use a comma as a thousand separator|
|`:_`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder9)|Use a underscore as a thousand separator|
|`:b`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder10)|Binary format|
|`:c`||Converts the value into the corresponding unicode character|
|`:d`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder12)|Decimal format|
|`:e`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder13)|Scientific format, with a lower case e|
|`:E`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder14)|Scientific format, with an upper case E|
|`:f`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder15)|Fix point number format|
|`:F`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder16)|Fix point number format, in uppercase format (show `inf` and `nan` as `INF` and `NAN`)|
|`:g`||General format|
|`:G`||General format (using a upper case E for scientific notations)|
|`:o`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder19)|Octal format|
|`:x`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder20)|Hex format, lower case|
|`:X`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder21)|Hex format, upper case|
|`:n`||Number format|
|`:%`|[Try it](https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder23)|Percentage format|