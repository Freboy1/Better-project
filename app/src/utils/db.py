import pymysql
from app.src.utils.config import host, user, password, db_name

def wrong_correct(query, password2):
    if query == user and password == password2:
        return True
    return False

def data_return():
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            show_table = "SELECT * FROM actor"
            cursor.execute(show_table)
            l = list()
            rows = cursor.fetchall()
            for row in rows:
                l.append(row)

            return l
    finally:
        connection.close()

def find_id_user(id):
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            show_table = f"SELECT * FROM actor where {id} = actor_id"
            cursor.execute(show_table)
            l = list()
            rows = cursor.fetchall()
            for row in rows:
                l.append(row)

            return l
    finally:
        connection.close()