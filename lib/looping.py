#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 11
    while count > 0:
        count -= 1
        print(count)
        print("Happy New Year!")

def square_integers(int_list):
    squared = []
    for num in int_list:
        squared_num = num * num
        squared.append(squared_num)  
    return squared

def fizzbuzz():
    count = 0
    while count < 100:
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)
