numbers = [10, 20, 30, 40, 50]

num = int(input("Enter number to find position: "))

if num in numbers:
    position = numbers.index(num) + 1
    print("Position of the number is:", position)
else:
    print("Number not found in the list")