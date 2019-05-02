
import xlsxwriter

# create an object of workbook
workbook = xlsxwriter.Workbook("sample.xlsx")

# create a sheet
sheet = workbook.add_worksheet('First Sheet')


# add a format for clearer text
sheet.set_column('A:D', 20)


# bold text
bold = workbook.add_format({'bold': True})


# data
data = [
    ("Name", "Id", "Phone"),
    ("AAA", 1, 123),
    ("BBB", 2, 456),
    ("CCC", 3, 789)
]


# write the data into sheet
sheet.write('A1', data[0][0], bold)
sheet.write('B1', data[0][1], bold)
sheet.write('C1', data[0][2], bold)


sheet.write('A2', data[1][0])
sheet.write('B2', data[1][1])
sheet.write('C2', data[1][2])


sheet.write('A3', data[2][0])
sheet.write('B3', data[2][1])
sheet.write('C3', data[2][2])


sheet.write('A4', data[3][0])
sheet.write('B4', data[3][1])
sheet.write('C4', data[3][2])


workbook.close()