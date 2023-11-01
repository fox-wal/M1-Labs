# Encapsulation

In Python, there are no actual access restrictions. There are just naming conventions that act as indicators for programmers.

public: can be accessed from anywhere.

private/protected: should be accessed by getters and setters.

## Levels of access

### Define

Define the variables in the constructor as normal.

```python
class MyClass():
	def __init__(self):
		my_public_variable = 0
		_my_protected_variable = 1
		___my_private_variable = 2
```

### Access

Create an accessor method.

```python	
	@property
	def get_my_private_variable(self):
		return self.__my_private_variable
```

Call it

```python
print(instance.get_my_private_variable)
```

### Change

Create a setter method.

```python
	@get_my_private_variable.setter
	def set_my_private_variable(self, new_value):
		return self.__my_private_variable = new_value
```

Use it like a variable or call it.

```python
instance.set_my_private_variable = 3
instance.set_my_private_variable(4)
```
