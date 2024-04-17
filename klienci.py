from connection import connect_to_db

def get_clients():
    conn = connect_to_db()
    cur = conn.cursor()
    query = "select * from clients"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_clients(id_clients):
    name = input("""
        Podaj imię klienta:
        """)
    surname = input("""
        Podaj nazwisko:
        """)
    query = f"""
    Update clients
    set name = '{name}',
        surname = '{surname}'
    WHERE id = {id_clients}
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()