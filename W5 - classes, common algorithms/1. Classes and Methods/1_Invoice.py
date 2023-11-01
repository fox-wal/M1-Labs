from datetime import date

class Invoice:
    """
    Attributes:
        item_type: Type of item to be delivered.
        item_quantity: Amount of item to be delivered.
        item_price: Price of each item.
        delivery_date: Expected date that the order should be delivered.
    """
    
    def __init__(self, item_type: str, item_quantity: int, item_price: int, delivery_date: date):
        self.item_type = item_type
        self.item_quantity = item_quantity
        self.item_price = item_price
        self.delivery_date = delivery_date
    
    def __str__(self) -> str:
        TEMPLATE: str = "Item type: {}\nItem quantity: {}\nItem price: {}\nDelivery date: {}"
        return TEMPLATE.format(self.item_type, self.item_quantity, self.item_price, self.delivery_date)
    
    def get_invoice(self) -> float:
        return self.item_quantity * self.item_price / 100
    
    def update_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        self.item_quantity = quantity

    def get_quantity(self) -> int:
        return self.item_quantity
    
    def get_item(self) -> str:
        return self.item_type

    def invoice_test(self):
        print("Tests:")
        print("Default string representation: ", str(self))
        print("Get invoice:", self.get_invoice())
        print("Get/Update quantity: initial = {}, updated = {}".format(self.get_quantity(), self.update_quantity(50)))
