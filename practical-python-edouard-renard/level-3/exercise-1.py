def max(_numbers):
    m = 0
    for number in _numbers:
        if number > m:
            m = number
    return m


numbers = [10, 2, 5, 9]

print(str(max(numbers)))
