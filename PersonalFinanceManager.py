def menu():
    while True:
        print (f'''\nWelcome to your Personal Finance Manager!
        
        1. Register
        2. Login
        3. Exit''')
    
        choice = int(input("\nEnter your choice: "))
        
        if choice == 3:
            break
    

def main():
    menu()


main()