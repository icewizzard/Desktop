import os
import psycopg2
from classes import User, Banker, Manger



try:
    connection = psycopg2.connect(host="localhost",
                                  database="bank",
                                  user=os.environ['yoni'],
                                  password=os.environ['yoni123'])

    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO bank (username, password, email) VALUES (%s,%s,%s)"""
    record_to_insert = (5, 'One Plus 6', 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
