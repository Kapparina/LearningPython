# Import os library.
import os
from pathlib import Path
import sys
import pandas as pd


# Function to print and amend working directory.
relpath = Path(__file__).parent / "Modules"

# Define and print "workbook.csv".
csvfile = pd.read_csv(relpath & "/workbook.csv")
print(csvfile.head().to_string())
