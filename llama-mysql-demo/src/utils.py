def connect_to_database(host='localhost', user='root', password='!23', dbname='test_db'):
    import pymysql

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname
    )
    return connection

def execute_query(connection, query, data=None):
    with connection.cursor() as cursor:
        cursor.execute(query, data)
        connection.commit()

def fetch_all(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def close_connection(connection):
    connection.close()