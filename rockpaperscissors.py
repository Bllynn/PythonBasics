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
# from random import randint
# computer_wins = 0
# player_wins = 0

# winning_score = int(input("Whats the winning score?"))
# print("...rock...")
# print("...paper...")
# print("...scissors...")

# while player_wins < winning_score and computer_wins < winning_score:
#     print(f"{player_wins} - {computer_wins}")
#     player = input("Player, make your move: ").lower()
#     # print("****DONT CHEAT YOU HACK!****\n\n" *20)
#     if player == "quit" or player == "q":
#         break
#     elif player != "rock" and player != "paper" and player != "scissors":
#         print("Please pick a valid move")
#     else:
#         number_move = randint(0, 2)
#         if number_move == 0:
#             computer = "rock"
#         elif number_move == 1:
#             computer = "paper"
#         else:
#             computer = "scissors"
#         print(f"computer plays {computer}")
#         if player == computer:
#             print("It's a draw!")
#         elif player == "rock" and computer != "paper":
#             print(f"player wins with {player}!")
#             player_wins += 1
#         elif player == "paper" and computer != "scissors":
#             print(f"player wins with {player}!")
#             player_wins += 1
#         elif player == "scissors" and computer != "rock":
#             print(f"player wins with {player}!")
#             player_wins += 1
#         else:
#             print(f"Computer wins with {computer}")
#             computer_wins += 1
# if player_wins > computer_wins:
#     print("Congratulations! You've won!")
# elif(player_wins == computer_wins):
#     print("Its a tie!")
# else:
#     print("You just got beat by a COMPUTER! LOSER!")




#.............................COMPUTER MOVE SHORTENED UP!..................................................
from random import randint
computer_wins = 0
player_wins = 0

winning_score = int(input("Whats the winning score?"))
print("...rock...")
print("...paper...")
print("...scissors...")

while player_wins < winning_score and computer_wins < winning_score:
    print(f"{player_wins} - {computer_wins}")
    player = input("Player, make your move: ").lower()
    # print("****DONT CHEAT YOU HACK!****\n\n" *20)
    if player == "quit" or player == "q":
        break
    elif player != "rock" and player != "paper" and player != "scissors":
        print("Please pick a valid move")
    else:
        moves=["rock","paper","scissors"]
        computer_move = moves[randint(0, 2)]
        print(f"computer plays {computer_move}")
        if player == computer_move:
            print("It's a draw!")
        elif player == "rock" and computer_move != "paper":
            print(f"player wins with {player}!")
            player_wins += 1
        elif player == "paper" and computer_move != "scissors":
            print(f"player wins with {player}!")
            player_wins += 1
        elif player == "scissors" and computer_move != "rock":
            print(f"player wins with {player}!")
            player_wins += 1
        else:
            print(f"Computer wins with {computer_move}")
            computer_wins += 1
if player_wins > computer_wins:
    print("Congratulations! You've won!")
elif(player_wins == computer_wins):
    print("Its a tie!")
else:
    print("You just got beat by a COMPUTER! LOSER!")