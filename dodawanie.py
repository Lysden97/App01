from connection import connect_to_db

first_name = input("""
Podaj imie:
""")
last_name = input("""
Podaj nazwisko:
""")

query = f"INSERT INTO clients (name, surname) VALUES ('{first_name}','{last_name}')"
connection = connect_to_db()
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()


