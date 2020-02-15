'''


QUESTION 1


'''

from math import sqrt, ceil

def mean(leest):
	return sum(leest)/len(leest)
	
def median(leest):
	leest = sorted(leest)
	return (leest[len(leest)//2] + leest[~(len(leest)//2)])/2
		
def mode(leest):
	return max(set(leest), key=leest.count)
    
def stdv(leest):
	mn = mean(leest)
	return sqrt(sum((x - mn)**2 for x in leest) / len(leest))
	
def percentile(leest, percentile):
    size = len(leest)
    return sorted(leest)[int(ceil((size * percentile) / 100)) - 1]

x = [2,3,2,1,23,123,123,123,14,2,456,45,45,46,3]
print(mean(x), median(x), mode(x), stdv(x), percentile(x, 10))


'''


QUESTION 2


'''

import random

life = 3
ah = ["rock", "paper", "scissors"]
while life > 0:
	try:
		uh = str(input("Enter your choice: "))
		ch = ah[random.randint(4,3000)%3]
		print("computer plays", ch)
		if ah.index(uh) > ah.index(ch):
			print("you won this round\n\n")
			life += 1
		elif ah.index(ch) > ah.index(uh):
			life -= 1
			print("You have", life, "lives left\n\n")
		elif ah.index(ch) == ah.index(uh):
			print("you drew\n\n")
	except:
		pass
