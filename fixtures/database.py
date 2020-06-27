import mysql.connector
from decouple import config


def data_base_query(sql_query):
    try:
        connection = mysql.connector.connect(
            user=config('user'),
            password=config('password'),
            host=config('host'),
            port=config('port'),
            database=config('database'))
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()

        return result

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))