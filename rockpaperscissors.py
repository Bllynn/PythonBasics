# print("...rock...")
# print("...paper...")
# print("...scissors...")
# player1 = input("Player 1 make your move: ")
# print("****DONT CHEAT YOU HACK!****\n\n" *20)

# player2 = input("Player 2 make your move: ")
# if player1 == player2:
#     print("It's a draw!")
# elif player1 == "rock" and player2 != "paper":
#     print("player 1 wins!")
# elif player1 == "paper" and player2 != "scissors":
#     print("player 1 wins!")
# elif player1 == "scissors" and player2 != "rock":
#     print("player 1 wins!")
# else:
#     print("player 2 wins!")
# ..............................................................VS COMPUTER..................................................
from random import randint
print("...rock...")
print("...paper...")
print("...scissors...")
player = input("Player, make your move: ").lower()
# print("****DONT CHEAT YOU HACK!****\n\n" *20)
if player != "rock" and player != "paper" and player != "scissors":
    print("Please pick a valid move")
else:
    number_move = randint(0, 2)
    if number_move == 0:
        computer = "rock"
    elif number_move == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"computer plays {computer}")
    if player == computer:
        print("It's a draw!")
    elif player == "rock" and computer != "paper":
        print(f"player wins with {player}!")
    elif player == "paper" and computer != "scissors":
        print(f"player wins with {player}!")
    elif player == "scissors" and computer != "rock":
        print(f"player wins with {player}!")
    else:
        print(f"Computer wins with {computer}")
