#!/usr/bin/python
# -*- coding: UTF-8 -*-

#send mail package
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#check disk info package
import os
import re
import time
import smtplib
import commands
import subprocess
import sys

#variable define
home='home'
oracle='oracle'

def SendMail(service_name, pass_val):
	sender = '123@.com'
	receivers = ['123@qq.com']  # recv mail
	
	# First parameter:send mail content,Seconds parameter: plain set text format,The third parameter:utf-8 set the encoding format
	message = MIMEText('UAT disk must be clean,dictionary is:[%s],Used disk space is:[%s%%]'%(service_name, pass_val), 'plain', 'utf-8')
	message['From'] = Header("PYTHON", 'utf-8')  # sender
	message['To'] = Header("UAT", 'utf-8')  # receover
	
	subject = 'UAT Disk Space Warning!!!'
	message['Subject'] = Header(subject, 'utf-8')
	
	try:
	    smtpObj = smtplib.SMTP('localhost')
	    smtpObj.sendmail(sender, receivers, message.as_string())
	    print ("mail send success")
	except smtplib.SMTPException:
	    print ("send mail fail")

    
def CheckDisk():
	child = subprocess.Popen('df -h | awk \'NR>1 {print $6}\'', stdout=subprocess.PIPE, shell=True) #NR>1 expression get the value start the second line
	out = child.stdout.readlines()

	for item in out:
		line = item.strip().split('/')[-1]
		print line
		
		if ((home == line) or (oracle == line)):
			capa_val = subprocess.Popen('df -h | grep %s | awk \'{print $5}\''%line, stdout=subprocess.PIPE, shell=True)
			dig_val = capa_val.stdout.readlines()
			for val in dig_val:
				dig = val.strip().split('%')[0]
				print dig
				if (int(dig) > 60):
					SendMail(line, int(dig))
	
		
	
if __name__=='__main__':
	CheckDisk()	    

