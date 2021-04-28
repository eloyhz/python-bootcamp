rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

images = [rock, paper, scissors]

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
if 0 <= user <= 2:
    print(images[user])

computer = random.randint(0, 2)
print("Computer choose:")
print(images[computer])

winner = 'computer'
if user == 0 and computer == 2:
  winner = 'user'
elif user == 0 and computer == 0:
  winner = 'draw'
elif user == 1 and computer == 0:
  winner = 'user'
elif user == 1 and computer == 1:
  winner = 'draw'
elif user == 2 and computer == 1:
  winner = 'user'
elif user == 2 and computer == 2:
  winner = 'draw'

if winner == 'computer':
  print('You loose!') 
elif winner == 'user':
  print('You win!')
else:
  print("It's a draw")

