#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

#variables
guesses = 0
guess_range = 20
print('Hello there! What is your name?')
Name = input()

#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
number = random.randint(1,guess_range)
print('Hello there! ' + Name + ', I have a number of apples in my bag between 1 and 20.')

#ask the user for a response and store it in the variable [guess]
print('Guess how many apples are in my bag. You have 5 guesses.')


try:
    while guesses < 5:
        guess = input()
        guess = int(guess)
        guesses = guesses + 1

        if guess < number:
            guesses = str(guesses)
            print('Your guess is too low. Try again. You have guessed ' + guesses + ' times.')

        if guess > number:
            guesses = str(guesses)
            print('Your guess is too high. Try again. You have guessed ' + guesses + ' times.')

        if guess == number:
            break
        guesses = int(guesses)
except ValueError:
    print('Please enter a whole number.')

if guess == number:
    guesses = str(guesses)
    print('Good job, ' + Name + ' You guessed how many apples I have in my bag in ' + guesses + ' guesses!')

if guess != number:
    number = str(number)
    print("Sorry you didn't guess correctly, I had " + number + ' apples in my bag.')


#a try/except block is a great tool for programmers to be able to deal with errors. In this instance, it reports an error if the user enters something other than an integer

