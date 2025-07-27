import time

class ATM:
    def __init__(self):
        self.card_number = "12345678"
        self.password = "abcdefgh"
        self.balance = 45000
        self.max_daily_withdrawal = 10000

    def check_card(self, card_number):
        if card_number == self.card_number:
            return True
        else:
            print("Wrong Card Number")
            return False

    def check_password(self, password):
        attempts = 0
        while attempts < 3:
            if password == self.password:
                return True
            else:
                attempts += 1
                print("Wrong Password. Try again.")
                password = input("Enter password: ")
        print("You have exceeded the number of attempts.")
        time.sleep(5)
        return False

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        time.sleep(5)

    def withdraw_cash(self, amount):
        if amount > self.balance:
            return 1  # Insufficient balance
        elif amount > self.max_daily_withdrawal:
            return 2  # Exceeded daily withdrawal limit
        else:
            self.balance -= amount
            print("Please take your money from the machine.")
            
            return 3  # Withdrawal successful

def main():
    atm = ATM()

    while True:
        card_number = input("\n=============================\n Welcome to My ATM Machine\n============================ \nEnter your card number: ")
        if atm.check_card(card_number):
            password = input("Enter password: ")
            if atm.check_password(password):
                print("1. Check Balance\n2. Withdraw Cash\n3. Exit")
                option = input("Select an option: ")
                if option == "1":
                    atm.get_balance()
                elif option == "2":
                    amount = float(input("Enter amount to withdraw: $"))
                    result = atm.withdraw_cash(amount)
                    if result == 1:
                        print("Insufficient balance. Please enter a smaller amount.")
                    elif result == 2:
                        print("Exceeded daily withdrawal limit. Please enter a smaller amount.")
                elif option == "3":
                    print("Exiting program. Thank you!")
                    break
                else:
                    print("Invalid option. Please try again.")
            else:
                print("Returning to welcome screen.")
        else:
            print("Returning to welcome screen.")

if __name__ == "__main__":
    main()
