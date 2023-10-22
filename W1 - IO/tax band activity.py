# Tax bands
income = int(input('Enter Annual Taxable Income: £'))

BASIC_UPPER_LIMIT = 37700
HIGHER_UPPER_LIMIT = 125140

BASIC_RATE = 0.2
HIGHER_RATE = 0.4
ADDITIONAL_RATE = 0.45

tax = 0

# Under 37,700
if income <= BASIC_UPPER_LIMIT:
    tax = income * BASIC_RATE
else:
    tax = BASIC_UPPER_LIMIT * BASIC_RATE

# 37,700 to 125,140
if income <= HIGHER_UPPER_LIMIT:
    tax += (income - BASIC_UPPER_LIMIT) * HIGHER_RATE
else:
    tax += (HIGHER_UPPER_LIMIT - BASIC_UPPER_LIMIT) * HIGHER_RATE

# Over 125,140
if income > HIGHER_UPPER_LIMIT:
    tax += (income - HIGHER_UPPER_LIMIT) * ADDITIONAL_RATE

print('Tax:', tax.__round__(2))
print('Income after tax:', (income - tax).__round__(2))

# Feedback: - don't use 37_700 --> doesn't work in Python
#           - use one if statament with multiple elifs