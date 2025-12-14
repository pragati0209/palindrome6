import sys

# Check if user has provided a string as command-line argument
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    s = sys.argv[1]
    print("User provided string")
else:
    script_name = sys.argv[0]
    s = "madam"
    print("No input given – using default string")

# Convert to lowercase
original = s.lower()

# Reverse the string
reverse = ""
for ch in original:
    reverse = ch + reverse

# Check palindrome
if original == reverse:
    result = "Palindrome"
else:
    result = "Not a palindrome"

# Output
print("Script Name :", script_name)
print("String :", s)
print("Reversed String :", reverse)
print("Result :", result)
