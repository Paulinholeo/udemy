print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1, make your move: ")
player2 = input("Player2, make your move: ")

if player1 == player2:
    print ("its a tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("player 1 wins!")
    elif player2 == "paper":
        print("player2 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    elif player2 == "scissors":
         print("player2 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins")
    elif player2 == "paper":
        print("player1 wins")
else:
    print ("something went wrong")


     