'''
Author: Rapha Jacobson
Description: Preforms 7 different actions (involving numbers) through recursive functions
Bonuses: gdp function
Bugs: in fibonacci's sequence, if you enter a number over 35, it will severely lag
Log: 1.0
'''


def factorial(n):
    '''
    Description: calculate the factorial of a number
    Args:
        n - number inputted by user
    returns:
        factorial of n
    '''
    if n == 0:
        return 1
    return n * factorial(n - 1)

def summation(n):
    '''
    Description: Calculate the summation of a number
    Args:
        n - number inputted by user
    returns:
        summation of n
    '''
    if n == 0:
        return 0
    return n + summation(n - 1)

def powers(a, n):
    '''
    Description: find the sum of any number to any power
    Args:
        a - base inputted by user
        n - power inputted by user
    returns:
        a to the nth power
    '''
    if n == 0:
        return 1
    return a * powers(a, n - 1)

def sum_of_a_numbers_digits(n):
    '''
    Description: find the sum of a number's digits
    Args:
        n - number inputted by user
    returns:
        a to the nth power
    '''
    if n < 10:
        return n
    return sum_of_a_numbers_digits(n//10) + n%10     #n mod 5 + function with paramaters of n + 10 (mod is the remainder)

def fibonacci(n):
    '''
    Description: calculate a number in  fibonacci's sequence
    Args:
        n - number inputted by user
    returns:
        How many times it needs to go through fibonacci's sequence to get to that number
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)      #fibonacci's sequence

def gcd(x, y):
    '''
    Description: find the greatest common denominator of any 2 numbers
    Args:
        x - number inputted by user
        y - number inputted by user
    returns:
        the greates common factor of x and y
    '''
    if y <= x and x%y == 0:
        return y
    return gcd(y, x%y)
   
def product_of_2_numbers(a, b):
    '''
    Description: find the product of any 2 numbers
    Args:
        a - number inputted by user
        b - number inputted by user
    returns:
        a times b
    '''
    if b == 0:
        return 0
    if b > 0:
        return a + product_of_2_numbers(a, b-1)

def main():
    while True:
        inp = input("Which option would you like to choose? (enter the number) (enter 'x' to quit) \n" \
        "1. find the factorial of a number\n"
        "2. find the summation of a number\n"
        "3. find the number to the power of another number\n"
        "4. find the sum of a number's digits\n"
        "5. enter a number you would like to evaluate in terms of fibonacci's sequence \n" \
        "6. find the greatest common denominator of 2 numbers\n"
        "7. find the product of 2 numbers\n"
        ": ")
        if inp == "1":                                  #preform factorial function if user chooses option 1
            fac = input("Which number would you like to find the factorial of?: ")
            try:
                print(factorial(int(fac)))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == "2":                                  #preform summation function if user chooses option 2
            sum = input("Which number would you like to find the summation of?: ")
            try:
                print(summation(int(sum)))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == "3":                                  #preform powers function if user chooses option 3
            avalue = input("What number would you like to be the base?: ")
            nvalue = input("What number would you like to raise the base to?: ")
            try: 
                print(powers(int(avalue), int(nvalue)))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == "4":                                  #preform sum of a numbers digit function if user chooses option 4
            num = input("Enter any number: ")
            try:
                print(sum_of_a_numbers_digits(int(num)))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == "5":                                  #preform fibonacci function if user chooses option 5
            num = input("input any number: ")
            try:
                print(fibonacci(int(num)))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == "6":                                  #preform gcd function if user chooses option 6
            num1 = input("input any number: ")
            num2 = input("input a second number: ")
            try:
                print(gcd(int(num1), int(num2)))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == "7":                                  #preform product of 2 numbers function if user chooses option 7
            num1 = input("input one number: ")
            num2 = input("input a second number: ")
            num1 = int(num1)
            num2 = int(num2)
            try:
                print(product_of_2_numbers(num1, num2))
                continue
            except ValueError:
                print("please enter a number.")
            continue
        elif inp == 'x':                                  #end program if user enters 'x'
            quit() 
        else:
            print("invalid input - please try again.")
            continue
            
main()
