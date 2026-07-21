# age = int(input("Enter your age: "))

# if age >= 18:
#     status = "Adult"

# else:
#     status = "Minor"

# OR

age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"

print(f"you're in category{status}")