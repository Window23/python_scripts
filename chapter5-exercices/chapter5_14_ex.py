""" Perform the following tasks on a list of invoice tuples:
    Use function sorted with a key argument to sort the tuples by part description, then display the results.
    To specify the element of the tuple that should be used for sorting, first import the itemgetter function from the operator module as in

    from operator import itemgetter

    Then, for sorted’s key argument specify itemgetter( index ) where index specifies which element of the tuple should be used for sorting purposes.
    Use the sorted function with a key argument to sort the tuples by price, then display the results.
    Map each invoice tuple to a tuple containing the part description and quantity, sort the results by quantity, then display the results.
    Map each invoice tuple to a tuple containing the part description and the value of the invoice (the product of the quantity and the item price), sort the results by the invoice value, then display the results.
    Modify Part (d) to filter the results to invoice values in the range $200 to $500.
    Calculate the total of all the invoices. """

from operator import itemgetter


def sorted_key(arg):
    items = []
    for item in range(1, arg + 1):
        (part_number, part_description, quantity, price) = (int(input(f"Part number for the item number {item} is: ")),
                                                            str(input(f"Part description for the item {item} is ")),
                                                            int(input(f"Quantity for the item number {item} is: ")),
                                                            float(input(f"Price for the item number {item} is: ")))
        items.append((part_number, part_description, quantity, price))
    return items

def choice_key():
    key_choice = str(input("Which item would you like to sort by?")).lower()
    if key_choice == 'part number':
        b = sorted(sorted_key(how_many_items), key=itemgetter(0))
    elif key_choice == 'part description':
        b = sorted(sorted_key(how_many_items), key=itemgetter(1))
    elif key_choice == 'quantity':
        b = sorted(sorted_key(how_many_items), key=itemgetter(2))
    elif key_choice == 'price':
        b = sorted(sorted_key(how_many_items), key=itemgetter(3))
    return b

def printing_result():
    a = sorted_key(how_many_items)
    print(f"Part number  Part description  Quantity  Price")
    for item in a:
        part_number, part_description, quantity, price = item
        print(f"{part_number:<13}{part_description:<18}{quantity:<10}{price:<5.2f}")
    return

how_many_items = int(input("How many items would you like to purchase? "))



printing_result()

