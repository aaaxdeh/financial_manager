def login():
    # Prompt the user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the entered credentials match the predefined values
    if username == correct_username and password == correct_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def add_transaction(transactions, amount, category):
    transactions.append({"amount": amount, "category": category})
    print("Transaction added successfully.")

def show_balance(transactions):
    total_income = 0
    total_expenses = 0
    
    for transaction in transactions:
        amount = transaction["amount"]
        if amount > 0:
            total_income += amount
        else:
            total_expenses += amount
            
    balance = total_income + total_expenses
    
    print(f'''\n
 Balance Overview:
-------------------

Total Income: ${total_income}
Total Expenses: ${abs(total_expenses)}

Current Balance: ${balance}\n''')

def show_transactions(transactions):
    print(f'''\n
 Transaction History:
----------------------
{'Index': <6}{'Amount': <10}{'Category': <15}
{'-' * 30}''')
    
    for idx, transaction in enumerate(transactions, 1):
        amount = f'${transaction['amount']}'
        category = transaction['category']
        print(f'{idx: <6}{amount: <10}{category: <15}')

def menu():
    print(f'''\n
--------- M E N U ---------

1. Add Expense
2. Add Income
3. Show Balance
4. Show Transactions
5. Exit

---------------------------''')
        
def main():
    print("Welcome to Personal Finance Manager")

    # Login loop
    while True:
        if login():
            break

    transactions = []

    print("\nRecord and categorize your daily expenses, monitor income streams, track savings goals, and manage investment portfolios.")

    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            add_transaction(transactions, -amount, category)
        elif choice == '2':
            amount = float(input("Enter income amount: $"))
            category = input("Enter income category: ")
            add_transaction(transactions, amount, category)
        elif choice == '3':
            show_balance(transactions)
        elif choice == '4':
            show_transactions(transactions)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
