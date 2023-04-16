from itertools import count

import pandas as pd

from pandas import DataFrame

# df = pd.read_excel("../MiscFiles/MockOutput.xlsx")
# with pd.ExcelWriter("../MiscFiles/random_data.xlsx", mode="a") as writer:
#     df.to_excel(writer, sheet_name="NewSheet", index=False)


# x = ".test"
# print(f"value"+x)

a: list[int | str] = [5, "apple"]
b: dict[int | str, int | str] = {key: i for i, key in enumerate(a)}
print([key for key in b.keys()])

df: dict[str | int, DataFrame] = pd.read_excel("../../MiscFiles/random_data.xlsx", sheet_name=None)
print("Workbook 'random_data.xlsx' consist of the following sheets: ", list(df.keys()))
while (sheet_name := input("Please select a sheet to view: ")) != "q":
    try:
        print(df[sheet_name: DataFrame])
    except KeyError:
        print("Remember sheet names are case sensitive; 'sheet one' and 'Sheet One' are unique names...")
