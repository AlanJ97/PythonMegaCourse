import psycopg2 


def crate_table():
    conn = psycopg2.connect("dbname='mydatabase' user='alan' password='123456' host= 'localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS store(
            item TEXT,
            quantity INTEGER,
            price REAL
        )"""
    )
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='mydatabase' user='alan' password='123456' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO store VALUES(
            %s,
            %s,
            %s
    )""",(item, quantity, price)
    )
    conn.commit()
    conn.close()

#insert_data("Coca 2", 3, 5.64)

def view():
    conn = psycopg2.connect("dbname='mydatabase' user='alan' password='123456' host= 'localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='mydatabase' user='alan' password='123456' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item= %s",(item,))
    conn.commit()
    conn.close()

def update(quantity, price ,item):
    conn = psycopg2.connect("dbname='mydatabase' user='alan' password='123456' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price ,item))
    conn.commit()
    conn.close()

#delete("orange")
update(11,11,"sabritas")
print(view())
#insert_data("orange",34,16)
crate_table()