from random import random, randint

class Account():
    """
    Stores details of a bank account including its balance.
    """

    def __init__(self, account_number: int, account_holder_name: str, opening_balance: float, account_type: str):
        """
        Args:
            account_number: Unique 8-digit number which identifies your bank account.
            account_holder_name: The name on your account.
            opening_balance: The initial balance (in pence) in your account.
            account_type: The type of your account i.e. current, savings, etc.
        """
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = opening_balance
        self._account_type = account_type

    def __str__(self):
        TEMPLATE = "Account number: {number:0>8d}\nAccount holder: {name}\nBalance: £{balance:.2f}\nAccount type: {type}"
        return TEMPLATE.format(number  = self._account_number,
                               name    = self._account_holder_name,
                               balance = self._balance,
                               type    = self._account_type)

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        
        if self._balance < amount:
            raise ValueError("Insufficient account balance.".format(self._balance))
        
        self._balance -= round(amount, 2)

    @property
    def get_balance(self) -> float:
        return round(self._balance, 2)

    @get_balance.setter
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        self._balance += round(amount, 2)
    
    def test(self, deposit_amount: float, withdraw_amount: float) -> bool:
        """
        Returns:
            False if any of the tests caused an exception.
            True otherwise.
        """

        try:
            print("String representation:", str(self))
            self.deposit(deposit_amount)
            self.withdraw(withdraw_amount)
            print("Balance: £{:.2f}".format(self.get_balance()))
        except:
            return False
        else:
            return True

class SavingsAccount(Account):
    """
    Contains details about a savings account as well as the Annual Interest Rate for all savings accounts.
    """
    
    annual_interest_rate = 1

    def __init__(self, account_number: int, account_holder_name: str, opening_balance: float):
        """
        Args:
            account_number: Unique 8-digit number which identifies your bank account.
            account_holder_name: The name on your account.
            opening_balance: The initial balance (in pence) in your account.
            account_type: The type of your account i.e. current, savings, etc.
        """

        super().__init__(account_number, account_holder_name, opening_balance, "Savings Account")

    def update_interest(new_rate: float):
        """
        Args:
            new_rate: a decimal number, such that 1 <= number < 2, stipulating the new annual interest rate.
        """

        if new_rate <= 0:
            raise ValueError("Rate must be positive.")
        SavingsAccount.annual_interest_rate = new_rate

    def calculate_monthly_interest(self):
        NUMBER_OF_PAY_PERIODS = 12
        self._savings_balance *= 1 + (SavingsAccount.annual_interest_rate - 1) / NUMBER_OF_PAY_PERIODS
    
    def test(self):
        print("String:", str(self))
        print("Doctsring:", self.__doc__)
        print("Current Annual Interest Rate:", SavingsAccount.annual_interest_rate)
        SavingsAccount.update_interest(random() + 1)
        print("New Annual Interest Rate:", SavingsAccount.annual_interest_rate)
        self.calculate_monthly_interest()
        print("Balance sfter monthly interest rate: £{:.2f}".format(self._savings_balance))

# my_account = Account(random() * 10**7, "Fox Walczak", random() * 200 + random(), "Current account")
# print("Test successful:", my_account.test(2, 3))
my_savings_account = SavingsAccount(randint(0, 99999999), "Fox Walczak", randint(3, 500) + random())
my_savings_account.test()
