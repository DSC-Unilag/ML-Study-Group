import math
import random

def mean(n):
	""" Computes the mean value of a list of parameter n """
	total = 0
	for i in n:
		total += i

	return total/len(n)

def median(n):
	""" Computes the median value of a list of parameter n """
	n.sort()
	length_of_n = len(n)

	if length_of_n%2==0:
		after = length_of_n//2
		average = n[after-1] + n[after]

		return average/2
	else:
		return n[length_of_n//2]

def mode(n):
	""" Computes the most occuring value of a list of parameter n """

	nSet = set(n)
	modeVal = 0
	modeNum = n[0]
	for i in nSet:
		if(modeVal < n.count(i)):
			modeNum = i
			modeVal = n.count(i)

	return modeNum

def standard_deviation(n):
	""" Computes the standard deviation of a list of parameter n """
	top = 0
	average = mean(n)
	for i in n:
		top += pow(i-average, 2)

	return(math.sqrt(top/(len(n))))




#############  This is the rock scissor player game   #############

userGuess = input("Pick your game. Select 1 for rock, 2 for scissor, 3 for paper: ")
outcomesDic = {1:'rock', 2:'scissor', 3:'paper'}
outcomesList = ['rock', 'scissor', 'paper']

try:
	userGuess = outcomesDic[eval(userGuess)]
except Exception as e:
	# Randomly choosing an option for the user because he went out of box
	val = random.randint(1,3)
	print("You have chosen out of the options and {} have been selected for you".format(val))

userLive = 3
userPoint = 0
gameSwitch = True


computerGuess = random.choice(outcomesList)
while gameSwitch:
	if(userGuess=='rock' and computerGuess=='scissor'):
		userPoint += 1
		print("You win because computer plays scissor")
	elif(userGuess=='scissor' and computerGuess=='rock'):
		userLive -= 1
		print("You lost to the computer because it plays rock")
		print("You have {} live remaining".format(userLive))

	elif(userGuess=='paper' and computerGuess=='rock'):
		userPoint += 1
		print("You win because computer plays rock")
	elif(userGuess=='rock' and computerGuess=='paper'):
		userLive -= 1
		print("You lost to the computer because it plays paper")
		print("You have {} live remaining".format(userLive))

	elif(userGuess=='scissor' and computerGuess=='paper'):
		userPoint += 1
		print("You win because computer plays paper")
	elif(userGuess=='paper' and computerGuess=='scissor'):
		userLive -= 1
		print("You lost to the computer because it plays scissor")
		print("You have {} live remaining".format(userLive))
	else:
		print("This round is a draw because you guessed same thing as the computer")



	if(userLive<1):
		print("Game over! You scored {}".format(userPoint))
		break;

	print() # Creating a space between rounds of the game
	userGuess = input("Pick your game. Select 1 for rock, 2 for scissor, 3 for paper: ")
	try:
		userGuess = outcomesDic[eval(userGuess)]
	except Exception as e:
		# Randomly choosing an option for the user because he went out of box
		val = random.randint(1,3)
		print("You have chosen out of the options and {} have been selected for you".format(val))

	computerGuess = random.choice(outcomesList)
