class SavingsAccount:
    """
    This is a class that represents a savings account
    """
    _annual_interest_rate = 4.3

    def __init__(self,account_number:int,account_holder:str,account_type:str,opening_balance:float=10):
        self._number = account_number
        self._holder = account_holder
        self._type = account_type
        self._savings_balance = opening_balance

    def update_interest_rate(self,new_rate:float)->None:
        if new_rate < 0:
            raise ValueError("Interest rate must be positive")
        else:
            self._annual_interest_rate = new_rate

    def calculate_monthly_interest(self)->None:
        self._savings_balance += self._savings_balance*(self._annual_interest_rate/12)

    def get_balance(self):
        return self._savings_balance

    def __str__(self):
        return f"Account information:\nHolder: {self._holder}, number: {self._number}, balance: {self._savings_balance}"
