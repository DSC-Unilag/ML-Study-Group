def Mean(List):
    '''
        This function takes in a list of numbers and returns their mean.
    '''
    return sum(List)/len(List)
def Median(List):
    '''
    This function takes in a list of numbers and returns the median number.
    '''
    List = sorted(List)
    a = len(List)//2
    if len(List)%2 == 0:
        return (List[a-1]+List[a])/2
    else:
        return List[a]

def Standard_deviation(List):
    '''
    this function takes in a list of numbers and returns the standard deviation of the array of numbers.
    '''
    N = len(List)
    dev = sum([(i-Mean(List))**2 for i in List])
    if N < 50 :
        '''
        When data is from the entire Population
        '''
        return (dev/N)**(1/2)
    else:
        '''
        When data is just a sample
        '''
        return (dev/(N-1))**(1/2)

def Percentiles(frac,List):
    '''
    This function takes in the percentile desired and the ordered/unordered array of numbers and returns
    the element in the array which is at the desired percentile.
    '''
    List.sort()
    n= len(List)
    R = ((frac/100)*n) - 1
    print(R)
    if R%1 ==0 :
        ind = int(R)
        return (List[ind]+List[ind+1])/2
    else:
        ind = int(R//1 +1)
        return (List[ind])
#print(Percentiles(50,[43,54,56,61,62,66,68,69,69,70,71,72,77,78,79
# ,85,87,88,89,93,95,96,98,99,99]))

def RPS(Player1,Player2):
    '''This function takens in the entry of both players and
    returns the identity of the player that wins (Player1 or Player2)
    Note that:
    Rock > scissors but Rock < paper
    Paper > rock but Paper <scissors
    Scissors> paper but Scissors < rock
    '''
    play = ['scissors', 'paper', 'rock']
    Player1 = Player1.lower()
    Player2  = Player2.lower()
    a = play.index(Player1)
    b = play.index(Player2)
    if a== b+1:
        return 'Player Two wins'
    elif a+1 ==b:
        return 'Player One wins'
    elif a==b:
        return "It's a draw, play again..."
    elif a+2 == b:
        return 'Player Two wins'
    elif a ==b+2:
        return 'Player One wins'



'''
print(RPS('Paper','scissors'))
print(RPS('Rock','paper'))
print(RPS('Rock','scissors'))
print(RPS('scissors','Paper'))
print(RPS('rock','ROCk'))
print(RPS('Scissors', 'Rock'))

'''

