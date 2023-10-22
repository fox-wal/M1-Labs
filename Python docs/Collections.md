tags: #python #docs 

---
# Collections

## List

```python
#             Index:  0  1  2  3  4
my_list: list[int] = [1, 2, 3, 5, 7]

.append(item)
.remove(item)
[1:4] # --> [2, 3, 5]
[3:] # --> [5, 7]
[:3] # --> [1, 2, 3]

my_list = [0]*5 # --> [0, 0, 0, 0, 0]
```

- Ordered.

To make a 2D list, you must nest lists.

## Set

```Python
my_set: set[int] = {1, 2, 3, 5, 7}

.add(element)
.update(multiple_elements)
.discard(element)
.clear()
```

- Cannot repeat values.
    - If converting from a list to a set, duplicates will be removed.
- Cannot nest sets.
- Unordered --> won't retain the order you define it with.

## Dictionary

```python
my_dictionary: dict[str, int] = {
    "key 1" : 0,
    "key 2" : 1
}

my_dictionary["key 3"] = 2
```

- #tips Can use it to store attributes of something (instead of using a class).
- Ordered, but accessed via the key.

## Tuple

```python
my_tuple: tuple[str, int, str] = ("My name is Sandy I'm", 14, "years old")
```

- Cannot change the contents of a tuple. It is read-only.
- Ordered.
- Can use it to swap values:
    ```python
    var1, var2 = (var2, var1)
    ```
