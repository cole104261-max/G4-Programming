"""
Filename: conditional_calculator.py
Author: <Schuyler, Cole>
Created: <10/6/2026>
Instructor: Burgess
"""

print("Welcome to Conditional Calculator")

print("The calculator will then perform only the operation that the user requested. If the user enters an operation that the calculator does not support, then tell the user that the function is not supported.")

n1=int(input("Enter the first number: "))
op=(input("Enter the operation(+, -, *, /): "))
n2=int(input("Enter the second number: "))

if op=="+":
    print(f"{n1} + {n2} = {n1 + n2}")

elif op=="-":
    print(f"{n1} - {n2} = {n1-n2}")

elif op=="*":
    print(f"{n1} * {n2} = {n1 * n2}")

elif op=="/":
    print(f"{n1} / {n2} = {n1 / n2}")

print("Thank you for using Conditional Calculator")