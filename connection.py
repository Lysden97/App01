from psycopg2 import connect

settings = {
    'host': 'localhost',
    'database': 'exercises_db',
    'user': 'postgres',
    'password': 'coderslab',
    'port': '5432'
}

def connect_to_db():
    connection = connect(**settings)
    return connection