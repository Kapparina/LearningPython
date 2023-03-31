# Import os library.
import os
from pathlib import Path
import sys
import pandas as pd

# Define and print "workbook.csv".
csvfile = pd.read_csv("workbook.csv")
print(csvfile.head().to_string())
