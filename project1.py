#!/usr/bin/env python3
"""Felicia Kenney- Project 1 - IF Conditionals"""

#imports
from random import randint
from colorama import Fore, init

#auto resets print color after it is used
init(autoreset=True)

def main():

    #boolean values for valid user input
    valid_location_input = False
    valid_cheat_input = False
    valid_job_input = False
    valid_hobby_input = False
    valid_friend_input = False

    #starting value for each house
    houses = { 'gryphindor' : 0 , 'hufflepuff' : 0 , 'ravenclaw': 0, 'slytherin' : 0 }

    decision = []

    #prints banner
    print("\n=========================================  HOGWARTS SORTING HAT  =======================================================================")
    print(Fore.BLUE +"\nSorting Hat: There\'s nothing hidden in your head the Sorting Hat can\'t see.....So try me on and I will tell you Where you ought to be.\n")
    
    #------------------- QUESTION 1 ---------------------------------

    #Ask first question until a valid input 
    while not(valid_location_input):
        location = input('Q1. What\'s your ideal holiday location?: \n 1. Somewhere sunny! \n 2. Somewhere dark and moody. \n 3. Somewhere everyone can get to! \n 4. Somewhere solitary \n')
        valid_location_input = location == '1' or location == '2' or location == '3' or location == '4'
        
        # if not valid ask for valid input
        if not (valid_location_input):
            print( Fore.RED + "Please enter a valid number of 1, 2, 3, or 4")

    #Calculates points for Question 1
    if location == '1':
        houses['hufflepuff'] += 1
    elif location == '2':    
        houses['slytherin'] += 1
    elif location == '3':  
        houses['gryphindor'] += 1
    else:    
        houses['ravenclaw'] += 1 


    #------------------- QUESTION 2 ---------------------------------

    #ask question 2 until a valid input is entered
    while not (valid_cheat_input):
       
        #user input for whether they cheat
        cheat = input('\nQ2. Do you cheat in a class test?: \n 1. All the time! \n 2. Only if I\'m really stuck..\n 3. I try not to but sometimes I do \n 4. Never! \n')
        valid_cheat_input = cheat == '1' or cheat == '2' or cheat == '3' or cheat == '4'

        # if not valid ask for valid input
        if not (valid_cheat_input):
            print( Fore.RED + "Please enter a valid number of 1, 2, 3, or 4")

    #Calculates points for Question 2
    if cheat == '1':
        houses['slytherin'] += 1
    elif cheat == '2':   
        houses['gryphindor'] += 1
    elif cheat == '3':  
        houses['ravenclaw'] += 1
    else: 
        houses['hufflepuff'] += 1
 

    #------------------- QUESTION 3 ---------------------------------

    #ask question 3 until a valid input is entered
    while not (valid_job_input):
        #ask user for preferred job
        job = input('\nQ3. What\'s your preferred job?: \n 1. Something that will make me a star! \n 2. Something in a cosy office \n 3. Something really creative \n 4. I won\'t need a job, I\'ll steal everything I need... \n')
        valid_job_input = job == '1' or job == '2' or job == '3' or job == '4'
        
        # if not valid ask for valid input
        if not (valid_job_input):
            print( Fore.RED + "Please enter a valid number of 1, 2, 3, or 4")

    #Calculates points for Question 3
    if job == '1':
        houses['gryphindor'] += 1
    elif job == '2':   
        houses['hufflepuff'] += 1 
    elif job == '3':  
        houses['ravenclaw'] += 1  
    else: 
        houses['slytherin'] += 1

    #------------------- QUESTION 4 ---------------------------------    
    while not(valid_hobby_input):
        #ask user for hobbies
        hobbies= input('\nQ4. What do you do in your free time?: \n 1. Study of course! \n 2. I play sports/workout \n 3. I watch loads of TV... \n 4. Nothing, to be honest\n')
        valid_hobby_input = hobbies == '1' or hobbies == '2' or hobbies == '3' or hobbies == '4'
         # if not valid ask for valid input
        if not(valid_hobby_input):
            print( Fore.RED + "Please enter a valid number of 1, 2, 3, or 4")

    #Calculates points for Question 4
    if hobbies == '1':
        houses['ravenclaw'] += 1  
    elif hobbies == '2':   
        houses['gryphindor'] += 1 
    elif hobbies == '3':  
        houses['slytherin'] += 1  
    else: 
        houses['hufflepuff'] += 1     

    #------------------- QUESTION 5 ---------------------------------    
    while not(valid_friend_input):
        
        #ask user for qualities in friend
        friends = input('Q5. What qualities do you look for in a friend?: \n 1. Wisdom \n 2. Loyalty\n 3. Trustworthiness \n 4. Can I use them for my own gain?\n')
        valid_friend_input = friends == '1' or friends == '2' or friends == '3' or friends == '4'
        
         # if not valid ask for valid input
        if not(valid_friend_input):
            print( Fore.RED + "Please enter a valid number of 1, 2, 3, or 4")

    #Calculates points for Question 5
    if friends == '1':
        houses['ravenclaw'] += 1
    elif friends == '2':   
        houses['hufflepuff'] += 1
    elif friends == '3':  
        houses['gryphindor'] += 1
    else: 
        houses['slytherin'] += 1  

    #-------------- FINAL DECISION ---------------------------

    #Gets the max value from the houses dictionary
    max_value = max(houses.values())
    
    #Loops through all of the values stores values that are equal to max in decision list
    for key in houses:
            if houses[key] == max_value:
                decision.append(key)

    # if there are two HOUSES contain the same value then it randomly removes one           
    if len(decision) > 1:

        #prints out the two Tied decisions
        print(f"{Fore.BLUE} Hmmm I\'m having trouble deciding should it be {decision[0]} or {decision[1]}")
        
        #random number 
        random = randint(0 , len(decision)-1)

        #removes random number from the decision
        decision.remove(decision[random])
    
    else:
       # if decision is not longer than 1 then it prints message
       print(f"{Fore.BLUE} I know just the house for you...")

    print(Fore.GREEN + decision[0].upper())   
    
if __name__ == "__main__":
        main()