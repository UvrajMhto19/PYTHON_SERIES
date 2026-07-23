# n = int(input("Enter a number: "))

# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

i = start
while i <= end:
    print(i, end=" ")
    i += 1

print(f"After while loop, Starting value is {start} and ending value is {end}")