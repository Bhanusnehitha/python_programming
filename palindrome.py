def palindrome(s):
    # Base case
    if len(s) <= 1:
        return True

    # Check first and last characters
    if s[0] != s[-1]:
        return False

    # Recursive call for the remaining string
    return palindrome(s[1:-1])

# User input
text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")