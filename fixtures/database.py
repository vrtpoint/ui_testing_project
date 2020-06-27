import mysql.connector


def data_base_query(sql_query):
    try:
        connection = mysql.connector.connect(
            user='root',
            password='password',
            host='localhost',
            port='3306',
            database='bitnami_opencart')
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()

        return result

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))