"""
Filename: <>
Author: <Schuyler, Cole>
Created: <10/30/2026>
Instructor: Burgess
"""

import random

#prints a random integer between 1 & 100

num = random.randint(1,100)
print(num)


guess=int(input("Ask the player to enter a number on each attempt "))


if guess > num:
    print("Too high! Try again.")
elif guess < num:
    print("Too low! Try again.")
elif guess == num:
    print("Correct! You guessed the number!")