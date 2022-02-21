#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
import gamedata as gd
import game_art


# In[10]:


play_again = ""
full_list = []
full_list[:] = gd.data #Check the technique of making copies of 'separate' lists here: https://bit.ly/3H4ZpFT

while play_again not in ["N", "n"]:
    print(game_art.logo)
    user_guess = ""
    wrong = False
    score = 0

    a = random.choice(full_list)
    #print(a)
    full_list.remove(a)
    len(full_list)

    b = random.choice(full_list)
    #print(b)
    full_list.remove(b)
    len(full_list)

    while wrong == False and len(full_list) != 0:

        if a['description'][0] not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
        else:
            print(f"Compare A: {a['name']}, an {a['description']} from {a['country']}.")

        if b['description'][0] not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:  
            print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")
        else:
            print(f"Against B: {b['name']}, an {b['description']} from {b['country']}.")

        while user_guess not in ["A", "a", "B", "b"]:
            user_guess = input("Who has more follower? Type A or B :")

        if user_guess in ['A', 'a'] and a['follower_count'] > b['follower_count']:
            print("You are right!")
            print(f"gd.data = {len(gd.data)}")
            #print(f"full_list = {len(full_list)}")      
            score += 1
            a = b
            b = random.choice(full_list)
            full_list.remove(b)
            user_guess = ""
        elif user_guess in ['B', 'b'] and b['follower_count'] > a['follower_count']:
            print("You are right!")
            print(f"gd.data = {len(gd.data)}")
            #print(f"full_list = {len(full_list)}")
            score += 1
            a = b
            b = random.choice(full_list)
            full_list.remove(b)
            user_guess = ""
        else:
            print("You are wrong!")
            print(f"gd.data = {len(gd.data)}")
            #print(f"full_list = {len(full_list)}")
            wrong = True
            user_guess = ""

    print(f"Your score is {score}.")

    while play_again not in ["Y", "y", "N", "n"]:
        play_again = input("Play again? Y/N: ")
        
    if play_again in ['Y', 'y']:
        gd.data = list(full_list) #Replenish the fill_list list
        full_list[:] = gd.data

