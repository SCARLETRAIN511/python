import xlrd
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

xlrd.Book.encoding = "utf-8"
data = xlrd.open_workbook("1.xlsx")
table = data.sheet_by_index(0)


def calculateXls():
    rows_count = table.nrows
    for i in range(rows_count):
        print(table.row_values(i))# it will give the values in the list and float number
    
    cell_A1 = table.cell(0,0).value# this will give the 0x0 value in the table
    cell_B3 = table.cell(3,1).value
    print("The value in B3 is %d" %cell_B3)
    print("The value in A1 is %d" %cell_A1)

#xlwt cant only manipulate xlsx file 
def CreateXls():
    file_name = xlwt.Workbook()
    sheet2 = file_name.add_sheet('test')
    coneten1 = 'this is the first content'
    for i in range(9):
        for j in range(8):
            sheet2.write(i, j, i*j)
    file_name.save("2.xls")

def editXls():
    rb = open_workbook("2.xls")
    wb = copy(rb)
    s = wb.get_sheet(0)
    s.write(0,1,"new data")
    wb.save("2.xls")

if __name__ == "__main__":
    CreateXls()
    editXls()
    

