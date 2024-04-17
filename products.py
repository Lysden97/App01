from connection import connect_to_db

def get_products():
    conn = connect_to_db()
    cur = conn.cursor()
    query = "Select * from products"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
