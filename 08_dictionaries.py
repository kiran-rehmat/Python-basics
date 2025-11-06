# DICTIONARIES (store data in key-value pairs)

student = {
    "name": "Kiran",
    "age": 20,
    "course": "Information Technology"
}

# Accessing values
print("Student name:", student["name"])

# Adding a new key-value pair
student["grade"] = "A"
print("Updated student info:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)