"""
Series of interactive python programs , by KodeCloud labs / Udemy labs examples , written with full understanding by 
Srivatsa RV , in course of practicing for coding interviews


GAME - User has to guess the index at which "O" lottery ticket is found after an inital list of values is shuffled

Example:
- Before Shuffle - [' ' , 'O', ' ', ' ']
- After Shuffle - ['O', ' ' , ' ' , ' ' ]
- User takes a guess , say index 3 (incorrect) | say index 0 (correct)
- Program also returns a hint if you go wrong, which index was the lottery ticket located. 
Credit to Section 5 - Methods and Functions from Udemy "The Complete Python Bootcamp From Zero to Hero in Python" course

Date - 3rd August 2023

"""

from random import shuffle


real_list = ['','','O','','']    #A hard-coded list initalized , to show initial placement of lottery ticket

#Create a function that shuffles the real_list and returns the mixed_list 
def mix_the_list(real_list):
    shuffled_list = real_list.copy()  #Doing this to avoid the Shuffle types None Return,  now we get Class List return
    shuffle(shuffled_list)
    return shuffled_list   #At this point , the lottery ticket has moved to a random index in the list

#Create the function that takes the user guess 
def input_user_guess():
    guess = ''
    while guess not in ['1','2','3','4']:
        guess = input('Enter your guess index: ')
    return int(guess)   
        

# #Create the function that checks the user guess
def validate_user_guess(mixed_list_result, guess_index):
    if mixed_list_result[guess_index] == 'O':
        print('Correct Guess, the O was located in', guess_index, 'position')
    else:
        for i in range(len(mixed_list_result)):
            if mixed_list_result[i] == 'O':
                print('Incorrect Guess, here is where the O was located in the following position\n', i,'\n',mixed_list_result ) 


#Welcome and mix the list
print('\nWelcome to the Lottery ticket game, we have a list here:', real_list,'\n') 
mixed_list_result = mix_the_list(real_list)

#Game is on, take user input
print('This has now been shuffled! You have to now guess which index position does the O lottery ticket sits in!\n')
guess_index = input_user_guess()

#User has guessed,  now validate the input

validate_user_guess(mixed_list_result, guess_index)


#DEBUG Statements 
# print('Array value after shuffle ',mixed_list_result) - use this to quickly check before and after shuffle value of the list
# print('Return type of mixed array ', type(mixed_list_result))  - use this to check if mixed list returned is of list type or not
# print('You have selected index as ', guess_index) = use this to see which index guest has selected
# print(type(guess_index)) - and this is to verify if the guest's selection is returned as int type so we can use it 