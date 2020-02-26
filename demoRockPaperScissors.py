#!/usr/bin/env python3
import random
game=True
rps = ['rock', 'paper', 'scissors']
rock_counter = 0
paper_counter=0
scissors_counter=0 

def better_decision ():
    
    max_counter = max(rock_counter, paper_counter, scissors_counter)
    if rock_counter== max_counter:
        return 1
    elif paper_counter==max_counter:
        return 2
    elif scissors_counter==max_counter:
        return 0
    else:
        return random.randint(0,2)


while game:

    computer_decision = better_decision()
    
    player_decision = int(input ('Make a choice: rock(0), paper(1), scissors(2): '))
    
    if player_decision==computer_decision:    
        if player_decision == 0:
            rock_counter += 1
        if player_decision == 1:
            paper_counter += 1
        if player_decision == 2:
            scissors_counter += 1    
        print ('It"s a tie!'+ ' You selected '+ rps[player_decision] + ', computer selected '+ rps[computer_decision] )
    elif player_decision==0 and computer_decision==1 :
        rock_counter += 1
        print ('You lose!' + ' You selected '+ rps[player_decision] + ', computer selected '+ rps[computer_decision] )
    elif player_decision==1 and computer_decision==2:
        paper_counter += 1
        print ('You lose!'+ ' You selected '+ rps[player_decision] + ', computer selected '+ rps[computer_decision] )
    elif player_decision==2 and computer_decision==0:
        scissors_counter += 1
        print ('You lose!'+ ' You selected ' + rps[player_decision] + ', computer selected '+ rps[computer_decision] ) 
    else:
        if player_decision == 0:
            rock_counter += 1
        if player_decision == 1:
            paper_counter += 1
        if player_decision == 2:
            scissors_counter += 1
        print('You win!'+ ' You selected '+ rps[player_decision] + ', computer selected '+ rps[computer_decision] )  

    player_session=input('Do you want to continue? (y/n): ')
    
    if player_session.lower() =='n':
        game= False
    elif player_session.lower() =='y':
        pass
    else:
        print('Please enter a valid input')

