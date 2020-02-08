#!/usr/bin/env python
# coding: utf-8

# In[8]:


def mean(list = []):
    total = sum(list)
    mean = (total/len(list))
    return mean

print(mean([1,2,3,4,5]))


# In[7]:



def median(list=[]):
    list.sort()
    if len(list) % 2 == 0:
        first_median = list[(len(list) // 2)]
        second_median = list[((len(list) // 2) - 1)]
        return first_median / second_median
    else :
        return list[(len(list))//2]
    
print(median([1,2,3,4,5,6,7]))


# In[9]:


def percentile(nth_percentile, list = []):
    num_of_observations = len(list)
    return (nth_percentile/100) * num_of_observations
    
print(percentile(50,[1,3,5,7]))    


# In[12]:


def standard_deviation(list = []):
    num_of_items = len(list)
    sum_of_items = sum(list)
    mean = sum_of_items/num_of_items
    variance_list = []
    for i in list:
        dispersion = (i - mean) ** 2 
        variance_list.append(dispersion)
    sum_of_variance = sum(variance_list)
    variance = sum_of_variance/num_of_items
    standard_deviation = variance ** 0.5#
    
    return standard_deviation

print(standard_deviation([1,2,3,4,5]))


# In[21]:


import statistics
def mode(list=[]):
    if len(list) !=0:
        try:
            return(statistics.mode(list))
        except:
            print("No Unique Mode")
    else:
        print("List is empty")
        
print(mode([1,2,3,3,6,4]))        


# In[ ]:


import random


print("Rock Paper Sciccors is a very simple game to play")
print("paper beats rock, rock beats scissors and scissors beats paper\ninput either rock, paper or scissors")

choice = ['paper', 'rock', 'scissors']
lives = 3
points = 0

while lives > 0:
    user_choice = input('Enter your choice: \n\n')
    computer_choice = random.choice(choice)
    print("player chooses " + str(usr_choice))
    print("Computer plays ",computer_choice)
    
    if user_choice == compyter_choice:
        print("You drew Continue")
        continue
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You won this round continue")
        points += 1
        continue
    elif user_choice == 'scissors' and computer_choice == 'rock':
        lives -= 1
        print("You have " + str(lives) + " lives left")
        continue
    elif user_choice == 'rock' and computer_choice == 'paper':
        lives -= 1
        print("You have " + str(lives) + " lives left")
        continue
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You won this round continue")
        points += 1
        continue
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You won this round continue")
        points += 1
        continue
    elif user_choice == 'paper' and computer_choice == 'scissors':
        lives -= 1
        print("You have " + str(lives) + " lives left")
        continue
    else:
            print("invalid entry\n\n")
    
if lives == 0:
    print("you lost\n you had " + str(points) + "points")


# In[ ]:





# In[ ]:





# In[ ]:




