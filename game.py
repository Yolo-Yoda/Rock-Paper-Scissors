import random
import sys

name = input('Enter your name: ')
print('Hello,', name)
file_rating = open('rating.txt', 'r+', encoding='utf-8')
dict_rating = {}
lines = file_rating.read().splitlines()
for line in lines:
    key, value = line.split(' ')
    dict_rating.update({key:value})
if name in dict_rating:
    rating = int(dict_rating[name])
else:
    rating = 0
file_rating.close()
list_a = input()
if list_a == '':
    list_a = ['rock', 'paper', 'scissors']
else:
    list_a = list(list_a.split(','))
print("Okay, let's start")
winning_results = {'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                   'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
                   'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
                   'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
                   'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
                   'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
                   'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
                   'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
                   'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
                   'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
                   'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
                   'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
                   'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
                   'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
                   'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lighting']}
user_pick = input()
while user_pick != '!exit':
    comp_pick = random.choice(list_a)
    if user_pick in list_a:
        if comp_pick == user_pick:
            print('There is a draw ({})'.format(comp_pick))
            rating = rating + 50
            user_pick = input()
        elif comp_pick in winning_results[user_pick]:
            print('Well done. The computer chose {} and failed'.format(comp_pick))
            rating = rating + 100
            user_pick = input()
        else:
            print('Sorry, but the computer chose {}'.format(comp_pick))
            user_pick = input()
    elif user_pick == '!rating':
        print('Your rating:', rating)
        user_pick = input()
    else:
        print('Invalid input')
        user_pick = input()
print('Bye!')
sys.exit()
















