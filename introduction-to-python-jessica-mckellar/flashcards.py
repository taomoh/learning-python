import random
import sys

f = open("country_capitals.txt", "r")

questions = {}

for line in f:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    questions[question] = answer
    
while True:
    _questions = list(questions.keys())
    question = random.choice(_questions)
    correct_answer = questions[question]
    actual_answer = input(question + " ")
    
    if actual_answer == 'quit':
        break
    elif actual_answer == correct_answer:
        print("Correct!")
    else:
        print("Oops! Correct answer is: " + correct_answer)

print("Goodbye!")
