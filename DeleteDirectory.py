from datetime import datetime
import re
import time
import subprocess
import sys

def executeShellCommand(ExecuteShellCommand):
    with subprocess.Popen(ExecuteShellCommand, stdout=subprocess.PIPE) as proc:
        Output = proc.stdout.readlines()
        return Output

#Get-ChildItem C:\myfolder -Include *.* -Recurse | ForEach  { $_.Delete()}
def removefilepath():
	base=["powershell","-command"]
	Deletedir="Remove-Item {} -Recurse".format(sys.argv[0].replace(" ",""))
	print("check type",type(Deletedir))
	base.append(Deletedir)
	#return base

deletePath=removefilepath()
print("check type",type(deletePath))
output1=executeShellCommand(deletePath)
print(output1)
#output2=executeShellCommand(removeDir())
