player_name = input("Please tell me your name...\n")
print(f"Welcome {player_name}, to this adventure!")

answer = input("You find yourself at the end of a long dirt road - do you head left or right?\n").lower()

if answer == "left":
    answer = input("You arrive at a river; do you attempt to 'walk around' it, or to 'cross'?\n").lower()

    if answer == "cross":
        print("You attempted to cross... unsuccessfully; piranhas feast on your corpse...")

    elif answer == "walk" or answer == "walk around":
        print("You walk for what feels like hours before finally finding a means to cross the river safely.")

    else:
        print("Your decision has roused a nearby pack of snakes! They devour you, and you die!")

elif answer == "right":
    # noinspection PyStatementEffect
    answer == input("You head right, eventually coming to a fragile-looking bridge.")

else:
    print("Your decision-making skills were your downfall; snakes devour you!")
    