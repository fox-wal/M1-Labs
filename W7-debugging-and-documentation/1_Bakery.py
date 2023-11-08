from datetime import date
class Invoice:
    '''
    This is a class that keeps information of the Bakery's invoices.
    '''
    def __init__(self,type:str,quantity:int,price_per_item:float,delivery_date:date):
        self.type = type
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.delivery_date = delivery_date

    def get_invoice(self):
        return self.quantity*self.price_per_item

    @property
    def get_quantity(self)->int:
        return self.quantity

    @get_quantity.setter
    def update_quantity(self,new_quantity:int):
        if new_quantity >0:
            self.quantity = new_quantity
        else:
            raise ValueError("New quantity must be positive")
    @property
    def get_item(self)->str:
        return self.type

    def __str__(self):
        return (f"This is an order of {self.quantity} {self.type} to be delivered {self.delivery_date}")

# this is a test function
def invoice_test():
    invoice_2 = Invoice("sourdough boule",75,2,date(2023,2,15).strftime("%d/%m/%y"))
    print ("This order will amount to: ", invoice_2.get_invoice())

    invoice_2.update_quantity = 70
    print(invoice_2)
    print ("The item that has been ordered is: ",invoice_2.get_item)

invoice_test()
