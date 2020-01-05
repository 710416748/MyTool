# -*- coding: utf-8 -*-
# @Time        : 2020 01 05
# @Author      : YeChen.Xu
# @Email       : 710416748@qq.com
# @File        : rename_file.py
# @Description :

import os
import sys

default_path = "/home/ubuntu/test"
default_old_str = ".bp"
default_new_str = ".bp1"
file_pickup = []


def deal_dir(path, str_value):
    if os.path.isdir(path):
        pickup_file(path, str_value)
    else:
        # print(path + " is no dir")
        pass


def filter_file(file, str_value):
    # print("get file " + file)
    if file.endswith(str_value):
        file_pickup.append(file)


def pickup_file(path, str_value):
    file_root = os.listdir(path)

    if file_root is None:
        print("ERROR cannot find the file")

    file_list_copy = file_root

    for file in file_list_copy:
        # print(os.path.join(path, file))
        whole_path = os.path.join(path, file)
        if os.path.isfile(whole_path):

            filter_file(whole_path, str_value)
            file_root.remove(file)

    for dir_name in file_root:
        deal_dir(os.path.join(path, dir_name), str_value)

    return file_pickup


def rename_file(path, old_str, new_str):

    if not os.path.exists(path):
        print("please check file path")
        return

    pickup_file(path, old_str)

    if file_pickup is None:
        print("cannot find file contains " + old_str)
        return

    for file in file_pickup:
        print("pick up " + file)

    confirm = input("enter n to exit and enter other to rename: ")
    if confirm in ['n', 'N']:
        print("catch " + confirm + " and exit")
        return

    for file in file_pickup:
        os.rename(file, os.path.join(os.path.dirname(file), os.path.basename(file).replace(old_str, new_str)))

    print("rename done")


if __name__ == '__main__':

    if len(sys.argv) == 4:
        print("path = " + sys.argv[1] + " old_str = " + sys.argv[2] + " new_str = " + sys.argv[3])
        rename_file(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) > 1:
        print("please enter path  old string  new_string")
    else:
        print("use default parameters")
        rename_file(default_path, default_old_str, default_new_str)
