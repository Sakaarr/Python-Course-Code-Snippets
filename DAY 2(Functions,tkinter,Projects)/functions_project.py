# Mini Banking System using functions 

account = {}

def create_account():
    name = input("Enter your name: ")
    
    if name in account:
        print("Account already exists.")
    else:
        account[name] = 0
        print(f"Account created for {name} with balance Rs.0")
        
def check_balance():
    name = input("Enter your name: ")
    
    if name in account:
        print(f"Your balance is Rs.{account[name]}")
    else:
        print("Account not found.")
        
def deposit():
    name = input("Enter your name: ")
    
    if name in account:
        amount = float(input("Enter amount to deposit: "))
        account[name] += amount
        print(f"Rs.{amount} deposited. New balance is Rs.{account[name]}")
        # print(account)
    else:
        print("Account not found.")
        
def withdraw():
    name = input("Enter your name: ")
    
    if name in account:
        amount = float(input("Enter amount to withdraw: "))
        
        if amount > account[name]:
            print("Insufficient balance.")
        else:
            account[name] -= amount
            print(f"Rs.{amount} withdrawn. New balance is Rs.{account[name]}")
    else:
        print("Account not found.")

def main():
    while True:
        print("\n-----Mini Banking System------")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            print("Exiting the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()