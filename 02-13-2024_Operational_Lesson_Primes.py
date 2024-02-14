# Balneo CSC 02/13/2024, Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal
# 02-13-2024_Operational_Lesson_Primes.py
# prints all primes from 1 to n
# CC BY-NC-SA 4.0
# Imports 
# Variables 
# Functions
def prime_check(num):
    prime_check = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                prime_check = True
                break
    if prime_check:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# Code
prime_check(input("What is your Number? \n ►"))
