#!/usr/bin/env python3
"""Felicia Kenney- Project 1 - IF Conditionals"""

from os import lseek


def main():
    #gets users input for ideal location
    location = input('What\'s your ideal holiday location?: \n 1. Somewhere sunny! \n 2. Somewhere dark and moody. \n 3. Somewhere everyone can get to! \n 4. Somewhere solitary \n')
    
    #user input for whether they cheat
    cheat = int(input('\nDo you cheat in a class test?: \n 1. All the time! \n 2. Only if I\'m really stuck..\n 3. I try not to but sometimes I do \n 4. Never! \n'))

    #user input for whether they cheat
    job = int(input('\nWhat\'s your preferred job?: \n 1. Something that will make me a star! \n 2. Something in a cosy office \n 3. Something really creative \n 4. I won\'t need a job, I\'ll steal everything I need... \n'))

    hobbies= int(input('\nWhat do you do in your free time?: \n 1. Study of course! \n 2. I play sports/workout \n 3. I watch loads of TV... \n 4. Nothing, to be honest\n'))

    alone = int(input('Do you prefer...: \n 1. Time alone \n 2. Time with friends\n'))
if __name__ == "__main__":
        main()