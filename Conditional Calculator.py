"""
Filename: conditional_calculator.py
Author: <Schuyler, Cole>
Created: <10/6/2026>
Instructor: Burgess
"""

print("Welcome to Conditional Calculator")

n1=int(input("Enter the first number: "))
op=(input("Enter the operation(+, -, *, /): "))
n2=int(input("Enter the second number: "))

if op=="+":
    print(n1+n2)
    #Code goes here
elif op=="-":
    print(n1-n2)
    #Code goes here
elif op=="*":
    print(n1*n2)
    #Code goes here
elif op=="/":
    print(n1/n2)
    #Code goes here