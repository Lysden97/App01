from connection import connect_to_db


def get_orders():
    conn = connect_to_db()
    cur = conn.cursor()
    query = "SELECT * FROM orders"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def update_orders(id_orders):
    description = input("""
        Podaj opis zamówienia:
        """)
    query = f"""
    Update orders
    set description = '{description}'
    WHERE id = {id_orders}
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
