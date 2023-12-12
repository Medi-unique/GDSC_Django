"""Functions:
a) Write a function named greet that takes a person's name as an argument and prints a greeting message.
b) Write a function named add_numbers that takes two numbers as arguments and returns their sum.

Usage of *args:
a) Write a function named print_args that takes any number of arguments and prints them.
b) Write a function named calculate_average that takes any number of numbers as arguments and returns their average."""

def greet(name):
    print('Hello ',name)
greet('medi')

def add_numbers(num1,num2):
    return num1+num2
def print_args(*args):
    print(args)
print_args( 1,2,3,4,5)

def calculate_average(*args):
    return print(sum(args)//len(args))
calculate_average(1,2,3)


"""lambda functions

solve the following problems using lambda functions:

Example 1: Adding two numbers:
Example 2: Squaring a number:
Example 3: Checking if a number is even:"""

print((lambda a,b:a+b)(10,15))
print((lambda a:a*a)(10))
print((lambda a:  a%2 and 'odd' or 'even')(11))


"""filter functions

Example: Filtering even numbers from a list.
map function
Example: Double each number in a list.
try and catch
Example: take two numbers from the user and return the sum(validate user input)
Example: take two numbers from the users and divide the first number with the second one(try and catch division by zero error)"""

nums=[0,1,2,3,4,5,6,7,8,9,10]
def is_even(num):
    if num%2==0:
        return True
even=list(filter(is_even,nums))
print(even)

double=list(map((lambda i:i*2 ),nums))
print(double)
try:
    x1,x2=map(int,input().split())
    print(x1+x2)
except ValueError:
    print('non digit value error')
    
try:
    x1,x2=map(int,input().split())
    print(x1/x2)
except ZeroDivisionError:
    print('0 division error')
    

