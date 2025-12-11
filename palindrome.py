import sys

# Check if exactly one argument is passed
if len(sys.argv) != 2:
    print("Usage: python palindrome_check.py <string>")
    sys.exit(1)

# Read the string from command line argument
text = sys.argv[1]

# Palindrome check
if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")