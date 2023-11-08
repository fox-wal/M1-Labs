import Account
class SavingsAccount(Account):
    """
    This is a class that represents a savings account
    """
    _annual_interest_rate = 4.3

    def __init__(self,account_number:int,account_holder:str,account_type:str,opening_balance:float=10):
        super().__init__(account_number, account_holder, account_type, opening_balance)

    def update_interest_rate(self,new_rate:float)->None:
        if new_rate < 0:
            raise ValueError("Interest rate must be positive")
        else:
            self._annual_interest_rate = new_rate

    def calculate_monthly_interest(self)->None:
        self._balance += self._balance*(self._annual_interest_rate/12)
