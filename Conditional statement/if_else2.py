marks = int(input("Enter your marks : "))

if marks > 90 and marks <= 100:
    print("'A'")

elif marks <= 90 and marks > 75:
    print("'B'")

elif marks <= 75 and marks > 60:
    print("'C'")

elif marks <= 60 and marks > 45:
    print("'D'")

elif marks <=45 and marks > 0:
    print("Fail")
    
else:
    print("Invalid value")
    