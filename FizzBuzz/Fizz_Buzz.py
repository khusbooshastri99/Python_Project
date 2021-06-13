"This program will print 'fizz and buzz" for numbers divisible by 3 and 5 respectively and 'fizzbuzz' for both."


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        
    elif number % 3 == 0:
        print("Fizz")
        
    elif number % 5 == 0:
        print("Buzz")
        
    else:
        print(number)
