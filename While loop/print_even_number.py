start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
i = start
while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1