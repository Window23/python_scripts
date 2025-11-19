""" (Tuples Representing Invoices) When you purchase products or services from a company,
    you typically receive an invoice listing what you purchased and the total amount of money due.
    Use tuples to represent hardware store invoices that consist of four pieces of data—a part ID string,
    a part description string, an integer quantity of the item being purchased and, for simplicity, a float item price (in general, Decimal should be used for monetary amounts).
    Use the sample hardware data shown in the following table."""

how_many_items = int(input("How many items would you like to purchase? "))

def item_description(arg):
    items = []
    for item in range(1, arg + 1):
        part_number = int(input(f"Part number for the item number {item}  is: "))
        part_description = str(input(f"Part description for the item number {item}  is: "))
        quantity = int(input(f"Quantity for the item number {item}  is: "))
        price = float(input(f"Price for the item number {item}  is: "))
        items.append((part_number, part_description, quantity, price))
    items = tuple(items)
    return items

a = item_description(how_many_items)

print(f"Part number  Part description  Quantity  Price")
for item in a:
    part_number, part_description, quantity, price = item
    print(f"{part_number:<13}{part_description:<18}{quantity:<10}{price:<5.2f}")






