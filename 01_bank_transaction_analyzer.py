'''
Problem: Bank Transaction Analyzer

Description:
Create a program that simulates a simple bank transaction system. The program should allow users to:
1. Make deposits (credits)
2. Make withdrawals (debits)
3. View their transaction history and final balance

The program should handle edge cases like insufficient funds for withdrawals and invalid inputs.

Approach:
- Use a while loop to continuously present options to the user
- Track balance and transaction history in memory
- Validate user inputs and handle edge cases
- Format currency values with proper decimal places
- Provide clear feedback for each transaction
'''

def bank_transaction_analyzer():
    balance = 0
    transaction_history = []
    
    while True:
        print("\nBank Transaction Menu:")
        print("1. Credit (Deposit)")
        print("2. Debit (Withdrawal)")
        print("3. Exit and Show Summary")
        
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == '1':
            amount = float(input("Enter the credit amount: "))
            balance += amount
            transaction_history.append(f"Credited: ${amount:.2f}")
            print(f"Transaction successful! Balance: ${balance:.2f}")
        
        elif choice == '2':
            amount = float(input("Enter the debit amount: "))
            if amount > balance:
                print("❌ Insufficient funds!")
            else:
                balance -= amount
                transaction_history.append(f"Debited: ${amount:.2f}")
                print(f"Transaction successful! Balance: ${balance:.2f}")
        
        elif choice == '3':
            print("\nFinal Summary:")
            print(f"Ending balance: ${balance:.2f}")
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)
            break
        
        else:
            print("⚠️ Invalid option. Please try again.")

# Run the Bank Transaction Analyzer
if __name__ == "__main__":
    bank_transaction_analyzer()