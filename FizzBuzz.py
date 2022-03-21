import sys

#Create a range of values between 1 and 100.
numbers = range(1, 101)

#Create an iterative loop that cycles the values and prints Fizz, Buzz or FizzBuzz 
#based on weather the number is divisible by 3, 5 or both. The correct value is then displayed
#via the print function.
for number in numbers:
    if number % 5==0 and number % 3==0:
        print("FizzBuzz")
    elif number % 3==0:
        print("Fizz")
    elif number % 5==0:
        print("Buzz")
    else:
        print(number)
