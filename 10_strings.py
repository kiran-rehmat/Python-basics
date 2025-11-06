# STRINGS AND THEIR METHODS

text = "Hello Python"

# Accessing characters
print("First character:", text[0])

# String slicing
print("First 5 letters:", text[:5])

# String methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Replace:", text.replace("Python", "World"))

# Loop through string
for char in text:
    print(char, end=" ")