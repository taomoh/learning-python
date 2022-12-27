def average(_numbers):
    return sum(_numbers)/len(_numbers)


numbers = []
ask_user = True
while ask_user:
    number = float(input("Enter a number: "))
    if number == 0.0:
        ask_user = False
    else:
        numbers.append(number)

print("Average is: " + str(average(numbers)))
