"""
Filename: trivia_game.py
Author: <Schuyler, Cole>
Created: <10/8/2026>
Instructor: Burgess
"""
#Answered Correctly: 10
Correct=0

#Total score: 20
Score=0


x=input("What is the default data type for numbers in Python?")
if x =="none":
    Score+=2
    Correct+=1
    print("Correct")
x=input("What month is Hitler's birthday?")
if x =="April":
    Score+=2
    Correct+=1
    print("Correct")
x=input("How many hours are in a school day?")
if x =="Seven":
    Score+=2
    Correct+=1
    print("Correct")
x=input("How many football players are allowed on the field on each sides?")
if x =="Eleven":
    Score+=2
    Correct+=1
    print("Correct")
x=input("How many states are in the United States?")
if x =="Fifty":
    Score+=2
    Correct+=1
    print("Correct")
