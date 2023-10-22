######################
# INPUTS AND OUTPUTS #
# -----27-09-23----- #
######################

def Task1():
    name = input("What's your name?\n")
    salary = input("What's your salary?\n£")
    print(name.capitalize(), ": £", salary, sep="")

def Task2():
    name = input("Hi, what's your name?\n")
    print("'", name, "'", sep="")

def Task3():
    # The value of a variable can change during runtime.
    number = input("Enter number: ")
    print("Your number is", number)
    number = input("Enter another number: ")
    print("Your number is", number)

def Task4():
    # Dynamic Typing: a variable can hold different types of value.
    variable = 4
    variable = "pasta"
    variable = True

##############
# Data types #
##############

def Task5():
    # Strings
    # Defining
    singleQuote = 'single'
    orDoubleQuote = "double"
    multilineString = '''This is a string
over multiple
lines'''

    # Functions
    print(type(multilineString))
    print(multilineString)
    len(multilineString)
    message = "Have you" + " had lunch?"
    print("Are you " + singleQuote + "?")

    # Characters
    hello = "hello"
    firstLetter = hello[0]
    lastLetter = hello[len(hello) - 1]

    # Substrings
    print(hello[2:3]) # Get characters 2 to 3.
    print(hello[:1]) # The start of the string is assumed.
    print(hello[3:]) # The end of the string is assumed.
    # The second bound (y in [x:y]) is EXCLUSIVE.

    # Split
    sentence = "sentence: The quick brown fox jumped over the lazy dog."
    words = sentence.split() # Default split character = space
    sections = sentence.split(':')

def Task6():
    # Integers
    number = input("Enter number between 1 and 100") # Input is always a string.
    print("Type:", type(number)) # str
    number = int(number) # Convert
    print("Type:", type(number)) # int

def Task7():
    # Floating point numbers
    pi = 3.141592653589793
    print(type(pi))

    # Convert int to float
    x = 3
    print(x, type(x))
    floatX = float(x)
    print(floatX, type(floatX))

    # Convert string to float
    string1 = '4.5'
    float1 = float(string1)
    print(float1, type(float1))
    string2 = '10000000000'
    float2 = float(string2)
    print(float2, type(float2))

def Task8():
    # Complex Number
    complexNumber = 3 + 4j # j is the engineering symbol for imaginary numbers.
    print(complexNumber)
    print(complexNumber.real) # Get real part
    print(complexNumber.imag) # Get imaginary part
    print(type(complexNumber))

def Task9():
    # Boolean
    t = True
    f = False
    print(type(t))

def Task10():
    # None Value
    # Python has a special type: the NoneType
    value = None
    print(value, type(value))
    # Null creates issues for garbage collection, which is why the NoneType exists.

Task10()