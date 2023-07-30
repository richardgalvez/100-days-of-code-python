import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

cpu_choice = random.randint(0, 2)

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

if player_choice == "0":
    print(rock)
    print("Computer chose:\n")
    if cpu_choice == 0:
        print(rock)
        print ("Draw! Try again.")
    elif cpu_choice == 1:
        print(paper)
        print("Sorry, you lost! Try again!")
    elif cpu_choice == 2:
        print(scissors)
        print("Congrats! You won!")
    else:
        print("Invalid choice, please try again and choose a valid option.")

elif player_choice == "1":
    print(paper)
    print("Computer chose:\n")
    if cpu_choice == 0:
        print(rock)
        print ("Congrats! You won!")
    elif cpu_choice == 1:
        print(paper)
        print("Draw! Try again.")
    elif cpu_choice == 2:
        print(scissors)
        print("Sorry, you lost! Try again!")
    else:
        print("Invalid choice, please try again and choose a valid option.")

elif player_choice == "2":
    print(scissors)
    print("Computer chose:\n")
    if cpu_choice == 0:
        print(rock)
        print ("Sorry, you lost! Try again!")
    elif cpu_choice == 1:
        print(paper)
        print("Congrats! You won!")
    elif cpu_choice == 2:
        print(scissors)
        print("Draw! Try again.")
    else:
        print("Invalid choice, please try again and choose a valid option.")

else:
    print("Try again.")