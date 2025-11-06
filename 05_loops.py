# LOOPS IN PYTHON

# FOR LOOP
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# WHILE LOOP
print("\nCounting down from 5 to 1:")
num = 5
while num > 0:
    print(num)
    num -= 1

# Example: Sum of first 5 numbers
total = 0
for i in range(1, 6):
    total += i
print("\nSum of first 5 numbers:", total)