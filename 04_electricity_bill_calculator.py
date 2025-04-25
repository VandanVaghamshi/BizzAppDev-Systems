'''
Problem: Electricity Bill Calculation (Business Logic)

Description:
Develop a program that calculates electricity bills based on a tiered pricing structure.
The pricing tiers are as follows:
- 0-100 units: ₹5 per unit
- 101-300 units: ₹7 per unit
- 301-500 units: ₹10 per unit
- Above 500 units: ₹15 per unit

The program should:
1. Accept electricity usage in kilowatt-hours (kWh)
2. Calculate the bill based on the tiered pricing structure
3. Display a detailed breakdown of charges for each tier
4. Show the total amount payable

Approach:
- Use conditional statements to determine which pricing tiers apply
- Calculate charges for each applicable tier
- Provide a detailed breakdown of the bill
- Format the output with proper currency symbols
'''

def electricity_bill_calculator(usage):
    if usage <= 100:
        bill = usage * 5
        print(f"0-100 units @ ₹5/unit = ₹{bill}")
    elif usage <= 300:
        bill = (100 * 5) + ((usage - 100) * 7)
        print(f"0-100 units @ ₹5/unit = ₹{100 * 5}")
        print(f"101-300 units @ ₹7/unit = ₹{(usage - 100) * 7}")
    elif usage <= 500:
        bill = (100 * 5) + (200 * 7) + ((usage - 300) * 10)
        print(f"0-100 units @ ₹5/unit = ₹{100 * 5}")
        print(f"101-300 units @ ₹7/unit = ₹{200 * 7}")
        print(f"301-500 units @ ₹10/unit = ₹{(usage - 300) * 10}")
    else:
        bill = (100 * 5) + (200 * 7) + (200 * 10) + ((usage - 500) * 15)
        print(f"0-100 units @ ₹5/unit = ₹{100 * 5}")
        print(f"101-300 units @ ₹7/unit = ₹{200 * 7}")
        print(f"301-500 units @ ₹10/unit = ₹{200 * 10}")
        print(f"Above 500 units @ ₹15/unit = ₹{(usage - 500) * 15}")

    print(f"Total Amount Payable = ₹{bill}")

# Example usage
if __name__ == "__main__":
    usage = float(input("Enter electricity usage (in kWh): "))
    electricity_bill_calculator(usage)