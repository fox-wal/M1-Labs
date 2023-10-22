###################
# Week 1: variables
###################

# Hours to minutes
hours = float(input("Please give the time in hours"))
print("The time in minutes is %d :" % (hours*60))

# Student expenses
rent = int(input("Rent: "))
transport = float(input("Transport: "))
groceries = float(input("Groceries: "))
eating_out = float(input("Eating out etc: "))
total = rent+transport+groceries+eating_out
print("Total expenses: %.2f" % total)

# String operations
weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, " \
         "with plenty of winter sunshine developing. " \
         "However, patchy cloud and isolated showers may move in from the west later in the afternoon."
new_line = weather.split("\n")
print(new_line)
space = weather.split()
print(space)
comma = weather.split(",")
print(comma)
full_stop = weather.split(".")
print(full_stop)
print("Length: ",len(weather))
weather_lc = weather.lower()
print(weather_lc)

if weather.find("sunshine") == -1 and weather.find("sunny") == -1:
    print("Tomorrow will not be sunny :(")
else:
    print("Tomorrow will be sunny :) ")
