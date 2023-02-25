import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="bank",
        user=os.environ['yoni'],
        password=os.environ['yoni123'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS bankusers;')
cur.execute('CREATE TABLE bankusers (id serial PRIMARY KEY,'
                                 'username text (150) NOT NULL,'
                                 'password text (50) NOT NULL,'
                                 'email text NOT NULL,'
                                 )

# Insert data into the table

cur.execute('INSERT INTO bankusers (username, password, email)'
            'VALUES (%s, %s, %s)',
            ('icewizzard',
             'ak47hh',
             'yoni@gmail.com')
            )

conn.commit()

cur.close()
conn.close()
#להסתכל באינרנט מה ששמרתי

#https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91 sqlalchemy
#https://www.w3schools.com/python/pandas/default.asp pandas toutrial