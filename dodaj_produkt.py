from connection import connect_to_db


def add_product():
    produkt = input("""
    Podaj nazwę produktu:
    """)
    opis = input("""
    Podaj opis produktu:
    """)
    cena = input("""
    Podaj cenę produktu:
    """)
    ocena = input("""
    Podaj ocenę produktu:
    """)

    query = f"INSERT INTO products (name, description, price, ratings) VALUES ('{produkt}','{opis}',{cena},{ocena})"
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def update_product(id_product):
    produkt = input("""
        Podaj nazwę produktu:
        """)
    opis = input("""
        Podaj opis produktu:
        """)
    cena = input("""
        Podaj cenę produktu:
        """)
    ocena = input("""
        Podaj ocenę produktu:
        """)
    query = f"""
    Update products
    set name = '{produkt}',
        description = '{opis}',
        price = {cena},
        ratings = {ocena}
    WHERE id = {id_product}
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

