#!/usr/bin/env python3.8
from random import randint 
t=['rock', 'paper', 'scissors']
computer=t[randint(0,2)]
player= False
while player ==False:
    player=input('rock, paper, scissors? ')
    if player==computer:
        print('it"s a tie!')
    elif player =='rock':
        if computer=='paper':
            print('You lose!', computer, 'covers', player)
        else:
            print('you win')
    elif player=='paper':
         if computer == "scissors":
            print("You lose!", computer, "cut", player)
         else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player==False
    computer=t[randint(0,2)]