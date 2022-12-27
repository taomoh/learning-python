file = open("cities.txt", "r")

cities = []
for line in file:
    cities.append(line.strip())

cities.sort()

print(cities)

output = open("output.txt", "w")


for city in cities:
    output.write(city)
    output.write("\n")
