"""Carrot in a box, by Al Sweigart al@inventwithpython.com
A silly bluffing game between two human players, Based on the game
from the show 8 out of 10 cats.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, beginner, game, two-player"""

import random 

print('''Carrot in a Box, by Al Sweigart al@inventwithpython.com

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')
input('Press Enter to begin...')

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11) + '   ' + p2Name[:11].center(11)

print(''' HERE ARE TWO BOXES:

   ___________     __________
  /          /|   /         /|
  +---------+ |   +--------+ |
  |  RED    | |   |  GOLD  | |
  |  BOX    | |   |  BOX   | |
  +---------+/    +--------+/''')
print()
print(playerNames)
print(p1Name + ' , you have RED box in front of you.')
print(p2Name + ' , you have GOLD box in front of you.')
print()
print(p1Name + ' , you will get to look into your box.')
print(p2Name.upper() + ' , close your eyes and don\'t look!!!')
input('When ' + p2Name + ' has closed their eyes, press Enter...')
print()

print(p1Name + ' here is the inside of your box: ')

if random.randint(1, 2) == 1:
  carrotInFirstBox = True
else:
  carrotInFirstBox = False
  
if carrotInFirstBox:
  print('''
  ___W_____   
 |   W     |
 |   W     |
 |__| |____|   ___________
/   | |   /|  /          /|
+--------+ |  +---------+ |
|  Red   | |  |  Gold   | |
|  Box   | |  |  Box    | |
+--------+/   +---------+/
  (carror!)''')
     print(playerNames)
else:
  print('''
  __________
 |          |
 |          |     ______________
 |__________|    /             / |
/          /|   +-------------+  |
+---------+ |   |   GOLD      |  |
|   RED   | |   |   BOX       | /
|   BOX   | /   +-------------+/
+---------+/
(no carrot!)''')
  print(playerNames)

input('Press Enter to continue..')

print('\n' * 100) # Clear the screen by printing several newlines.
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue..')

print()
print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
print('  1) There is a carrot in my box.')
print('  2) THere is not a carrot in my box.')
print()
input('Then press Enter to continue...')

print()
print(p1Name + ', do you want to swap boxes with ' + p1Name + ' ? YES/NO')
while True:
  response = input('> ').upper()
  if not (response.startswith('Y') or response.startswith('N')):
    print(p2Name + ' , please enter "YES" or "NO".')
  else:
    break

firstBox = 'RED ' # Note the space after the "D"
secondBox = 'GOLD'

if response.startswith('Y'):
  carrotInFirstBox = not carrotInFirstBox
  firstBox, secondBox = secondBox, firstBox
 
print('''HERE ARE THE TWO BOXES:
     ____________         ___________
    /           /|       /         / |
    +----------+ |       +--------+  |
    |    ()    | |          () ||   
    |    Box   | |       |   Box   | /
    +----------+/        +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Press Enter to reveal the winner...')
print()

if carrotInFirstBox:
  print('''
  ____W_____        _________
 |    W     |      |         |
 |    W     |      |         |
 |___||_____|      |_________|
/    ||    /|     /         /|
+---------+ |    +---------+ |
|  ()  |  |         () |  |   
|  Box    | /    |   Box   | /
+---------+/     +---------+/'''.format(firstBox, secondBox))

else:
   print('''
   _________    ______W_______
  |         |  |      W       | 
  |         |  |      W       |
  |________ |  |_____||_______|
 /         /|  /     ||      /|
 +--------+ |  +------------+ |
 |  () |  |  |     ()  |  |    
 |  Box   | /  |     Box    | /
 +--------+/   +------------+/'''.format(firstBox, secondBox))
    
print(playerNames)

# This modification made possible through the 'carrInFirstBox' variable
if carrotInFirstBox:
  print(p1Name + ' is the winner!')
else:
  print(p2Name + ' is the winner!')
  
print('Thanks for playing!!')
  
