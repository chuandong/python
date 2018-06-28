#!/usr/bin/python
#coding:utf-8

import random
import os
import re
import string
import shutil
import sys

length = 12
time_len = 12
num_len = 10
file_path = '/home/jkcore/core/data/qrfile'
new_file_path = '/home/jkcore/core/data/yace_file'
if not os.path.isdir(new_file_path):
    os.makedirs(new_file_path)

file_name = os.listdir(file_path)

file_head="000800014498280   2018061500000000PROD00000001"
file_body="386800000011000012088222459778451    9001208822245977845114498280   04498280   50023301   41310314498280                                               000000000000000000000000000000000000000000001000000000371580000000371582018061515600000000006400FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFTERMID   30800   公交：0011路 车号：038807 乘车时间：2018-06-15-08:48:11                                                                         20180615084811FFFFFFFFFFFFFFF0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF100011732001020F00000001000001014C81014924010100000612044982800918900021040400210398170881A55BDC3F4E6DDF1E5B847AFEA60BB2243733809DAC92C0E3B47B73092EB38A312A6CAEA1A3896319794D2824AC9908918AECF8D4EEA47FD3D17CD7D5BF37C45A843667F91C9FE1916989A799CA96F9550414F617DB0CEFBD783CF5B532303838323232343539373738343531900120882224597784510449828050023301000007D0032B6BA9E4E08CD9C649A66EB6D38D9FFEDE564A622311C3805BB3DB921B38784A5B2C470B025800153D97CE85E9B1C6735A84F9D73384B509294BA409A09E13D0CBE053C601CDF59C6EF4024DF515B4D732484D2301AA9614D76AE2B8BE84BEB98E10579B4D01A4805B230C9315D3895BDE150C02D3F484C9F2E759246ED6DF04F27F292E89441BCA1C67CAE6619E6D3DF3030E49077FE3D6F0DA4D3E730F0C2EEF0CB44E3D0CB953E83A34E8D40002000838323830313030310003000830363037303830390004000A322E315F3137303932330005002B3034343938323830303030313431333130313037333339353230313830363135303834383131333038303000060004343133310007000100000800033135360009000400000100000A0006303338383037000C00054646464646000D0006303030303131001000045B230CCB00110020B96AD89FDF3DC1C5952F1279E396CE12FB41EAEA6E2D2D6089530645B2D54EA420020000200300142018061508481120050004001120070001020090012413101073395201100048280203700060011路20380006武威市"
file_end="0018000000000000RECORD00000000000000000000000000000000"

def create_yace_file(file_nums, contentNums):
	
    file_type = "BCPD"
    inst_no = "14498280"
    end_type = "A"
    info_body=""
    change_body=""
    change_end=""
    record_nums = contentNums+2
    print('record_nums:%d'%record_nums)
    
    for m in range(file_nums):
        timeNum = [random.choice(string.digits) for i in range(time_len)]
        time_random = ''.join(i for i in timeNum)
        numNum = [random.choice(string.digits) for i in range(num_len)]
        num_random = ''.join(i for i in numNum)
        new_files = file_type + time_random + inst_no + num_random + end_type
    	print('new_files:%s'%new_files)
        """
        srcFile = os.path.join(file_path, files)
        targetFile = os.path.join(new_file_path, new_files)
        print(targetFile)
        if targetFile not in new_file_path:
            shutil.copyfile(srcFile, targetFile)
        with open(file_path + '//'+ files, "r") as fr:
		
            for info_data in fr:
                if re.search('TERMID', info_data):
                    info_data  = re.sub('TERMID', value, info_data)
                    write_info += info_data
        """
        if new_files not in new_file_path:
        	info_body=""
    		change_body=""
    		change_end=""
    		write_info = ""	
        	for j in range(contentNums):
        		
        		slcNum = [random.choice(string.digits) for i in range(length)]
        		value = ''.join(i for i in slcNum)
        		change_body=file_body
        		#print("change_body", change_body)
        		if re.search('TERMID', change_body):
        			change_body=re.sub('TERMID', value, change_body)
        		info_body=info_body + change_body
        	
        	change_end=file_end
        	if re.search('RECORD', change_end):
        		change_end=re.sub('RECORD',str(record_nums), change_end)
        	
        	write_info = file_head+info_body+change_end
        	with open(new_file_path + '//'+ new_files, "w") as fw:
        	    fw.write(write_info)

if __name__ == "__main__":
    file_nums = int(input("Please input you want create file numbers:"))
    contentNums = int(input("Please input you want file content numbers:"))
    create_yace_file(file_nums, contentNums)
