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
        self._item_type = item_type
        self._item_quantity = item_quantity
        self._item_price = item_price
        self._delivery_date = delivery_date
    
    def __str__(self) -> str:
        TEMPLATE: str = "Item type: {}\nItem quantity: {}\nItem price: {}\nDelivery date: {}"
        return TEMPLATE.format(self._item_type, self._item_quantity, self._item_price, self._delivery_date)
    
    def get_invoice(self) -> float:
        return self._item_quantity * self._item_price / 100
    
    @property
    def get_quantity(self) -> int:
        return self._item_quantity
    
    @get_quantity.setter
    def update_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        self._item_quantity = quantity

    @property
    def get_item(self) -> str:
        return self._item_type

    def invoice_test(self):
        print("Tests:")
        print("Default string representation: ", str(self))
        print("Get invoice:", self.get_invoice())
        print("Get/Update quantity: initial = {}".format(self._quantity))
        self.update_quantity(50)
        print("                     updated = {}".format(self._quantity))
