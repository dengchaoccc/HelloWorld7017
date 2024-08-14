
import xlrd
import xlwt
import  datetime
import  os
import csv

def get_all_file(dir, key_name):
    result_file_list = []
    os.chdir(dir)
    for file_name in os.listdir("."):
        if ("csv" not in file_name) and ("xls" not in file_name):
            continue
        if key_name in file_name:
            result_file_list.append(file_name)

    return result_file_list


def read_csv_file(src_file, target_sheet, start_line):
    read_line_count = 0
    target_line = start_line
    file_handle = open(src_file, "r", encoding="utf-8")
    reader = csv.reader(file_handle)

    for single_row  in reader:
        for j in range(0, len(single_row)):
            target_sheet.write(target_line, j , single_row[j])
        target_line = target_line + 1
        read_line_count = read_line_count +1

    return read_line_count


def read_xls_file(src_file, target_sheet, start_line):
    read_line_count = 0
    target_line = start_line
    file_handle = xlrd.open_workbook(src_file, "r", encoding="utf-8")
    my_sheets = file_handle.sheets()
    table = my_sheets[0]

    nRows = table.nrows
    nCols = table.ncols


    for i in range(0,nRows):
        for j in range(0, nCols):
            temp_string = table.cell(i,j).values
            target_sheet.write(target_line,j, temp_string)

        target_line = target_line + 1
        read_line_count = read_line_count + 1

    return read_line_count


def merge_all_excel_file(dir, key_name_list):
    os.chdir(dir)
    result_file_name = "wechtBank"+datetime.datetime.now().strftime("%Y-%m-%d %H %M %S")+"xls"
    start_line = 0
    write_line_count = 0

    file_list = get_all_file(".", key_name_list)
    my_excel = xlwt.Workbook(encoding="utf-8")
    my_sheet = my_excel.add_sheet("weChat")

    for file_name in file_list:
        if "csv" in file_name:
            write_line_count = read_csv_file(file_name, my_sheet, start_line)
            start_line += write_line_count
        elif "xls" in file_name:
            write_line_count = read_xls_file(file_name, my_sheet, start_line)
            start_line += write_line_count
        else:
            print("file type error")
    my_excel.save(result_file_name)