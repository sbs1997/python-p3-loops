#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")
# happy_new_year()
    

def square_integers(int_list):
    result = []
    for num in int_list:
        result.append(num**2)
    return result

def fizzbuzz():
    x = 1
    while x<=100:
        if not x%3:
            if not x%5:
                print("FizzBuzz")
            else: print("Fizz")
        elif not x%5:
            print("Buzz")
        else: print(x)
        x += 1 
fizzbuzz()
