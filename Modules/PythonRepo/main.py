import time
import pandas as pd
import pyexcel as p

start = time.time()


def pandas_csv():  # Reading a CSV file with Pandas...
    csvfile = pd.read_csv("workbook.csv")
    print(csvfile.head(5).dtypes.to_string())
    csvfile.to_excel("../workbook-temp.xlsx", sheet_name="test", index=False)


def pyexcel_csv():  # Reading a CSV file with PyExcel...
    sheet = p.get_sheet(file_name="../Automobile.csv")
    sheet.row += ["This", "row", "is", "for", "testing", "purposes"]
    sheet.column += ["Test Col"]
    print(sheet)


pandas_csv()

end = time.time()

print("Execution time: \n", (end - start) * 10 ** 3 / 1000, "s")
