import sqlite3

DB_PATH = '../database/inventory.db'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

# Create Sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity_sold INTEGER NOT NULL,
    sale_date TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
)
""")

conn.commit()
conn.close()
print("Database and tables created successfully!")