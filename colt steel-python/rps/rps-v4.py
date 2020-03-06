import random

player = input("player, make your move: ").lower()

rand_num = random.randint(0, 2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print (f"computer plays {computer}")

if player == computer:
    print ("its a tie")
elif player == "rock":
    if computer == "scissors":
        print("player  wins!")
    else:
        print("computer wins")
elif player == "paper":
    if computer == "rock":
        print("player wins")
    else:
         print("computer wins")
elif player == "scissors":
    if computer == "paper":
        print("player wins")
    else:
        print("computer wins")
else:
    print ("please enter a valid move: ")


     