'''
Problem: Separate and Sort (String Manipulation)

Description:
Develop a function that takes a mixed string of letters and digits, separates them,
sorts each group (letters and digits) individually, and then concatenates them.

The function should:
1. Separate alphabetic characters from numeric characters
2. Sort the alphabetic characters alphabetically
3. Sort the numeric characters numerically
4. Concatenate the sorted alphabetic characters followed by the sorted numeric digits

For example, input "B4A1D3" should output "ABD134"

Approach:
- Use list comprehension to separate letters and digits
- Sort each group independently
- Join the sorted groups and return the result
- Use built-in string methods to identify character types
'''

def separate_and_sort(s):
    """
    Separates letters and digits from a string, sorts them individually,
    and returns the concatenated result.
    
    Args:
        s: Input string containing letters and digits
        
    Returns:
        String with sorted letters followed by sorted digits
    """
    letters = ''.join(sorted([c for c in s if c.isalpha()]))
    digits = ''.join(sorted([c for c in s if c.isdigit()]))
    return letters + digits

# Test the function
if __name__ == "__main__":
    input_string = "B4A1D3"
    output_string = separate_and_sort(input_string)
    print(f"Input: {input_string}")
    print(f"Output: {output_string}")