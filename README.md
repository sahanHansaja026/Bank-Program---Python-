# Bank Program

This project is a simple banking system implemented in Python. It allows users to create accounts, deposit money, check balances, and withdraw cash. User account details are stored in a CSV file.

## Project Structure
- `main.py` - The main program file
- `initial.py` - Initializes the account
- `saving.py` - Handles saving money into the account
- `balance.py` - Checks the account balance
- `withdraw.py` - Withdraws cash from the account
- `accounts.csv` - Stores user account details

## Features
- Create a new account
- Deposit money
- Check account balance
- Withdraw cash

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-program.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bank-program
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main program:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to create an account, deposit money, check balance, or withdraw cash.

### Example Usage
When you run the main program, you will see a menu with the following options:
```
This is the main operations of our bank:
1. Initialize account
2. Check balance
3. Deposit money in the account
4. Withdraw money in the account

Enter the operation index number: 
```
For example, to deposit money:
1. Enter the operation index number: `3`
2. Enter the account number to update the balance: `0660-123-1`
3. Enter the new balance: `500`
4. You will see a confirmation message: `Balance updated successfully.`

![Example Usage](https://github.com/sahan026/images/blob/main/bank_program.png)

## Files Description
- `main.py`: The main entry point of the program. It coordinates the different functionalities.
- `initial.py`: This script is responsible for initializing new user accounts.
- `saving.py`: This script handles the logic for depositing money into the account.
- `balance.py`: This script allows users to check their current account balance.
- `withdraw.py`: This script handles cash withdrawals from the account.
- `accounts.csv`: A CSV file that stores user account details, including account number, name, and balance.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any changes or improvements.
