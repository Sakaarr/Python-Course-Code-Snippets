#ENHANCE THE MINI BANKING PROJECT WITH LOGIN FEATURE AND FILE SAVING

FILE_NAME = "account.txt"
#LOAD ACCOUNTS FROM FILE
def load_accounts():
    accounts = {}
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                name, password, balance = line.strip().split("|")
                accounts[name] = {"password": password, "balance": float(balance)}
    except FileNotFoundError:
        pass
    return accounts

#SAVE ACCOUNTS TO FILE
def save_accounts(accounts):
    with open(FILE_NAME, 'w') as file:
        for name, data in accounts.items():
            file.write(f"{name}|{data['password']}|{data['balance']}\n")
            
#CREATE ACCOUNT FUNCTION
def create_account(accounts):
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists.")
    else:
        password = input("Enter a password:")
        accounts[name] = {"password": password, "balance": 0.0}
        save_accounts(accounts)
        print(f"Account created for {name} with balance Rs.0")
        
def login(accounts):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    
    if name in accounts and accounts[name]["password"] == password:
        print(f"Login successful! Welcome {name}.")
        return name
    else:
        print("Invalid credentials.")
        return None
    
# Check balance
def check_balance(accounts, name):
    print(f"💰 {name}, your balance is ₹{accounts[name]['balance']}")

# Deposit money
def deposit(accounts, name):
    amount = float(input("Enter amount to deposit: ₹"))
    accounts[name]["balance"] += amount
    save_accounts(accounts)
    print(f"✅ ₹{amount} deposited. New balance: ₹{accounts[name]['balance']}")

# Withdraw money
def withdraw(accounts, name):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= accounts[name]["balance"]:
        accounts[name]["balance"] -= amount
        save_accounts(accounts)
        print(f"✅ ₹{amount} withdrawn. New balance: ₹{accounts[name]['balance']}")
    else:
        print("⚠️ Insufficient balance.")

# --- MAIN PROGRAM ---
accounts = load_accounts()

while True:
    print("\n--- MINI BANKING SYSTEM ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        create_account(accounts)

    elif choice == "2":
        user = login(accounts)
        if user:
            while True:
                print(f"\n--- Welcome, {user} ---")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Logout")

                option = input("Choose an option (1-4): ")

                if option == "1":
                    check_balance(accounts, user)
                elif option == "2":
                    deposit(accounts, user)
                elif option == "3":
                    withdraw(accounts, user)
                elif option == "4":
                    print("🔒 Logged out.")
                    break
                else:
                    print("❗ Invalid option.")

    elif choice == "3":
        print("👋 Exiting Banking System. Bye!")
        break

    else:
        print("❗ Invalid choice. Try again.")