# This will essentially be used as a custom module, imported within the 'app.py' file.

import random

feet_in_mile = 5280
metres_in_kilometre = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)

