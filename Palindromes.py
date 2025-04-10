# Author: Ekemini Peter
# Date: 15/12/2024
# Description: Original implementation of Palindromes Checker
# Scope:
#    assume that an empty string isn't a palindrome;
#    treat upper- and lower-case letters as equal;
#    spaces are not taken into account during the chreck – treat them as non-existent
##################################################################################################################

# Collect User input text
    
user_text = input("Enter a text to be tested: ")
transposed_text = ""                    # empty string to hold the the transposed user text

# Check for empty string: empty string isn't palindrome
if user_text != "":
    
    modified_text = user_text.upper()       # convert all letters to the same case for logical comparison

    # Run loop check on the text entered
            
    for char in range(1,len(modified_text)):
        transposed_text += modified_text[-char]
    transposed_text += modified_text[0]
    transposed_text = transposed_text.replace(" ", "") # remove all white spaces from transposed text
    modified_text = modified_text.replace(" ", "") # remove all white spaces from modified text

    # Compare modified and transposed text for exactness 
    if modified_text == transposed_text:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
else:
    print("It's not a palindrome")


