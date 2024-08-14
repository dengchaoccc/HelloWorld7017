import datetime
import os
import string
import pandas as pd

'''
获取当前目录下所有的文件
'''
def get_all_file(dir, key_name)->list[string]:
    result_list = []
    for file_name in os.listdir(dir):
        if key_name in file_name:
            result_list.append(file_name)
    return result_list

def merge_excel(dir, key_name):
    file_list = get_all_file(dir, key_name)

    result_file_name = "wechatBank"+str(datetime.datetime.now().strftime("%Y-%m-%d %H %M"))+".xlsx"
    result_file_name = os.path.join(dir, result_file_name)

    file_handle_list  = []

    for file_name in file_list:
        file_path = os.path.join(dir, file_name)
        if "cvs" in file_path:
            file_handle_list.append(pd.read_csv(file_path, encoding = "gb2312", header = None))
        elif "xlsx" in file_name or "xls" in file_name:
            file_handle_list.append(pd.read_excel(file_path, encoding="gb2312")