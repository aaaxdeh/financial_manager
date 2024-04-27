# financial_manager
Managing personal finances is a crucial aspect of modern life, as it enables individuals to maintain financial stability, achieve their goals, and plan for the future effectively. The Personal Finance Manager is a Python application designed to assist users in organizing and controlling their finances seamlessly.

Financial management begins with understanding one's income, expenses, savings, and investments. The Personal Finance Manager offers a comprehensive platform where users can conveniently record and categorize their daily expenses and monitor their income streams. By centralizing financial data in one place, users gain clarity and control over their financial situation.

Budgeting is a fundamental practice for responsible financial management. With the Personal Finance Manager, users can create monthly budgets for different expense categories and monitor their spending habits. By setting realistic budgets and comparing actual expenses to budgeted amounts, users can identify areas where they may need to adjust their spending and make informed decisions to achieve their financial goals. These insights empower users to make proactive adjustments to their financial strategies and work towards long-term financial stability.

The algorithm for the code created is the following:
1. User Registration:
  - User inputs their username and password.
  - A success message is displayed upon registration.
  - Username and password are stored.
2. Login:
  - User enters their username and password to log in.
  - Verification is done to check if the entered data matches the registered information.
  - If there's a match, a successful login message is shown.
  - If not, an error message is displayed, prompting to try again.
3. Add Transaction:
  - User is prompted to enter the transaction amount and category.
  - The transaction is added to the 'transaction.txt' file.
  - A success message is displayed after adding the transaction.
4. Open File:
  - 'transaction.txt' file is opened to read its contents.
  - The content is stored in a list for further processing.
5. Show Balance:
  - Content of 'transaction.txt' file, containing transactions, is obtained.
  - Total income and expenses are calculated to show the current balance.
6. Show Transactions:
  - Header for transaction history is displayed.
  - Previous transactions are shown in a user-friendly format.
7. Menu Options:
  - A menu displaying available options is presented to the user.
8. Program Start:
  - A welcome message and initial registration or login options are shown.
9. Main Program:
  - A loop is initiated for the user to perform actions based on their financial needs.
  - Options include adding expenses/income, checking balance and transactions, and exiting the program.
10. User Welcome:
  - The program starts by welcoming the user and allowing them to either log in or register as needed.
