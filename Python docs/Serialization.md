# Serialization

> Serialization is the process of converting complex data structures or program states into a format that can be easily stored, transmitted, and later reconstructed. [Source](https://now.ntu.ac.uk/d2l/le/content/981892/viewContent/12196643/View)

## Uses:

- Saving / loading the entire program state between runs.

## Pickle

This is a commonly used module for Python.

Example:

```python
import pickle

def save_state(filename, state):
    with open(filename, 'wb') as file:
        pickle.dump(state, file)

def load_state(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Your program logic and state
program_state = {
    'variable1': 42,
    'list_data': [1, 2, 3],
    'object_instance': SomeCustomClass(),
    # Add more program state as needed
}

# Save the program state to a file
save_state('program_state.pkl', program_state)

# ... program execution ...

# Load the program state from the file during the next run
loaded_state = load_state('program_state.pkl')

# Now 'loaded_state' contains the state saved during the previous run
```

> Convenient way to maintain the continuity of your program's state across different runs, facilitating tasks such as resuming complex computations or preserving user preferences.

### WARNING

> When loading serialized data, especially if it comes from untrusted sources, as pickle can execute arbitrary code during deserialization. If security is a concern, alternative serialization formats like JSON might be considered.


## Further Reading

[Python docs](https://docs.python.org/3/library/pickle.html)
[Tutorialspoint](https://www.tutorialspoint.com/object_oriented_python/object_oriented_python_serialization.htm)
