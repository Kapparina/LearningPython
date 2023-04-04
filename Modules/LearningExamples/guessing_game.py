secret_word = "giraffe"
guess = str(None)  # Setting this to a string to avoid confusion should the user guess an integer or float.
guess_count = 0
guess_limit = 3
out_of_guesses = False

def guessing_game():
    global guess, guess_count, guess_limit, out_of_guesses  # Declaring global variables to allow out-of-scope referral.

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Please enter your best guess: \n")
            guess_count += 1
        else:
            out_of_guesses = True

guessing_game()  # Calling this will begin the game again.

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN!")


retry = input("Play again? \n")

if retry == ["Y", "yes"]:
    print("Let's go again!")
    guessing_game()
elif retry == ["N", "*"]:
    print("Until next time!")