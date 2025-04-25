'''
Problem: Date Difference Calculator (Real-World Scenario)

Description:
Create a program that calculates the number of days a person has lived based on their birthdate.
The program should:
1. Accept a birthdate in the format dd-mm-yyyy
2. Calculate the number of days from the birthdate to the current date
3. Display the result to the user

This problem demonstrates working with date objects, parsing user input, and performing
date-based calculations for real-world applications.

Approach:
- Use the datetime module to handle date operations
- Parse the user input string into a datetime object
- Calculate the difference between the current date and the birthdate
- Return the result in days
'''

from datetime import datetime

def calculate_days_lived(birthdate):
    # Current date
    today = datetime.now()

    # Convert birthdate from string to datetime object
    birthdate = datetime.strptime(birthdate, "%d-%m-%Y")

    # Calculate the difference in days
    days_lived = (today - birthdate).days

    return days_lived

# Main execution
if __name__ == "__main__":
    # User input for birthdate
    birthdate = input("Enter your birthdate (dd-mm-yyyy): ")

    # Calculate and display the number of days lived
    days = calculate_days_lived(birthdate)
    print(f"You have lived {days} days.")