#!/usr/bin/env python3.8

guesses = []
count = 1
ans = 'python'
word = ''

while count < 10:
    guess = input ('guess a letter: ')
    guesses.append(guess)
    if ''.join(word) == ans:
        print('you win')
        break
    elif len(guess) > 1 and ans == guess:
        print(ans)
        print('you win')
        break
    else:
        for char in ans:
            if char in guesses:
                word.append(char)
                print(char)
            else:
                print('_')
        count += 1
else:
    print('\n you lose')