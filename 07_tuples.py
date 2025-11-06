# TUPLES (like lists but cannot be changed)

colors = ("red", "green", "blue")

# Accessing elements
print("First color:", colors[0])

# Length of tuple
print("Number of colors:", len(colors))

# Tuples are immutable, so we can’t modify them directly
# colors[0] = "yellow"  # ❌ This will cause an error

# But we can loop through them
for color in colors:
    print(color)