# PALINDROME CHECKER
# A palindrome reads the same backward and forward, like "madam" or "121".

def is_palindrome(text):
    text = text.replace(" ", "").lower()  # Remove spaces & make lowercase
    return text == text[::-1]  # Compare text with its reverse

user_input = input("Enter a word or number: ")

if is_palindrome(user_input):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")