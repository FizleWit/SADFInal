import sqlite3 as sql

conn = sql.connect("database.db")
conn.execute("CREATE TABLE Inventory(productname TEXT, description TEXT, quantity INTGER, date TEXT)") 
conn.close()

print("Created")
