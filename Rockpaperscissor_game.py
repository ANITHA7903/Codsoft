import random

user_turn = input("Enter a choice (rock, paper, scissors): ")
possible_turn = ["rock", "paper", "scissors"]
computer_turn = random.choice(possible_turn)
print(f"\nYou chose {user_turn}, computer chose {computer_turn}.\n")

if user_turn == computer_turn:
    print(f"Both players selected {user_turn}. It's a tie!")
elif user_turn == "rock":
    if computer_turn == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_turn == "paper":
    if computer_turn == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_turn == "scissors":
    if computer_turn == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
