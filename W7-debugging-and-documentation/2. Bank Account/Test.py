import Account
import SavingsAccount

# Test 1

standard1 = Account(101010,"John Doe","standard",200)
standard1.deposit(500)
standard1.withdraw(400)
print("New balance",standard1.get_balance())
print(standard1)

# Test 2

saver1 = SavingsAccount(232345, "Robin Hood","Easy Saver",35000)
saver2 = SavingsAccount(543232, "Snow White","Easy Saver", 1000)

saver1.calculate_monthly_interest()
saver2.calculate_monthly_interest()
print("Saver account 1: %.2f" % saver1.get_balance())
print("Saver account 2: %.2f" % saver2.get_balance())

# update interest rate
saver1.update_interest_rate(4.8)
saver2.update_interest_rate(4.8)

# next month's balances
saver1.calculate_monthly_interest()
saver2.calculate_monthly_interest()
print("Saver account 1: %.2f" % saver1.get_balance())
print("Saver account 2: %.2f" % saver2.get_balance())
