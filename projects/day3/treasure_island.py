print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

first_choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if first_choice == "right":
    print("You fell into a hole! Game over.")
elif first_choice == "left":
    second_choice = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if second_choice == "swim":
        print("You drowned! Game over!")
    elif second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if third_choice == "blue":
            print("You enter a room full of angry beasts. Game over!")
        elif third_choice == "red":
            print("Ahh! There's fire everywhere and you are engulfed in flames. Game over!")
        elif third_choice == "yellow":
             print("A shining light shows you the path to the room full of glorious treasure, you're rich! You win!!!")