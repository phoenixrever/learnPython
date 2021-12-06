# coding: utf-8
import xlwt

file = xlwt.Workbook()
sheet = file.add_sheet("sheet1")
sheet.write(0, 0, 'hello')  # 行 列 内容
file.save("test.xls")
