from datetime import datetime
import re
import time
import subprocess
import os
import sys

def executeShellCommand(ExecuteShellCommand):
    with subprocess.Popen(ExecuteShellCommand, stdout=subprocess.PIPE) as proc:
        Output = proc.stdout.readlines()
        return Output

def pythonFileCreate():
	return ["python",'ExecutePower.py']

def convertByteTostring(outputList):
	s=" "
	for item in outputList:
		s=s+item.decode()
	return s
"""
def Pattern(drivepath):
	pattern = re.findall(r'[\s][a-zA-z][\:][\\][a-zA-Z]+[\\]+',drivepath)
	return pattern"""

def Intervalexecute():
	intervalIterate = int(input("Now tell me how many times I need to run this, please in digits and limit to 5 not more\n"))
	if intervalIterate==6:
		sys.exit()
	for x in range(0,intervalIterate):
		print("executing for", x)
		CreateFileOutput=executeShellCommand(pythonFileCreate())
		time.sleep(5)
		getDirName=convertByteTostring(CreateFileOutput)
		print(getDirName)

Intervalexecute()





