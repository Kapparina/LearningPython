import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please type 'Rock/Paper/Scissors'; type 'Tally' to see the score, or 'Q' to quit: ").lower()
    if user_input == "tally":
        print("Player score: ", user_wins)
        print("Computer score: ", computer_wins)

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Tie!")

    else:
        print("You lose!")
        computer_wins += 1

print("Until next time!")