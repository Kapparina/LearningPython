import random
import pandas as pd

# The below generates a random sample of unique values in (start, stop), number-of-values) format:
number_range = random.sample(range(100000, 500000), 200)
fund_names = {"HOST", "HESTA", "AS", "CBUS"}
fund_range = random.choices(sorted(fund_names), k=200)
number_column = pd.Series(number_range)
fund_column = pd.Series(fund_range)
my_spreadsheet = pd.read_excel("../MiscFiles/random_data.xlsx")
my_spreadsheet.insert(loc=0, column="ReferenceNumbers", value=number_column)
my_spreadsheet.insert(loc=1, column="FundNames", value=fund_column)
my_spreadsheet.to_excel("../MiscFiles/MockOutput.xlsx", index=False)
print(pd.read_excel("../MiscFiles/MockOutput.xlsx"))
