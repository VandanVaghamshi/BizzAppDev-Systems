'''
Problem: Reverse Counting (Recursion Check)

Description:
Create a recursive function that counts down from a given number to 1.
This problem tests understanding of recursion and stack limits in Python.

The program should:
1. Accept a number as input
2. Use recursion to print numbers from that number down to 1
3. Handle large inputs by adjusting the recursion limit

Approach:
- Implement a recursive function that prints the current number
- Use the base case to stop recursion when n < 1
- Increase the recursion limit to handle larger inputs
- Call the recursive function with the desired starting number
'''

import sys
sys.setrecursionlimit(1100)  # Increase recursion limit to handle larger inputs

def reverse_count(n):
    """
    Recursively count down from n to 1
    
    Args:
        n: The number to start counting from
    """
    if n < 1:
        return
    print(n)
    reverse_count(n - 1)

# Main execution
if __name__ == "__main__":
    try:
        # For demonstration, we'll use a fixed value
        # In a real application, you might want to get user input
        start_number = 1000
        print(f"Counting down from {start_number}:")
        reverse_count(start_number)
    except RecursionError:
        print("Error: Maximum recursion depth exceeded.")
        print("Try increasing the recursion limit or using a smaller number.")