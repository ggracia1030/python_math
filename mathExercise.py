import os
from random import *

name = ""
score = 0
tries = 0
corrects = 0

def check_operation(num1, num2, operation, result):
    returnValue = False
    if operation == 0:
        if int(result) == (num1 + num2):
            print("Correct Answer!")
            returnValue = True
        else:
            print("Wrong Answer. The result is: " + str(num1 + num2))
    elif operation == 1:
        if int(result) == (num1 - num2):
            print("Correct Answer!")
            returnValue = True
        else:
            print("Wrong Answer. The result is: " + str(num1 - num2))
    else:
        if int(result) == (num1 * num2):
            print("Correct Answer!")
            returnValue = True
        else:
            print("Wrong Answer. The result is: " + str(num1 * num2))

    return returnValue

def new_operation(num1, num2, operation):
    if operation == 0:
        result = input("What is: " + str(num1) + " + " + str(num2) + "?")
    elif operation == 1:
        result = input("What is: " + str(num1) + " - " + str(num2) + "?")
    else:
        result = input("What is: " + str(num1) + " * " + str(num2) + "?")

    return result

def save_file(name, score, tries, corrects):
    with open("save.txt", 'w+') as file_object:
        temp_string = name + '\n' + str(score) + '\n' + str(tries) + '\n' + str(corrects)
        file_object.write(temp_string)

def load_file():
    global name
    global score
    global corrects
    global tries

    with open("save.txt", 'r') as file_object:
        name = file_object.readline()
        score = int(file_object.readline())
        tries = int(file_object.readline())
        corrects = int(file_object.readline())

def main():
    global name
    global score
    global corrects
    global tries

    exists = os.path.isfile("save.txt")

    if exists:
        load_file()
    else:
        name = input("What is your name?: ")

    print("\nWelcome " + name)

    gameOn = True
    while gameOn:
        print("---------------------------------")
        print("Your current SCORE is: " + str(score))
        print("Tries: " + str(tries))
        print("Corrects: " + str(corrects))

        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operation = randint(0, 2)
        result = new_operation(num1, num2, operation)

        if result == "bye":
            gameOn = False
            save_file(name, score, tries, corrects)
            print("\nGood bye " + name)
        else:
            tries += 1
            if check_operation(num1, num2, operation, result):
                score += 2
                corrects += 1
            else:
                score -= 1

main()

