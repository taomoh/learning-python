country_capitals = {
"Morocco": "Rabat",
"Scotland": "Edinburgh",
"France": "Paris",
"Qatar": "Doha"
}

import random

while True:
    countries = list(country_capitals.keys())
    country = random.choice(countries)
    correct_capital = country_capitals[country]
    guessed_capital = input("What is the capital of '" + country + "'? ")
    
    if guessed_capital == 'quit':
        break
    elif guessed_capital == correct_capital:
        print("Correct!")
    else:
        print("Oops! The capital of " + country + " is: " + correct_capital)

print("Goodbye!")
