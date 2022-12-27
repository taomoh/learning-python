def average(_numbers):
    return sum(_numbers)/len(_numbers)


numbers = []
for i in range(5):
    n = float(input("Enter a number: "))
    numbers.append(n)

print("Average is: " + str(average(numbers)))
