import csv

csv_file = 'transaction.csv'

def register():
    user = str(input("Username: "))
    password = str(input("Password: "))
    print (f'User registered successfully!')
    return user, password

def login(username, name, password, word):
        if username == name and password == word:
            print (f'Login succesfully!')
            return 0
        else:
            print (f'Error. User/Password are invalid. Please try again.') 
            return 1

def add_transaction(transactions, amount, category):
    transactions.append({"amount": amount, "category": category})
    print("Transaction added successfully.")

    # Write transaction to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

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
    print('''
Transaction History:
----------------------
Index   Amount    Category
''')

    for idx, transaction in enumerate(transactions, 1):
        amount = f'${transaction["amount"]}'
        category = transaction['category']
        print(f'{idx:<6} {amount:<10} {category}')
        

def menu():
    print(f'''\n
--------- M E N U ---------

1. Add Expense
2. Add Income
3. Show Balance
4. Show Transactions
5. Exit

---------------------------''')
    
def start():
    print(f'''
Welcome to Personal Finance Manager!

1. Register
2. Log in
3. Exit''')  
        
def main():
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
            break
        else:
            print("Invalid choice. Please try again.")

def welcome():   
    user = ""
    pas = ""
    
    while True:
        start()
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print (f'\nWelcome. To register please provide:')
            user, pas = register()
            return welcome()
 
        elif choice == 2:
            print (f'\n---- Login ----')
            
            count = 1
            while count < 4:
                name = str(input("Username: "))
                word = str(input("Password: "))
                result = login(user, name, pas, word)
                if result == 0:
                    return main()
                    break
                else:
                    count += 1
                
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please try again.")

welcome()
    