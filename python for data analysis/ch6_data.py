import sqlite3
query = """
CREATE TABLE testpy(
a VARCHAR(20),b VARCHAR(20),
c REAL,d INTEGER);
"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()