def max(_numbers):
    m = 0
    for number in _numbers:
        if number > m:
            m = number
    return m


file = open("numbers.txt", "r")

numbers = []
for line in file:
    strings = line.split(",")
    for string in strings:
        numbers.append(float(string))

maximum = max(numbers);

print("Maximum is: " + str(maximum))
