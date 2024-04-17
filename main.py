from klienci import get_clients, update_clients
from products import get_products
from zamówienia import get_orders, update_orders
from dodaj_produkt import add_product, update_product

interface = """
1 - Wyświetl produkty
2 - Wyświetl klientów
3 - Wyświetl zamówienia
4 - Wyjście

5 - Dodaj produkt
6 - Modyfikacja produktu
7 - Modyfikacja klienta
8 - Modyfikacja zamówienia
"""


while True:
    user_input = input(interface)
    if user_input == "1":
        products = get_products()
        for product in products:
            print(product)
    elif user_input == "2":
        if user_input == "2":
            clients = get_clients()
            for client in clients:
                print(client)
    elif user_input == "3":
        if user_input == "3":
            orders = get_orders()
            for order in orders:
                print(order)
    elif user_input == "4":
        break
    elif user_input == "5":
        if user_input == "5":
            add_product = add_product()
    elif user_input == "6":
        id_product = input("Podaj id produktu do modyfikacji:\n")
        update_product(id_product)
    elif user_input == "7":
        if user_input == "7":
            id_clients = input("Podaj id klienta do modyfikacji:\n")
            update_clients(id_clients)
    elif user_input == "8":
        if user_input == "8":
            id_orders = input("Podaj id zamówienia do modyfikacji:\n")
            update_orders(id_orders)

