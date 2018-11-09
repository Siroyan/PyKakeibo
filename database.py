# -*- config: utf-8 -*-
# filename: database.py

import sqlite3

#databese open
dbname = "database.db"
c = sqlite3.connect(dbname)

c.execute("PRAGMA foreign_keys = 1")

#define item table
ddl = """
CREATE TABLE IF NOT EXISTS item
(
    item_code INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL UNIQUE
);
"""

#pub SQL
c.execute(ddl)

#define table of acc_table
ddl = """
CREATE TABLE acc_data
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acc_date DATE NOT NULL,
    item_code INTEGER NOT NULL,
    amount INTEGER,
    FOREIGN KEY(item_code) REFERENCES item(item_code)
);
"""

#pub sql
c.execute(ddl)

#test item table rigistration
c.execute("INSERT INTO item VALUES(1,'食費');")
c.execute("INSERT INTO item VALUES(2,'住宅費');")
c.execute("INSERT INTO item VALUES(3,'光熱費');")
c.execute("COMMIT;")

#test acc_date table registration
c.execute("""
    INSERT INTO acc_data(acc_date,item_code,amount)
    VALUES('2018-11-08',1,1000);
""")
c.execute("COMMIT;")

#test acc_date table registration(using variable)
date = "'{}-{}-{}'".format(2017,3,5)
code = 2
amount = 2000

c.execute("""
    INSERT INTO acc_data(acc_date,item_code,amount)
    VALUES({},{},{});""".format(date,code,amount)
    )
c.execute("COMMIT;")

##show latest data
#show item table
result = c.execute("SELECT * FROM item;")
for row in result:
    print(row)

#show acc_date table
result = c.execute("SELECT * FROM acc_data;")
for row in result:
    print(row)

result = c.execute("""
    SELECT a.acc_date, i.item_name, a.amount
    FROM acc_data as a, item as i
    WHERE a.item_code = i.item_code;
""")
for row in result:
    print(row)
