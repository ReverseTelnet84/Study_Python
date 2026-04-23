import random
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

rock_paper_scissors = [rock, paper, scissors]
user_select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_select = random.randint(0,2)

print(rock_paper_scissors[user_select])

if user_select >= 3 or user_select < 0:
    print("You typed an invalid number. You lose!")

elif user_select == computer_select:
    print("Computer chose:")
    print(rock_paper_scissors[int(computer_select)])
    print("It's a draw")

elif user_select == 0:
    if computer_select == 1:
        print("Computer chose:")
        print(rock_paper_scissors[int(computer_select)])
        print("You lose")
    else:
        print("Computer chose:")
        print(rock_paper_scissors[int(computer_select)])
        print("You win!")

elif user_select == 1:
    if computer_select == 2:
        print("Computer chose:")
        print(rock_paper_scissors[int(computer_select)])
        print("You lose")
    else:
        print("Computer chose:")
        print(rock_paper_scissors[int(computer_select)])
        print("You win!")
else:
    if computer_select == 0:
        print("Computer chose:")
        print(rock_paper_scissors[int(computer_select)])
        print("You lose")
    else:
        print("Computer chose:")
        print(rock_paper_scissors[int(computer_select)])
        print("You win!")
