# Inheritance

## Constructor of subclass

```python
class Shape:
	def __init__(self, colour):
		self._colour = colour
	

class Circle(Shape):
	def __init__(self, colour, radius):
		super().__init__(colour)
		self._radius = radius
```

All public and protected attributes and methods are inherited.