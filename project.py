import random
import csv
import sys
import hashlib
import pyfiglet

FILE = "accounts.csv"

def main():
    
    while True: 
        
        try:
            choice = int(input("0. Create an Account\n 1. Login\n 2. Exit\n Choose: "))
        except ValueError:
            print("Invalid Input")
            continue

        match choice:
            # create an account
            case 0:
                create_account()

            # login
            case 1:
                user = login()
                if not user:
                    print("Invalid Credentials")
                    continue

                while True: 
                    try:
                        service = int(input("0. Balance inquiry\n 1. Withdraw\n 2. Deposit\n 3. Logout\n Choose Serice: "))
                    except ValueError:
                        print("Invalid Input")
                        continue

                    match service:
                        
                        # balance inquiry
                        case 0:
                            print(f"*** Your balance is {user['balance']} ***")

                        # withdraw    
                        case 1:
                            while True:
                                amount = int(input("Amount to Withdraw: "))
                                if amount <= 0:
                                    print("Invalid Amount")
                                elif amount > int(user["balance"]):
                                    print("Insufficient Balance")
                                else:
                                    break
                                
                            new_balance = withdraw(user["balance"], amount)
                            update_accounts(user, new_balance)
                            

                        # deposit
                        case 2:
                            while True:
                                amount = int(input("Amount to Deposit: "))
                                if amount < 0:
                                    print("Invalid Amount")
                                else:
                                    break
                                    
                            new_balance = deposit(user["balance"], amount)
                            update_accounts(user, new_balance)

                        # logout
                        case 3:
                            break
                        
                        case _:
                            print("Invalid Service")
                
            # exit  
            case 2:
                break
            
            case _:
                print("Invalid Input")   
           
# helper functions
def read():
    with open(FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def append(row): 
    rows = read()
    with open(FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "account_number", "PIN", "balance"])
        if len(rows) == 0:
            writer.writeheader()
        writer.writerow(row)
        
def write(rows):
    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "account_number", "PIN", "balance"])
        writer.writeheader()
        writer.writerows(rows)
        
def hash_PIN(pin):
    return hashlib.sha256(str(pin).encode()).hexdigest()

    
# core functionality         
def create_account():
    name = input("Name: ")
    
    while True:
        PIN = int(input("PIN: "))
        if 1000 <= PIN <= 9999:
            break
    
    while True:
        balance = int(input("Balance: "))
        if balance >= 1000:
            break
    
    while True:
        account_number = random.randint(1000000000, 9999999999)
        matched = False

        rows = read()
        for row in rows:
            if int(row["account_number"]) == account_number:
                matched = True
                    
        if not matched:
            break
                
    append({"name": name, "account_number": account_number, "PIN": hash_PIN(PIN), "balance":balance})
    print(f"Your account number is {account_number}")
         
def login():
    account_number = input("Account number: ")
    
    rows = read()
    
    for row in rows:
        if row["account_number"] == account_number:
            i = 0
            while i < 3:
                PIN = input("PIN: ")
                if hash_PIN(PIN) == row["PIN"]:
                    return row
                i = i + 1
            sys.exit("Account locked")
    return None            
        
def withdraw(balance, amount):
    return int(balance) - amount
    
def deposit(balance, amount):
    return int(balance) + amount
    
def update_accounts(user, new_balance):
    new_rows = []
        
    rows = read()
    for row in rows:
        if row["account_number"] == user["account_number"]:
            row["balance"] = new_balance
        new_rows.append(row)
            
    write(new_rows)
    user["balance"] = str(new_balance) 


if __name__ == "__main__":
    main()