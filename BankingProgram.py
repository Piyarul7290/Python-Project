def show_balance():
    print(f"Your balance is: ${balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"${amount} has been deposited.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"${amount} has been withdrawn.")
    else:
        print("Insufficient funds.")


balance = 0
is_running = True


while is_running:
    print("Balance Program")
    print("1. show balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")