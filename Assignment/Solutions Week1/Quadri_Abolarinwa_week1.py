"""
author = QUADRI, Abolarinwa (BoffinBee)
github_link = (http://github.com/BoffinBee)
"""


#this function calculates the mean of the given set of numbers
def evaluate_mean(numbers):
    numbers_sum = 0
    for number in range(len(numbers)):
        numbers_sum += numbers[number]
    mean_value = numbers_sum/len(numbers)
    return mean_value


#this function determines the median of the set of numbers
def evaluate_median(numbers):
    numbers.sort()
    if len(numbers)%2 == 1:
        return numbers[len(numbers)//2]
    else:
        return (numbers[len(numbers)//2])+(numbers[(len(numbers)//2)-1])/2


#function evaluating the most occurent in the set
def evaluate_mode(numbers):
    mode = numbers[0]
    for number in range(len(numbers)):
        if numbers.count(numbers[number])>numbers.count(mode):
            mode = numbers[number]
    return mode, numbers.count(mode)


#calculation of the standard deviation of the number set
def evaluate_standard_deviation(numbers):
    square_difference_sum = 0
    for number in range(len(numbers)):
        square_difference_sum += (evaluate_mean(numbers)-numbers[number])**2
    return square_difference_sum/len(numbers)


#function used to determine the first, second and third percentiles
def evaluate_percentiles(numbers):
    numbers.sort()
    first_percentile = numbers[round(25/100*len(numbers))]
    second_percentile = numbers[round(50/100*len(numbers))]
    third_percentile = numbers[round(75/100*len(numbers))]
    return first_percentile, second_percentile, third_percentile


#testing the computed functions with the data set below
number_list = [113, 110, 105, 60, 53, 64, 84, 78,
               106, 53, 105, 84, 109, 76, 2, 46, 87, 95,
               102, 67, 83, 73, 74, 23, 73, 126, 107, 117, 24, 50, 92, 57,
               92, 105, 81, 44, 85, 76, 116, 20, 53, 126, 112,
               59, 105, 116, 85, 11, 122, 1, 127, 57, 105, 110, 0,
               80, 45, 53, 126, 107, 117, 24, 50, 92, 57, 15, 87,
               92, 105, 81, 70, 44, 85, 103, 126, 107, 111, 117, 
		24, 50, 92, 57, 22, 15, 81, 94, 85]


print(f'Numbers = {number_list}')
print(f'\nMean of the numbers is {round(evaluate_mean(number_list),2)}.')

print(f'\nMedian of the numbers is {round(evaluate_median(number_list),2)}.')

print(f'\nMode of the numbers is {evaluate_mode(number_list)[0]}, \
it appeared {evaluate_mode(number_list)[1]} times.')

print(f'\nStandard deviation of the numbers \
is {round(evaluate_standard_deviation(number_list),2)}.')

print(f'\nFirst, second and third percentiles of the set \
of numbers is {evaluate_percentiles(number_list)[0]}, \
{evaluate_percentiles(number_list)[1]} and \
{evaluate_percentiles(number_list)[2]} respectively.')


#################################################


#import required libraries
from random import randint as rndint
import sys


#set a list of valid objects
objects = ['Rock', 'Paper', 'Scissors']

print('\n\nRock, Paper, Scissors')
while True:
    #let computer randomly pick one of the valid objects
    computer_throw = objects[rndint(0,2)]
    
    #collect player pick
    player_throw = input('\nChoose either "Rock", "Paper" \
or "Scissors"\n------> ').title()
    
    #ask player again for a pick after an invalid selection
    while player_throw not in objects:
        player_throw = input('Your pick is invalid,\nChoose either \
"Rock", "Paper" or "Scissors"\n------> ').title()
        
    #set conditions for a tied game
    if computer_throw == player_throw:
        print('Tie!')
        
    #set conditions for player wins
    elif (computer_throw == 'Rock' and player_throw == 'Paper') or \
             (computer_throw == 'Paper' and player_throw == 'Scissors') or \
             (computer_throw == 'Scissors' and player_throw == 'Rock'):
        print('You win!')
        
    #in otherwise cases the player has lost
    else:
        print('You lost!')
        

    #enquire if player wants to go for another round
    play_again = input('\nDo you want to play again?\ \nYes = 1\nNo = 0\n------> ')
    request_command = ['0', '1']

    #if player makes an invalid request, ask to choose again
    while play_again not in request_command:
        play_again = input('Request wasn\'t understood, \nYes = 1\nNo = 0\n------> ')
    if play_again == '0':
        print('Bye, come play again!')
        sys.exit()
    elif play_again == '1':
        continue
