# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:16:55 2020

@author: Raynier
"""
import random

NumChances = 5;
NumMaxLimit = 10;

    

def guess(x):
    n = random.randint(1,x)
    print(f"\nI Have Chosen My Number. You Have {NumChances} Chance To Guess It Correctly. Your Guess Must Be Between 1 to {NumMaxLimit}")
    for i in range(NumChances):
        g = int ( input(f"(Chance No {i+1}) Enter Your Guess: ") )
        if g>n:
            print("Your Guess is Higher")
        elif g<n:
            print("Your Guess is Lower")
        elif g==n:
            print("You Won !!!!! ")
            break

def computerGuess(x):
    print(f"\nComputer Has {NumChances} Chance To Guess It Correctly")
    input(f"\nThink of a number between 1 to {NumMaxLimit} Press R when Ready : ")
    low = 1
    high = x
    for i in range(NumChances):
        g = random.randint(low,high)
        feedback = input(f"Is {g} High(H) or Low(L) or Correct(C): ")
        if feedback == 'C':
            print("Computer Won !!!!! ")
            return
        elif feedback == 'H':
            high = g-1;
        elif feedback == 'L' :
            low = g+1;
    print("You Won !!!!!!")
        
    
if __name__ == "__main__":
    
    print('_____________WELCOME TO THE NUMBER GUESSING GAME___________')
    C = input("If you want to guess the computers number enter Y (or) If you want computer to guess your number Enter N : ")
    
    if C=='Y':
        guess(NumMaxLimit)
    elif C=='N':
        computerGuess(NumMaxLimit)
    else:
        print("You Entered a Wrong Choice") 