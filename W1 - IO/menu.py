menu = {
    # Sides
    'Garlic bread' : 3.99,
    'Chips' : 2.99,

    # Mains
    'Pizza' : 14.99,
    'Tacos' : 7.99,
    'Chicken wings' : 5.99,
    'Corn dog' : 3.49,

    # Desserts
    'Ice cream' : 2.85,

    # Drinks
    'Milkshake' : 3.35,
    'Water' : 0,
    'Wine' : 7.88,
    'Beer' : 7.63,
    'Soft drink' : 2.29
}

amount = None
total = 0

print('Enter the amount of each item that you want.')

for item in menu:
    print(f'{item}: £{menu[item]}')

for item in menu:
    amount = int(input(item + ': '))
    total += menu[item] * amount

print('Total: £' + str(total))