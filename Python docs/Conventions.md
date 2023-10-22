tags: #python #tips #docs #conventions

---
# Conventions

## Naming

```python
class MyClass:
    ___my_private_field
    _my_protected_field
    my_public_field

    def my_method():
        pass

def my_function(my_parameter: object = "default")
    pass

MY_CONSTANT = 0
my_variable = 0
my_items: list = []
```

## Other

- Leave at least one blank line after each class and function.
- Try to put comments on their own line.
- Docstrings:
    ```python
    def my_function(my_parameter: type):
        '''
        My docstring.
        
        Args:
            my_parameter: My parameter.
        
        Returns:
            Return value if this.
            Some other value otherwise.
        
        Exceptions:
            MyError is raised if this.
        '''
    ```
- 