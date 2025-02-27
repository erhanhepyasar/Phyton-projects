import psycopg2

connstr = "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'"

def create_table():
    conn=psycopg2.connect(connstr)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect(connstr)
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item, quantity, price))  # Prone to sql injections
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect(connstr)
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect(connstr)
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=psycopg2.connect(connstr)
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

#create_table()
#insert("Banana", 6, 7)
print(view())
#delete("Orange")
#print(view())
update(14, 77, "Apple")
print(view())