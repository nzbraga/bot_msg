from openpyxl import load_workbook

def sheet_info(page):
    workbook = load_workbook('list_name.xlsx')
    sheet_name = workbook.sheetnames[page]
    sheet = workbook[sheet_name]

    return sheet