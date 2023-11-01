# Classes

## Methods

Must pass `self` as a parameter.

### Constructor

```python
class Pet():
	
	def __init__(self, height, owner):
		self.height = height
		self.owner = owner
```

```python
my_pet = Pet(64, "Fox")

print("owner:", my_pet.owner)
print(type(my_pet))
```

```output
owner: Fox
<class '__main__.Pet'>
```

### Default String Representation

```python
def __str__(self):
	return "Owner is: " + self.owner + "\nHeight is: " + str(self.height)

print(my_pet)
```

```output
Owner is: Fox
Height is: 64
```

## Docstrings

You can use docstrings in classes as well:

```python
class Pet():
	"""
	A class to store information regarding pets.
	"""

my_pet = Pet()
print(my_pet.__doc__)
```

```output
A class to store information regarding pets.
```

## Other

- Variables in a class are called attributes.
- Set attributes in constructor.
- Minimise access to attributes.
- Provide string representations.
