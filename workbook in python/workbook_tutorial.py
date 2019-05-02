
import xlsxwriter


# create a new excel file and a worksheet
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()


# write the first column to make the text clearer
worksheet.set_column('A:A', 20)


# add a bold format to use the highlight cell
bold = workbook.add_format({'bold': True})


# write some simple text in A1 cell
worksheet.write('A1', 'Hello')


# write some simple text in A2 cell
worksheet.write('A2', 'World', bold)


# write some numbers, with row/column notation
worksheet.write(2, 0, 123)

worksheet.write(2, 1, 456)


# insert an image
worksheet.insert_image('B5', 'logo.png')

workbook.close()
