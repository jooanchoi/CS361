import mariadb
import sys

from repair_app.db_credentials import host, user, password, db

def connect_to_db(host = host, user = user, password = password, db = db):
    db_connection = mariadb.connect
    return db_connection

def execute(db_connection = None, query = None, query_params = ()):
    if db_connection is None:
        print("No db object found")
        return None

    if query is None or len(query.strip()) == 0:
        print("No SQL query")
        return None

    cursor = db_connection.cursor()
    cursor.execute(query, query_params)
    db_connection.commit()
    return cursor