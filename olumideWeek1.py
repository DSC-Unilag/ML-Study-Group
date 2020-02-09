# QUESTION 2

arr = list(range(1,101)) #+ [4,5,5,5,5,6,7,8,9,7,6,5,4,3,3,3,2,1,1,2,2,3,4,4,5,5]

# This fuction divides the sum of all the 
# numbers in the list by the length of the list
def mean(arr):
    return sum(arr)/len(arr)

print(mean(arr))

# this function takes in a list, sorts it and returns the
# sum of the two middle numbers divded my two if the length of the
# list is even else, it just returns the middle number
def median(arr):
    arr, listLength = sorted(arr), len(arr)
    if listLength % 2 == 0:
        return (arr[int(listLength/2)] + arr[(int(listLength/2))-1])/2
    return arr[int((listLength+1)/2)-1]

print(median(arr))

# This function checks through every number in the list and
# checks their frequencies, it then returns the number with the
# highest frequency
def mode(arr, n = 0, k = 0):
    for i in arr:
        if arr.count(i) > n:
            n = arr.count(i)
            k = i
    return k
print(mode(arr))

# this function uses pythpn equivalent of the standard deviation
# formula to get the standard deviation of a list
def standardDeviation(arr, s=0):
    mean_ = sum(arr)/len(arr)
    for i in arr:
        s += (i - mean_)**2
    return (s/len(arr))**0.5
print(standardDeviation(arr))


# this function takes in a list and the percentile as args. It then
# computes the stated percentile and returns it
def percentile(arr, p):
    p = len(arr)*(p/100)
    if p.is_integer():
        p = int(p)
        return (arr[p-1]+(arr[p]))/2
    return arr[round(p)-1]

print(percentile(arr, 80))


# QUESTION 2

import random as rnd
choiceList = ['paper', 'rock', 'scissors']

# this function compares the choice of the user to that of the 
# computer and returns the corresponding result
def check(userChoice, compChoice):
    arr, p, r, s = [userChoice, compChoice], 'paper', 'rock', 'scissors'
    winArr, drawArr = [[p, r], [s, p], [r, s]], [[p, p], [r, r], [s, s]]
    if arr in winArr: 
        result = True
    elif arr in drawArr:
        result = 'draw'
    else:
        result = False
    return result
# this function asks user for input until they run out of lives, after which 
# the number of points is displayed
def play():
    lives, points = 3, 0
    print('This is a game of rock, paper, scissors. Enter "paper", "scissors" or "rock" as a choice.\n-----------------------------------------------------')
    while lives > 0:
        computerChoice = rnd.choice(choiceList)
        userChoice = input('Enter choice: ').lower()
        result = check(userChoice, computerChoice)
        print('Computer\'s choice: {}'.format(computerChoice))
        if result == True:
            print('Great! You win this round.')
            points += 1
        elif result == "draw":
            print('ooh, it\'s a draw!\n Let\'s go again.')
        else:
            lives -= 1
            print('You lost this round!')        
        print('You have {} lives left.'.format(lives))
    print('You ended the game with {} points.'.format(points))
play()










