# Import os library.
import os
from pathlib import Path
import sys
import pandas as pd
import cProfile
import pytest
import time

start = time.time()


# Define and print "workbook.csv".
csvfile = pd.read_csv("workbook.csv")
print(csvfile.head(5).to_string())

end = time.time()

print("Execution time: \n", (end-start) * 10**3 / 1000, "s")