# Tax bands
income = int(input('Enter Annual Taxable Income: £'))

BASIC_UPPER_LIMIT = 37700
HIGHER_UPPER_LIMIT = 125140

BASIC_RATE = 0.2
HIGHER_RATE = 0.4
ADDITIONAL_RATE = 0.45

tax = 0

# Basic: Under 37,700
if income <= BASIC_UPPER_LIMIT:
    tax = income * BASIC_RATE

# Higher: 37,700 to 125,140
elif income <= HIGHER_UPPER_LIMIT:
    tax = BASIC_UPPER_LIMIT * BASIC_RATE # Basic
    + (income - BASIC_UPPER_LIMIT) * HIGHER_RATE # Higher

# Additional: Over 125,140
else:
    tax = BASIC_UPPER_LIMIT * BASIC_RATE # Basic
    + (HIGHER_UPPER_LIMIT - BASIC_UPPER_LIMIT) * HIGHER_RATE # Higher
    + (income - HIGHER_UPPER_LIMIT) * ADDITIONAL_RATE # Additional

# Output
print('Tax:', tax.__round__(2))
print('Income after tax:', (income - tax).__round__(2))