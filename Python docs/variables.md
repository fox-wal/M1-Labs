tags: #python #docs  
see also: [operations](operations) | [naming conventions](Conventions#Naming)

---

# Variables and Datatypes

## Defining

```python
my_first_variable = "value"
my_second_variable: str
my_third_variable: str = "value"
```

## Available types

### Numeric

```python
my_integer: int = 0
my_real: float = 0.0
```

### Boolean

```python
my_boolean: bool = True
```

### String

```python
my_string_double_quotes: str = ""
my_string_single_quotes: str = ''
```

### None

This datatype exists to avoid `null`:

```python
my_none: None = None
```

## Assigning

When applying operations to a variable, you can shorten

```
variable = variable <operator> operand
```

to

```
variable <operator>= operand
```

e.g.

```python
number += 1 # Same as number = number + 1
number -= 273
number /= 5
number *= 10
```

## Changing types

Dynamic typing allows us to do the follwing:

```python
my_integer = "Ha! fooled you!"
my_real = False
my_boolean = 6.9
```

To change the way an existing value is stored:

```python
my_string = str(my_real)
my_integer = int("345") # Note: int() will floor the value
my_boolean = bool(0)
my_real = float("12.34")
```

## Check Type

```python
print(type(my_variable))
```