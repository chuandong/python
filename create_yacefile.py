import random
import os
import re
import string
import shutil
import sys
import importlib


importlib.reload(sys)

length = 20
time_len = 12
num_len = 10
file_path = 'F:\qrfile'
new_file_path = 'F:\qrfile\yace'
if not os.path.isdir(new_file_path):
    os.makedirs(new_file_path)

file_name = os.listdir(file_path)


def create_yace_file(file_nums):
    file_type = "BCPD"
    inst_no = "14498280"
    end_type = "A"
    for files in file_name:
        if files[:4] == "BCPD":
            print(files)

            for m in range(file_nums):
                timeNum = [random.choice(string.digits) for i in range(time_len)]
                time_random = ''.join(i for i in timeNum)
                numNum = [random.choice(string.digits) for i in range(num_len)]
                num_random = ''.join(i for i in numNum)

                new_files = file_type + time_random + inst_no + num_random + end_type

                srcFile = os.path.join(file_path, files)
                targetFile = os.path.join(new_file_path, new_files)
                print(targetFile)
                if targetFile not in new_file_path:
                    shutil.copyfile(srcFile, targetFile)
                slcNum = [random.choice(string.digits) for i in range(length)]
                card_no = ''.join(i for i in slcNum)
                write_info = ""
                with open(file_path + '\\'+ files, "r") as fr:

                    for info_data in fr:
                        if re.search('CARD_NO', info_data):
                            info_data  = re.sub('CARD_NO', card_no, info_data)
                            write_info += info_data
                with open(new_file_path + '\\'+ new_files, "w") as fw:
                    fw.write(write_info)


if __name__ == "__main__":
    file_nums = int(input("Please input you want create file numbers:"))
    create_yace_file(file_nums)
