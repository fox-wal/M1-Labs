class Account:
    def __init__(self,account_number:int,account_holder:str,account_type:str,opening_balance:float=10):
        self._number = account_number
        self._holder = account_holder
        self._type = account_type
        self._balance = opening_balance

    def deposit(self,amount:float)->None:
        self._balance +=amount

    def withdraw(self,amount:float)->None:
        if amount>self._balance:
            raise ValueError(f"Insufficient funds. Cannot withdraw {amount}")
        elif amount<0:
            raise ValueError(f"Cannot withdraw {amount}")
        else:
            self._balance -= amount

    def get_balance(self)->float:
        return self._balance

    def __str__(self):
        return f"Account information:\nHolder: {self._holder}, number: {self._number}, balance: {self._balance}"
