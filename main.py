import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

DB_PATH = '../database/inventory.db'

# ---------- Add Product ----------
def add_product(name, price, quantity):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    conn.close()
    print(f"Product '{name}' added successfully!")

# ---------- Update Product ----------
def update_product(product_id, name=None, price=None, quantity=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE Products SET name=? WHERE product_id=?", (name, product_id))
    if price:
        cursor.execute("UPDATE Products SET price=? WHERE product_id=?", (price, product_id))
    if quantity:
        cursor.execute("UPDATE Products SET quantity=? WHERE product_id=?", (quantity, product_id))
    conn.commit()
    conn.close()
    print(f"Product ID {product_id} updated successfully!")

# ---------- Delete Product ----------
def delete_product(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Products WHERE product_id=?", (product_id,))
    conn.commit()
    conn.close()
    print(f"Product ID {product_id} deleted successfully!")

# ---------- Record Sale ----------
def record_sale(product_id, quantity_sold):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT quantity, name FROM Products WHERE product_id=?", (product_id,))
    result = cursor.fetchone()
    if not result:
        print("Product not found!")
        conn.close()
        return
    current_qty, name = result
    if quantity_sold > current_qty:
        print(f"Not enough stock! Current quantity: {current_qty}")
        conn.close()
        return
    cursor.execute("UPDATE Products SET quantity=? WHERE product_id=?", (current_qty - quantity_sold, product_id))
    sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO Sales (product_id, quantity_sold, sale_date) VALUES (?, ?, ?)", (product_id, quantity_sold, sale_date))
    conn.commit()
    conn.close()
    print(f"Sale recorded for product '{name}'! Quantity sold: {quantity_sold}")

# ---------- View Products ----------
def view_products():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products_list = ""
    for row in rows:
        products_list += f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}\n"
    return products_list

# ---------- Sales Chart ----------
def sales_chart():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.name, SUM(s.quantity_sold) 
        FROM Sales s 
        JOIN Products p ON s.product_id = p.product_id
        GROUP BY p.name
    """)
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No sales data to show.")
        return

    products = [row[0] for row in data]
    sales = [row[1] for row in data]

    plt.bar(products, sales, color='skyblue')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.title('Sales per Product')
    plt.show()