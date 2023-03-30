# Import os library.
import os

import sys
import pandas as pd


# Function to print and amend working directory.
def WorkingDirectory():
    print("Current working directory is:", os.getcwd())
    # os.chdir("./Modules/PythonRepo")
    print("Amended working directory is:", os.getcwd())


# Call WorkingDirectory()
WorkingDirectory()

# Define and print "workbook.csv".
csvfile = pd.read_csv("workbook.csv")
print(csvfile.head().to_string())
