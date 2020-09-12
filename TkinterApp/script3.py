import sqlite3


def crate_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    open_conn()
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
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO store VALUES(
            ?,
            ?,
            ?
    )""",(item, quantity, price)
    )
    conn.commit()
    conn.close()

#insert_data("Coca 2", 3, 5.64)

def view():
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity, price ,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price ,item))
    conn.commit()
    conn.close()

#delete("Coca 2")
update(11,11,"Coca")
print(view())