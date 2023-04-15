import time
import pandas as pd
import pyexcel as p
import glob

start = time.perf_counter()


def pandas_csv():  # Reading a CSV file with Pandas...
    titanic_df = pd.read_csv("../MiscFiles/titanic.csv")
    print(titanic_df.head(5).dtypes.to_string())
    # titanic_df.to_excel("../xl-temp.xlsx", index=True)
    # titanic_df.tail(5).to_excel("../workbook-temp.xlsx", sheet_name="test-sheet", index=False)
    # xlsx_file = pd.read_excel("../workbook-temp.xlsx")
    # xlsx_file.to_csv("../csv-temp.csv", index=False)
    titanic_df.drop(columns=["PassengerId"], inplace=True)  # One way of removing a column...
    titanic_df = titanic_df.drop(columns=["SibSp"])  # ... and another way of removing a column.
    print(titanic_df.groupby(["Sex", "Pclass"]).mean(numeric_only=True))
    print(titanic_df[titanic_df["Age"] < 18].groupby(["Sex", "Pclass"]).mean(numeric_only=True))


def pyexcel_csv():  # Reading a CSV file with PyExcel...
    sheet = p.get_sheet(file_name="../Automobile.csv")
    sheet.row += ["This", "row", "is", "for", "testing", "purposes"]
    sheet.column += ["Test Col"]
    print(sheet)


pandas_csv()

end = time.perf_counter()
print("Execution time: \n", (end - start), "second(s)")

# print("Execution time: \n", (end - start) * 10 ** 3 / 1000, "s")
