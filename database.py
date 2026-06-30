import sqlite3

conn = sqlite3.connect("agriculture.db")
cursor = conn.cursor()

# Farmers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS farmers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile TEXT,
    village TEXT,
    username TEXT,
    password TEXT
)
""")

# Crop Management Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS crop_management(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name TEXT,
    farmer_name TEXT,
    village TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()



print("Database Created Successfully")