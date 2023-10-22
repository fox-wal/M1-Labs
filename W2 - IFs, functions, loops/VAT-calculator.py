#
# This program calculates the final price of an imported item.
#

def calculate_import_VAT(price: float, is_document: bool):
    if is_document:
        return price
    else:
        return price * 1.2

price = float(input("Please enter the price of your item: £"))
is_document = input("Is your item a book or magazine? (yes/no) ")

final_price = calculate_import_VAT(price, is_document.lower() == "yes")

print("Final price: £%.2f" % final_price)