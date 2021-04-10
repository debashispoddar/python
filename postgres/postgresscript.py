import psycopg2
"""
Create a new database connection.

    The connection parameters can be specified as a string:

        conn = psycopg2.connect("dbname=test user=postgres password=secret")

    or using a set of keyword arguments:

        conn = psycopg2.connect(database="test", user="postgres", password="secret")

    Or as a mix of both. The basic connection parameters are:

    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)
"""
def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432' ")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432' ")
    cur= conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('debashis', 1, 5)")
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')"  % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)" , (item, quantity, price))
    conn.commit()
    conn.close()
    
create_table()
insert('Water Glass2',10,10.5)
insert("Coffee Glass3",20,15.5)

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432' ")
    cur= conn.cursor()
    cur.execute("select * from store ")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
    