"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
def title():
    print("This is a number guessing game, guess a number between 0-1000, if the entered number is over, output will be over, if number guess is under, output will be under.")
title()
def game():
    import random
    count = 0
    x = random.randint(0, 1000)
    y = int(input("Enter a number between 0-1000 "))
    while y != x:
        if y > x:
            print("Over")
            y = int(input("Enter a number between 0-1000 "))
            count += 1
        elif y < x:
            print("Under")
            y = int(input("Enter a number between 0-1000 "))
            count += 1
    if y == x:
        print("You got the right number!!!")
        print(f"It took you {count} tries")
game()



