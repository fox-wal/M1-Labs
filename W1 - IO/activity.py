# Python as a Calculator
# Task 1
print(13//2)
print(13%2)
print(1-0.99)
print(7.5**2)

# Task 2
hours = float(input('Hours [float, 0-24]: '))
minutes = hours * 60
print("Time in minutes:", minutes)

# Task 3:
print("Enter how much you spend on each of these every month:")
rent = float(input('rent: £'))
transport = float(input('transport: £'))
groceries = float(input('groceries: £'))
eatingOut = float(input('eating out: £'))

total = rent + transport + groceries + eatingOut
print('Total: £', total.__round__(2), sep="")

# String Operations
# Task 1
weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, with plenty of winter sunshine developing. However, patchy cloud and isolated showers may move in from the west later in the afternoon."
# 1. Split
lines = weather.split('\n')
words = weather.split(' ')
phrases = weather.split(',')
sentences = weather.split('.')
# 2. Length
print(len(weather))
# 3. Lowercase
weatherLowerCase = weather.lower()
# 4. Sunshine
if weatherLowerCase.find("sunshine") != -1:
    print("There will be sunshine on Friday.")
else:
    print("There will not be sunshine on Friday.")