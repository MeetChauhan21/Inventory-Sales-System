import tkinter as tk
from tkinter import messagebox, simpledialog
from main import add_product, update_product, delete_product, record_sale, view_products, sales_chart

# ---------- Main Window ----------
root = tk.Tk()
root.title("Inventory & Sales System")
root.geometry("400x500")

# ---------- Functions ----------
def add_product_gui():
    name = simpledialog.askstring("Input", "Enter product name:")
    if not name:
        messagebox.showerror("Error", "Product name cannot be empty!")
        return

    price_input = simpledialog.askstring("Input", "Enter product price:")
    qty_input = simpledialog.askstring("Input", "Enter product quantity:")

    # Validate price
    try:
        price = float(price_input)
        if price < 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid price! Must be a positive number.")
        return

    # Validate quantity
    try:
        qty = int(qty_input)
        if qty < 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid quantity! Must be a positive integer.")
        return

    add_product(name, price, qty)
    messagebox.showinfo("Success", f"Product '{name}' added!")

def update_product_gui():
    try:
        product_id = int(simpledialog.askstring("Input", "Enter product ID to update:"))
    except:
        messagebox.showerror("Error", "Invalid product ID!")
        return

    name = simpledialog.askstring("Input", "Enter new name (leave blank to skip):")
    price_input = simpledialog.askstring("Input", "Enter new price (leave blank to skip):")
    qty_input = simpledialog.askstring("Input", "Enter new quantity (leave blank to skip):")

    price = None
    qty = None
    # Validate price if entered
    if price_input:
        try:
            price = float(price_input)
            if price < 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Invalid price! Must be a positive number.")
            return

    # Validate quantity if entered
    if qty_input:
        try:
            qty = int(qty_input)
            if qty < 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Invalid quantity! Must be a positive integer.")
            return

    update_product(product_id, name=name if name else None, price=price, quantity=qty)
    messagebox.showinfo("Success", f"Product ID {product_id} updated!")

def delete_product_gui():
    try:
        product_id = int(simpledialog.askstring("Input", "Enter product ID to delete:"))
    except:
        messagebox.showerror("Error", "Invalid product ID!")
        return

    delete_product(product_id)
    messagebox.showinfo("Success", f"Product ID {product_id} deleted!")

def record_sale_gui():
    try:
        product_id = int(simpledialog.askstring("Input", "Enter product ID to sell:"))
        qty_sold = int(simpledialog.askstring("Input", "Enter quantity sold:"))
        if qty_sold < 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid input! Quantity must be a positive integer.")
        return

    record_sale(product_id, qty_sold)
    messagebox.showinfo("Success", "Sale recorded!")

def view_products_gui():
    products = view_products()
    messagebox.showinfo("Products", products if products else "No products found.")

# ---------- GUI Buttons ----------
tk.Label(root, text="Inventory & Sales System", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Add Product", width=25, command=add_product_gui).pack(pady=5)
tk.Button(root, text="Update Product", width=25, command=update_product_gui).pack(pady=5)
tk.Button(root, text="Delete Product", width=25, command=delete_product_gui).pack(pady=5)
tk.Button(root, text="Record Sale", width=25, command=record_sale_gui).pack(pady=5)
tk.Button(root, text="View Products", width=25, command=view_products_gui).pack(pady=5)
tk.Button(root, text="View Sales Chart", width=25, command=sales_chart).pack(pady=5)

root.mainloop()
