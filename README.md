# BANK50
#### Video Demo: https://youtu.be/6M2SBgjPCFk
#### Description:

BANK50 is a command-line banking system developed in Python as a final project for CS50. The project simulates the core functionalities of a real banking application while demonstrating concepts such as file handling, authentication, hashing, modular programming, input validation, and persistent data storage.

The application allows users to:
- Create accounts
- Login securely
- Check balances
- Deposit money
- Withdraw money
- Store account data permanently using CSV files

# Function Descriptions

## `main()`

The `main()` function acts as the driver function of the entire banking system. It continuously displays the main menu and controls the navigation of the application.

The function handles:
- account creation,
- login,
- banking services,
- logout,
- and exiting the program.

It also uses `try-except` blocks to safely handle invalid non-numeric inputs entered by users.

---

## `read()`

The `read()` function opens the CSV file and reads all account data using `csv.DictReader`.

The function converts each row into a dictionary and returns all rows as a list. This abstraction prevents repetitive file-reading logic throughout the project.

Example returned structure:

```python
[
    {
        "name": "Rinkal",
        "account_number": "1234567890",
        "PIN": "hashed_pin",
        "balance": "5000"
    }
]
```

---

## `append(row)`

The `append()` function is responsible for adding new accounts into the CSV file.

If the file is empty, the function automatically writes the CSV header before appending the account information.

This function is used during account creation.

---

## `write(rows)`

The `write()` function rewrites the entire CSV file using updated account data.

CSV files cannot directly modify a single row, so the program:
1. reads all rows,
2. modifies the required row,
3. rewrites the entire file.

This function is mainly used after deposits and withdrawals.

---

## `hash_PIN(pin)`

The `hash_PIN()` function secures user PINs using Python’s `hashlib` module and the SHA-256 hashing algorithm.

Instead of storing plain-text PINs, the function converts the PIN into a secure hash before saving it in the CSV file.

This improves the security of the banking system and simulates how real authentication systems work.

---

## `create_account()`

The `create_account()` function handles the account registration process.

It:
- asks for the user's name,
- validates the PIN,
- validates the minimum starting balance,
- generates a unique account number,
- hashes the PIN,
- and stores the account data inside the CSV file.

The function ensures that duplicate account numbers are never generated.

---

## `login()`

The `login()` function authenticates users using:
- account number,
- and PIN.

The entered PIN is hashed and compared with the stored hashed PIN.

Users are given three attempts to enter the correct PIN. If all attempts fail, the account is locked.

If authentication succeeds, the logged-in user’s account dictionary is returned.

---

## `withdraw(balance, amount)`

The `withdraw()` function calculates the updated balance after subtracting the withdrawal amount from the current balance.

The function returns the new balance value.

---

## `deposit(balance, amount)`

The `deposit()` function calculates the updated balance after adding the deposited amount to the current balance.

The function returns the new balance value.

---

## `update_accounts(user, new_balance)`

The `update_accounts()` function updates a user's balance inside the CSV file.

The function:
- reads all account rows,
- finds the matching account,
- updates the balance,
- rewrites the CSV file,
- and synchronizes the currently logged-in user data.

This ensures that both the CSV file and the active session contain the same updated balance.

---

# Validations Implemented

The project includes several validations to improve reliability and security.

## PIN Validation

During account creation, the program only accepts a 4-digit PIN between 1000 and 9999.

This prevents invalid or insecure PIN values.

---

## Balance Validation

The initial account balance must be at least 1000.

The system repeatedly prompts the user until a valid balance is entered.

---

## Deposit Validation

Deposits cannot be negative.

If the user enters an invalid amount, the system asks for the input again.

---

## Withdrawal Validation

The system prevents:
- negative withdrawals,
- and withdrawals larger than the available balance.

---

## Input Validation

The program uses `try-except` blocks to safely handle invalid non-numeric inputs and prevent application crashes.


# Conclusion

BANK50 demonstrates important programming concepts including:
- file handling,
- hashing,
- authentication,
- validation,
- modular programming,
- and persistent data management.

The project successfully simulates a simple banking system while maintaining a clean, modular, and reusable code structure.
