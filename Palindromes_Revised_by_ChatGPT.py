# Author: Ekemini Peter
# Date: 15/12/2024
# Description: Improved Palindrome Checker
# Appreciation: Thanks to ChatGPT for the modularity concept to improve and optimise version code
##################################################################################################################

def is_palindrome(text):
# Normalize the input: remove spaces, convert to uppercase
    normalized_text = text.replace(" ", "").upper()
    # Check if the string is equal to its reverse
    return normalized_text == normalized_text[::-1]

# Test cases
test_cases = [
    "racecar",  # Simple palindrome
    "A man a plan a canal Panama",  # Palindrome with spaces
    "Hello, World!",  # Not a palindrome
    " ",  # Edge case: single space
    "Madam In Eden, I'm Adam",  # Palindrome with punctuation
    "1234321",  # Numeric palindrome
    "Palindrome",  # Not a palindrome
]

print("Testing Palindrome Checker...\n")
for case in test_cases:
    result = is_palindrome(case)
    print(f"Test: {case}")
    print("Result:", "It's a palindrome" if result else "It's not a palindrome")
    print("-" * 40)

