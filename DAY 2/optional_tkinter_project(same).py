import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "account.txt"

# --- Utility Functions ---
def load_accounts():
    accounts = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                name, pwd, balance = line.strip().split("|")
                accounts[name] = {"password": pwd, "balance": float(balance)}
    return accounts

def save_accounts(accounts):
    with open(FILENAME, "w") as file:
        for name, data in accounts.items():
            file.write(f"{name}|{data['password']}|{data['balance']}\n")

accounts = load_accounts()

# --- GUI Logic ---
def create_account():
    name = entry_name.get()
    pwd = entry_pwd.get()

    if name in accounts:
        messagebox.showerror("Error", "Account already exists.")
    else:
        accounts[name] = {"password": pwd, "balance": 0.0}
        save_accounts(accounts)
        messagebox.showinfo("Success", "Account created successfully!")

def login():
    name = entry_name.get()
    pwd = entry_pwd.get()

    if name in accounts and accounts[name]["password"] == pwd:
        messagebox.showinfo("Welcome", f"Welcome back, {name}!")
        open_dashboard(name)
    else:
        messagebox.showerror("Login Failed", "Invalid name or password.")

# --- Dashboard Window ---
def open_dashboard(username):
    root.withdraw()  # hide main window
    dash = tk.Toplevel()
    dash.title("Dashboard")
    dash.geometry("300x300")

    def check_balance():
        bal = accounts[username]["balance"]
        messagebox.showinfo("Balance", f"₹{bal}")

    def deposit_money():
        amount = float(entry_amount.get())
        accounts[username]["balance"] += amount
        save_accounts(accounts)
        messagebox.showinfo("Success", f"Deposited ₹{amount}")

    def withdraw_money():
        amount = float(entry_amount.get())
        if amount <= accounts[username]["balance"]:
            accounts[username]["balance"] -= amount
            save_accounts(accounts)
            messagebox.showinfo("Success", f"Withdrew ₹{amount}")
        else:
            messagebox.showwarning("Insufficient", "Not enough balance.")

    def logout():
        dash.destroy()
        root.deiconify()  # show main window again

    tk.Label(dash, text=f"Welcome, {username}", font=("Arial", 14)).pack(pady=10)

    tk.Button(dash, text="Check Balance", command=check_balance).pack(pady=5)
    entry_amount = tk.Entry(dash)
    entry_amount.pack(pady=5)
    tk.Button(dash, text="Deposit", command=deposit_money).pack(pady=5)
    tk.Button(dash, text="Withdraw", command=withdraw_money).pack(pady=5)
    tk.Button(dash, text="Logout", command=logout).pack(pady=10)

# --- Main Window ---
root = tk.Tk()
root.title("Mini Banking App")
root.geometry("300x250")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Password:").pack()
entry_pwd = tk.Entry(root, show="*")
entry_pwd.pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Create Account", command=create_account).pack(pady=5)

root.mainloop()
