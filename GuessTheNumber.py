#!/usr/bin/env python3.8

import random 
guessedSoFar=0

number=random.randint(1, 30)
print('Pick a number between 1 and 30')

while guessedSoFar<6:
    print('Make a guess: ')
    guess=input()
    guess=int(guess)
    guessedSoFar=guessedSoFar + 1
    if guess<number:
        print('Your guess is too low')
    if guess>number:
        print('Your guess is too high')
    if guess==number:
        break
if guess==number:
    guessedSoFar=str(guessedSoFar)
    print('you guessed the number in ' + guessedSoFar + ' guesses')
if guess!=number:
    number=str(number)
    print('too many tries. The number I was thinking of was: '+ number)
    