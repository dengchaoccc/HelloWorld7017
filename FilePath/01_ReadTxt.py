#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/19 15:14
# @Author  : mac
# @File    : 01_ReadTxt.py
# @Software: PyCharm

def read_txt_file():
    with open("oscommand.txt","r") as file_obj:
        #也可以用readlines一次性全部读取出来
        for aline in file_obj:
            if aline != "":
                #rstrip是删除txt里面每行的换行符，print函数本身已经换行了
                print(aline.rstrip())

def def_write_txt_to_file():
    with open("oscommand_copy.txt","w") as dest_file_obj:
        with open("oscommand.txt", "r") as read_file_obj:
            for aline in read_file_obj:
                if aline:
                    dest_file_obj.write(aline)
    return



if __name__ == "__main__":
    read_txt_file()
    def_write_txt_to_file()
