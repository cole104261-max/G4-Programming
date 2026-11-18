"""
Filename: n_fibonacci.py
Author: <Schuyler, Cole>>
Created: <11/18/2026>
Instructor: Burgess
"""

def n_fibonacci():
    # Write your code here
    x=int(input("input a non-negative whole number: "))



# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("Print another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()