import random

# This is a Rock Paper Scissors game
#rock = ('rock','scissors')
#paper = ('paper','rock')
#scissors = ('scissors','paper')

life = 3
def begin():
	game = ('Rock', 'Paper', 'Scissors')
	point = 0
	player = input('Enter your choice: ')
	if player == 'Rock' or 'rock':
		comp = random.choices(game)
		if comp == 'Paper':
			print ('Computer played Paper')
			#Paper covered Rock
			print ('Computer wins')
			life = life - 1

		elif comp == 'Scissors':
			print ('Computer played Scissors')
			#Rock smashed Scissors
			print ('Player wins')
			point = point + 1

		elif comp == 'Rock':
			print ('Computer played ', comp)
			#Paper covered Rock
			print ("It's a draw")

	elif player == 'Paper' or 'paper':
		comp1 = random.choices(game)
		if comp1 == 'Paper':
			print ('Computer played Paper')
			print ('Its a draw')

		elif comp1 == 'Scissors':
			print ('Computer played Scissors')
			#Rock smashed Scissors
			print ('Computer wins')
			life = life - 1

		elif comp1 == 'Rock':
			print ('Computer played Rock')
			#Paper covered Rock
			print ("Player wins")
			point = point + 1

	elif player == 'Scissors' or 'scissors':
		comp2 = random.choices(game)
		if comp2 == 'Paper':
			print ('Computer played Paper')
			#Scissors cuts paper
			print ('Player wins')
			point = point + 1

		elif comp2 == 'Scissors':
			print ('Computer played Scissors')
			print ('Its a draw')

		elif comp2 == 'Rock':
			print ('Computer played Rock')
			#Rock smashed scissors
			print ("Computer wins")
			life = life - 1

while life != 0:
	begin()

if life == 0:
    print ('Game over!')
    if point <= 1:
        print ('You have {} point'.format(point))
    elif point > 2:
        print ('You have {} points'.format(point))
        



	
