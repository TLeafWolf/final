import sqlite3

con = sqlite3.connect("inventory3.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Supply
           (name text PRIMARY KEY, price real, Count INTEGER, Location text) ''')

cur.execute('''INSERT OR IGNORE INTO Supply VALUES
            ('Dog Food One','48.34', '24', 'A12')''')

con.commit()

for row in cur.execute('''SELECT * FROM Supply'''):
    print(row)