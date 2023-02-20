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

#Write your code below this line 👇
import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input > 2:
  print("Please enter a valid number between 0 and 2\n")
else:
  computer_choice = int(random.randint(0, 2))
  user_choice = [rock, paper, scissors]
  print(user_choice[user_input])
  print("Computer chose:")
  print(user_choice[computer_choice])
  
  if user_input == 0 and computer_choice == 1:
    print("You lose")
  elif user_input == computer_choice:
    print("It's a Tie, Play again!")
  elif user_input == 0 and computer_choice == 2:
    print("You Win!")
  elif user_input == 1 and computer_choice == 0:
    print("You Win!")
  elif user_input == 1 and computer_choice == 2:
    print("You lose")  
  elif user_input == 2 and computer_choice == 0:
    print("You lose")
  elif user_input == 2 and computer_choice == 1:
    print("You Win!")
