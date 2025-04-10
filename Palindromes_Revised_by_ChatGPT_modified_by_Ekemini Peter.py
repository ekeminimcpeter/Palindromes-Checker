# Author: Ekemini Peter
# Date: 15/12/2024
# Description: Improved Palindrome Checker
# Appreciation: Thanks to ChatGPT for the modularity concept to improve and optimise version code
##################################################################################################################

def is_palindrome(text):
# Normalize the input: remove spaces, convert to uppercase
    normalized_text = text.replace(" ", "").upper()
    # Check if the string is equal to its reverse
    return normalized_text == normalized_text[::-1] # normalized_text[::-1]: causes the string to be read in reverse

# Collect user text
user_text = input("Enter the text to be checked: ")

if user_text != "":
    result = is_palindrome(user_text)
    print("Testing Palindrome Checker...\n")
    print("Result:", "It's a palindrome" if result else "It's not a palindrome")
else:
    print("It's not a palindrome")
