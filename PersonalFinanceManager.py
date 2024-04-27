def register():
    # Solicita al usuario que ingrese su nombre de usuario y contraseña
    user = str(input("Username: "))
    password = str(input("Password: "))

    print (f'User registered successfully!')
    # Retorna el nombre de usuario y la contraseña
    return user, password

def login(username, name, password, word):
    # Comprueba si el nombre de usuario y la contraseña coinciden con los proporcionados
    if username == name and password == word:
        print (f'Login successfully!')
        # Retorna 0 para indicar que el inicio de sesión fue exitoso
        return 0
    else:
        # Imprime un mensaje de error si el nombre de usuario o la contraseña son incorrectos
        print (f'Error. User/Password are invalid. Please try again.') 
        # Retorna 1 para indicar que el inicio de sesión falló
        return 1

def add_transaction(amount, category):
    # Abre el archivo 'transaction.txt' en modo append ('a')
    file = open('transaction.txt', 'a')
    # Escribe la transacción (cantidad y categoría) en el archivo
    file.write(f'{amount},{category}\n') 
    # Cierra el archivo después de escribir
    file.close()
    
    print('Transaction added successfully.')
        
def open_file():
    # Abre el archivo 'transaction.txt' en modo lectura ('r')
    file = open('transaction.txt', 'r')
    # Lee el contenido del archivo y lo guarda en una lista
    content = file.readlines()   
    # Cierra el archivo después de leer
    file.close()
    # Retorna la lista con el contenido del archivo
    return content

def show_balance():
    #Se crean variables para hacer la suma de los incomes y los expenses
    total_income = 0
    total_expenses = 0
    # Obtiene el contenido del archivo 'transaction.txt'
    content = open_file()

    #Separa la cantidad de la categoría
    for line in content:
        amount, category = line.split(',')
        #Para poder imprimir la cantidad como un número hay que convertirlo a un 'floar'
        amount = float(amount)
        # A través de un condicional se derivan los valores a sumar según su categoría
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

def show_transactions():
    print('''
Transaction History:
----------------------
Index   Amount    Category
''')
   
    # Obtiene el contenido del archivo 'transaction.txt'
    content = open_file()  

    #A través del ciclo for se busca otorgar un indice a cada linea para así poder mostrar al usuario el historial de sus transacciones
    for index, line in enumerate(content, 1):
        amount, category = line.split(',')
        amount = float(amount)
        #Como en el main le otorgamos un valor negativo a los expenses, aquí se busca quitarle el signo negativo a las distintas cantidades impuestas
        amount_str = f'${amount}' if amount >= 0 else f'-${abs(amount)}'
        # Imprime cada transacción en un formato específico
        print(f'{index:<6} {amount_str:<10} {category}') 
        

def menu():
    # Imprime el menú de opciones
    print('''
--------- M E N U ---------

1. Add Expense
2. Add Income
3. Show Balance
4. Show Transactions
5. Exit

---------------------------''')
    
def start():
    # Imprime el mensaje de bienvenida y las opciones iniciales
    print('''
Welcome to Personal Finance Manager!

1. Register
2. Log in
3. Exit''')  
        
def main():
    print("\nRecord and categorize your daily expenses and monitor income streams")

    while True:
        menu()

        # Solicita al usuario que ingrese su elección
        choice = int(input("Enter your choice: "))

        # Realiza acciones según la elección del usuario
        if choice == 1:
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            add_transaction(-amount, category)
        
        elif choice == 2:
            amount = float(input("Enter income amount: $"))
            category = input("Enter income category: ")
            add_transaction(amount, category)
        
        elif choice == 3:
            show_balance()
        
        elif choice == 4:
            show_transactions()
        
        elif choice == 5:
            break
        
        else:
            print("Invalid choice. Please try again.")

def welcome():   
    user = ""
    pas = ""
    
    while True:
        start()
        # Solicita al usuario que elija una opción
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            # Si elige registrarse, llama a la función register
            print (f'\nWelcome. To register please provide:')
            user, pas = register()
 
        elif choice == 2:
            # Si elige iniciar sesión, llama a la función login
            print (f'\n---- Login ----')
            
            #Se utilizan los números que retorna la función login para que el usuario solo tenga tres oportunidades para iniciar sesión
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
            # Si elige salir, termina el ciclo y finaliza el programa
            break
        else:
            print("Invalid choice! Please try again.")

# Llama a la función de bienvenida para iniciar el programa
welcome()