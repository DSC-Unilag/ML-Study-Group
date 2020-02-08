### Project Data Science
#### Function For Mean

def mean(lst):
  if type(lst) is list:
    Total = sum(lst)
    print(Total)
    lenght = len(lst)
    print(lenght)
    mean = Total/lenght
    return mean
  else:
    print('=== Argument is not a list ===')
    quit()

lst = list()
while True:
  numb = input('Enter any number: ')
  if numb == 'done':
    break
  num = int(numb)
  lst.append(num)
Mean = mean(lst)
print('The average value is:',Mean)

##### Project Data Science
##### Function For Median

def median(lst):
  if type(lst) is list:
    lst = sorted(lst)
    rmd = len(lst) % 2
    ##If the remainder is even!
    if rmd == 0:
      med1 = int(len(lst)/2 - 1)
      print(lst[med1])
      med2 = int(len(lst)/2)
      print(lst[med2])
      med = (lst[med1]+lst[med2])/2
      return med
    ##If the remainder is Odd!
    elif rmd == 1:
      medPos = int(len(lst)/2)
      med = lst[medPos]
      return med
x = list()    
while True:
  numb = input('Enter Number: ')
  if numb == 'done':
    break
  num = int(numb)
  x.append(num)
  
median = median(x)
print(median)

#### Project Data Science
#### Function for mode

def mode(lst):
  if type(lst) is list:
    count = dict()
    for num in lst:
      count[num] = count.get(num,0) + 1
    BigCount = None
    BigWord = None
    for num,val in count.items():
      if BigCount is None or BigCount < num:
        BigWord = num
        BigCount = val
        return BigWord
  else:
    print('====Argument not a list====')
    quit()

x = list()
while True:
  numb = input('Enter number: ')
  if numb == 'done':
    break
  num = int(numb)
  x.append(num)
mode = mode(x)
print(mode)


###Rock,Paper,Scissors Game!
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    inp = input('Press 1 to continue or Press 2 to quit: ')
    inp = int(inp)
    if inp == 1:
        continue
    elif inp == 2:
        break