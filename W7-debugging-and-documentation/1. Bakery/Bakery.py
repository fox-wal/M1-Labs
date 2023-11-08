from datetime import date
class Invoice:
    """
    This is a class that keeps information of the Bakery's invoices.
    """
    def __init__(self, type:str, quantity:int, price_per_item:float, delivery_date:date):
        self.type = type
        self.update_quantity(quantity)
        self.__set_price_per_item = price_per_item
        self.delivery_date = delivery_date

    def get_invoice(self):
        return round(self.quantity * self.price_per_item, 2)

    @property
    def get_quantity(self) -> int:
        return self.quantity

    @get_quantity.setter
    def update_quantity(self, new_quantity:int):
        if new_quantity > 0:
            self.quantity = new_quantity
        else:
            raise ValueError("New quantity must be positive")
    @property
    def get_item(self) -> str:
        return self.type

    @property
    def get_price_per_item(self) -> float:
        return self.price_per_item
    
    @get_price_per_item.setter
    def __set_price_per_item(self, new_price):
        if new_price <= 0:
            raise ValueError("Price must not be negative.")
        self.price_per_item = new_price

    def __str__(self):
        return (f"This is an order of {self.quantity} {self.type} to be delivered {self.delivery_date}")

# ---

"""
Improvement log:

Problem: Although the quantity setter prevents the user from setting the quantity to a non-positive number, this is not the case in the constructor.
Type: Semantic Error
Changes:
    Line 8:
        - self.quantity = quanity
        + self.update_quantity(quantity)

Problem: The price per item can be negative.
Type: Semantic Error
Changes:
    Line 9:
        - self.price_per_item = price_per_item
        + self.__set_price_per_item = price_per_item
    Lines 29 - 37:
        + @property
        + def get_price_per_item(self) -> float:
        +     return self.price_per_item
        + 
        + @get_price_per_item.setter
        + def __set_price_per_item(self, new_price):
        +     if new_price <= 0:
        +         raise ValueError("Price must not be negative.")
        +     self.price_per_item = new_price

Problem: The invoice will be too precise.
Type: Semantic Error
Changes:
    Line 13:
        - return self.quantity * self.price_per_item
        + return round(self.quantity * self.price_per_item, 2)
"""

# this is a test function
def invoice_test():
    invoice_2 = Invoice("sourdough boule", 75, 2, date(2023,2,15).strftime("%d/%m/%y"))
    print ("This order will amount to: ", invoice_2.get_invoice())

    invoice_2.update_quantity = 70
    print(invoice_2)
    print ("The item that has been ordered is: ", invoice_2.get_item)

invoice_test()
