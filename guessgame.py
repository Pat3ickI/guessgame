#importing modules
import sys
import time
import random

#version: 0.1

class Guess:
    guess = 0
    
    def __init__(self, guess, user_guess, computer_guess, ran_num):
        self.guess
        self.user_guess = user_guess
        self.computer_guess = computer_guess
        self.ran_num = ran_num
        
        
    def user_guess( x, guess_limit, guess_count=0): # create user guess 
        ran_num = random.randint(1, x)
        serect_number = ran_num # random number = serect number
        
        
        print(f'chances {guess_limit}')
        while guess_count < guess_limit: #guess limit greater than guess count
            guess = int(input(f'Guess a number between 1 and {x}: '))
            guess_count += 1 #adding 1 to guess count
            if guess_count == guess_limit-1:
                print("LAST CHANCE")
            if guess == serect_number:
                print('You Won!!! :)')
                break
            elif  guess > serect_number +2: # guess greater than serect number
                print("Too High, try again")
            elif guess < serect_number -2:
                print("Too Low, try again")
            elif guess > serect_number:
                print(" High, try again")
            elif guess < serect_number:
                print(" Low, try again")
        
        else:
            time.sleep(1)
            print(f"Oops you didnt get my secret number ({ serect_number }) ;) ")


    def computer_guess(x):
        low = 1 # lowest number 
        high = x # highest number
        feedback = " "
        guess_limit = 0
        
        try:
            while feedback != "c" and guess_limit < 4:
                if low != high: 
                    guess = random.randint(low, high)
                else:
                    guess = low
                feedback = input(f' Is {guess} too high (H), too low (L), or correct (C): ').lower()
                guess_limit += 1
                if feedback == "h":
                    high = guess - 1
                elif feedback == "l":
                    low = guess + 1

            if feedback == "c": #prints statement if won or lost
                print(f"Yay!! computer got your serect number: {guess} :) ")
            else:
                print("Oops i didn't get your serect number :(")
                print("i ran out of chances")
        except Expection as e:
            print(e) 
 
            print("INVALID RESPONSE")   

def main():
    '''main control function'''
    while True:
        user1 = input("DO YOU WANT TO PLAY FIRST YES(Y) OR NO(N): ").lower()

        if user1 == 'y':
            level = input("LEVEL: HARD (H) EASY (E): ")
            if level == 'e':
                time.sleep(1)
                Guess.user_guess(10, 3)
            elif level == 'h':
                time.sleep(1)
                Guess.user_guess(20, 4)
            else:
                print('Invalid Request')
        elif user1 == 'n':
            time.sleep(1)
            Guess.computer_guess(15)
        else:
            sys.exit()
    

if __name__ == '__main__':
    print("ver: 0.0.1")
    main()
