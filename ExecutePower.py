from datetime import datetime
import re
import time
import subprocess

def executeShellCommand(ExecuteShellCommand):
    with subprocess.Popen(ExecuteShellCommand, stdout=subprocess.PIPE) as proc:
        Output = proc.stdout.readlines()
        return Output

def Powereshell():
	command=["powershell","-command"]
	return command

#==============================================================================================================
# Code:1 Code between these lines will get the drive letter
def ListNFSMounts():
	#getOutput
	nfsMount = ["powershell","-command","Get-PSDrive", """| ?{[char[]]"CELSTW" -notcontains $_.name} | ?{$_.Provider.name -eq "FileSystem"}"""]
	return nfsMount

def convertByteTostring(outputList):
	s=" "
	for item in outputList:
		s=s+item.decode()
	return s

def Pattern(getDriveLetter):
	pattern = re.findall(r'[\n][a-zA-Z][\s]+',getDriveLetter)
	return pattern

#==============================================================================================================
#Functions below to create directory file and write data to nfs
def FormPathNFS(DriveLetter):
	driveLetter = DriveLetter +":\\"
	return driveLetter

def dirNameAdd():
	pathname=FormPathNFS(DriveLetter)
	command=pathname+"NewDirectory"
	return command


def Makdirpath():
	command="mkdir " + dirNameAdd() 
	return str(command)

def createDircommand(DirectoryPath):
	command=["powershell","-command"]
	command.append(DirectoryPath)
	return command

def CreatePathtocreatebinfile():
	filepath = dirNameAdd() + "\\testFile.bin"
	return filepath

#=======================Below uses fsutil command to create test file=================
def creatFsutil():
	size = " 600000000" 
	fsutilcmd =  "fsutil " + "file " + "createNew " + CreatePathtocreatebinfile()+size
	command = Powereshell()
	command = command+fsutilcmd.split()
	#print(command)
	return command
#=====================Delete dir and file===================================
def removefilepath():
	base=["powershell","-command"]
	Deletedir="Remove-Item {} -Recurse".format(dirNameAdd())
	#print("check type",type(Deletedir))
	base.append(Deletedir)
	return base

#==============================================================================================================
#Code between these lines will get the drive letter funtions associated to function number :1
result = executeShellCommand(ListNFSMounts()) 
OutputOfnfsmount=convertByteTostring(result)
#print(OutputOfnfsmount)
FindDriveLetter=Pattern(OutputOfnfsmount)
DriveLetter=re.sub(r"[\n\s]*", "", FindDriveLetter[0])
#print(DriveLetter)
#==============================================================================================================

#NsfPathtoCreatedir = FormPathNFS(DriveLetter)
DirectoryPath=Makdirpath()
#print(DirectoryPath)
Readytomakedir = createDircommand(DirectoryPath)
#print(Readytomakedir)
result2 = executeShellCommand(createDircommand(DirectoryPath)) 
print("==================================================")
print("Please wait creating directory...\n")
#print(convertByteTostring(result2))
print("Directory Created...\n")
print("==================================================")
#===========================Create file==================================================
createfile = executeShellCommand(creatFsutil())
#print(createfile)
output=convertByteTostring(createfile)
print("==================================================")
print("Please wait creating file.....\n")
print("\n",output)
#print(".bin file created .\n")
print("==================================================")
#print(createfile)
#===========================hold delete==================================================
print("==================Sleeping now....==========================")
time.sleep(5)
#===========================Delete File==================================================
print("==================================================")
print("Going to delete file now...\n")
deletePath=removefilepath()
output1=executeShellCommand(deletePath)
print("File Deleted now...\n")
print("==================================================")







