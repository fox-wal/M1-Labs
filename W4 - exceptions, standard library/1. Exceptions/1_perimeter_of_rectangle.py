def print_perimeter(width, height):
    '''
    Calculates and prints the perimiter of a rectangle with the given width and height.

    Args:
      - width (positive integer): width of the rectangle
      - height (positive integer): height of the rectangle

    Exceptions:
      - TypeError (if the width and/or height is not an integer)
      - ValueError (if the width and/or height is not positive)
    '''
    TYPE_ERROR_MSG = "Width and height should be positive integers."
    VALUE_ERROR_MSG = "Width and height should be positive integers.\nYou entered the values:\nwidth: {}\nheight: {}".format(width, height)

    # Check type
    if not ((str(width).isnumeric() and (len(str(width)) > 0))
    and (str(height).isnumeric() and (len(str(height)) > 0))):
        raise TypeError(TYPE_ERROR_MSG)
    
    # Convert to int
    width = int(width)
    height = int(height)

    # Check value
    if (width <= 0) or (height <= 0):
        raise ValueError(VALUE_ERROR_MSG)
    
    # Output result
    print("perimeter:", 2 * (width + height))

width = input("width: ")
height = input("height: ")
try:
    print_perimeter(width, height)
except TypeError or ValueError as e:
    print(e)
finally:
    print("End of program.")