import random
import pandas as pd
from pandas import DataFrame, Series


def random_data() -> tuple[Series, Series, DataFrame]:
    number_col: Series = pd.Series(random.sample(range(100000, 500000), 200))
    fund_col: Series = pd.Series(random.choices(sorted({"HOST", "HESTA", "AS", "CBUS"}), k=200))
    input_file: DataFrame = pd.read_excel("../../MiscFiles/random_data.xlsx")

    return number_col, fund_col, input_file


number_column, fund_column, my_spreadsheet = random_data()

my_spreadsheet.insert(loc=0, column="ReferenceNumbers", value=number_column.replace(",", ""))  # Inserting column.
my_spreadsheet.insert(loc=1, column="FundNames", value=fund_column)  # Inserting column.

output_path: str = "../../MiscFiles/"
while (my_input := input("What would you like the output to be called? ")) == "":
    print("Please input a value...")

my_spreadsheet.to_excel(output_path + my_input + ".xlsx", index=False)
# my_spreadsheet.to_excel("../MiscFiles/MockOutput.xlsx", index=False)  # Rewriting DataFrame to Excel workbook.

print(pd.read_excel("../../MiscFiles/MockOutput.xlsx"))
