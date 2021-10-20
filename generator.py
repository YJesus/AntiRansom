from random import randint
import random
import string
import xlsxwriter
from fpdf import FPDF
import os
import urllib.request
import sys
import zipfile
import os.path
import tkinter
from tkinter import messagebox
from shutil import copyfile
import subprocess
import re
import locale
import win32com.client

root = tkinter.Tk()
root.withdraw()

# XLS Files

def randomxls (path) :

	numxls = (randint(2000,5000))

	for i in range(10):
	
		name = path + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))]) + ".xlsx"
	
		workbook = xlsxwriter.Workbook(name)
		worksheet = workbook.add_worksheet()


		numrows = (randint(100,500))

		for i in range(numrows):

			coord = 'A' + str(i)
	
			textinrow = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))])
	
			worksheet.write(coord , textinrow)
	

		workbook.close()
		
		for i in range(numxls):
			
			dupli =  path + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))]) + ".xlsx"
			
			copyfile(name, dupli)
	
	
#PDF Files

def randompdf (path) :

	numpdf = (randint(1500,2000))

	for i in range(10):
	
		name = path + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))]) + ".pdf"
	
		numwords = (randint(200,1000))
	
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=12)
	
		words =[]
	
		for i in range(numwords):
		
			randomword  = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))])
			words.append(randomword)
	
		wordsinstring = ''.join(words)
	
		pdf.cell(200, 10, txt=wordsinstring, align="C")
		
		pdf.output(name)
		
		for i in range(numpdf):
			
			dupli = path + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))]) + ".pdf"
			
			copyfile(name, dupli)

#first sysinternals file

url1 = 'https://download.sysinternals.com/files/Procdump.zip'

file1 = 'Procdump.zip';

try :
	urllib.request.urlretrieve (url1, file1)

except Exception as ex:
	
	print (ex)
	
	if not os.path.isfile(file1):
		messagebox.showerror("Error", "Can't download Sysinternals's Files\nTry manually")
		sys.exit()

zip_ref = zipfile.ZipFile(file1, 'r')
zip_ref.extractall()
zip_ref.close()

## second file

url2 = 'https://download.sysinternals.com/files/Handle.zip'

file2 = 'Handle.zip';

try :
	urllib.request.urlretrieve (url2, file2)

except :
	
	if not os.path.isfile(file1):
		messagebox.showerror("Error", "Can't download Sysinternals's Files\nTry manually")
		sys.exit()


zip_ref = zipfile.ZipFile(file2, 'r')
zip_ref.extractall()
zip_ref.close()

langlocal = locale.getdefaultlocale()

if langlocal[0] == "es_ES" :
				
	messagebox.showinfo("AntiRansom V5", "La instalacion puede durar hasta 5 minutos\nPor favor, sea paciente")			

else :
	
	messagebox.showinfo("AntiRansom V5", "Installation could take up to 5 minutes\nPlease be patient")		


finalpathsys = os.environ['USERPROFILE'] + "\\" + str((randint(1,100))) + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))]) + "\\"

os.mkdir (finalpathsys)

randomxls(finalpathsys)
randompdf(finalpathsys)

finalpathexes = os.environ['USERPROFILE'] + "\\" + ''.join([random.choice(string.ascii_letters) for n in range(randint(5,15))]) + "\\"

os.mkdir (finalpathexes)

procdumpfinal = finalpathexes + 'procdump.exe'

copyfile("procdump.exe", procdumpfinal)

handlefinal = finalpathexes + 'handle.exe'

copyfile("handle.exe", handlefinal)


monitexe = str((randint(1,9))) +  ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))]) + ".exe"

namemonit = finalpathexes + monitexe
namesplash = finalpathexes+ 'splash.exe'

copyfile("monit.exe", namemonit)
copyfile("splash.exe", namesplash)

taskrandom = str((randint(1,100))) +  ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randint(5,15))])

#taskpath = re.sub(r"\\", r"\\\\", finalpathsys) 

# Task Stuff borrowed from https://dzone.com/articles/create-and-run-scheduled-task
action_id = taskrandom 
action_path = namemonit 
action_arguments =  finalpathsys[:-1]
action_workdir = finalpathexes 
task_id = taskrandom
task_hidden = False 
run_flags = "TASK_RUN_NO_FLAGS" 
TASK_TRIGGER_DAILY = 2
TASK_CREATE = 2
TASK_CREATE_OR_UPDATE = 6
TASK_ACTION_EXEC = 0

RUNFLAGSENUM = {
    "TASK_RUN_NO_FLAGS"              : 0,
    "TASK_RUN_AS_SELF"               : 1,
    "TASK_RUN_IGNORE_CONSTRAINTS"    : 2,
    "TASK_RUN_USE_SESSION_ID"        : 4,
    "TASK_RUN_USER_SID"              : 8,
    
}
scheduler = win32com.client.Dispatch("Schedule.Service")
scheduler.Connect()
rootFolder = scheduler.GetFolder("\\")
taskDef = scheduler.NewTask(0)
colTriggers = taskDef.Triggers
trigger = colTriggers.Create(9)
trigger.Enabled = True
colActions = taskDef.Actions
action = colActions.Create(TASK_ACTION_EXEC)
action.ID = action_id
action.Path = action_path
action.WorkingDirectory = action_workdir
action.Arguments = action_arguments
info = taskDef.RegistrationInfo
settings = taskDef.Settings
settings.Enabled = True
settings.Hidden = task_hidden
settings.ExecutionTimeLimit  = "PT0S"
settings.StopIfGoingOnBatteries = False
settings.DisallowStartIfOnBatteries = False
principal = taskDef.Principal
principal.RunLevel = 1
result = rootFolder.RegisterTaskDefinition(task_id, taskDef, TASK_CREATE_OR_UPDATE, "", "", RUNFLAGSENUM[run_flags] )
task = rootFolder.GetTask(task_id)
task.Enabled = True
runningTask = task.Run("")
###
file = open("uninstall.bat", "w")


file.write("taskkill /F /IM " + monitexe + "\n")
file.write("schtasks /delete /TN " + taskrandom + " /f" + "\n")
file.write("rmdir " + finalpathsys  + " /s /q" + "\n")
file.write("rmdir " + finalpathexes  + " /s /q" + "\n")

file.close()

nameunis = finalpathexes + 'uninstall.bat'
copyfile("uninstall.bat", nameunis)

disabindex = 'sc config WSearch start= disabled'
disabperm = 'sc stop WSearch'

os.system(disabindex) 
os.system(disabperm) 

startcommand = "schtasks /Run /TN " + taskrandom
 
subprocess.Popen(startcommand, shell=True)

if langlocal[0] == "es_ES" :
				
	messagebox.showinfo("AntiRansom V5", "Instalacion finalizada !!\nNo borre la carpeta desde la que instalo Anti Ransom")				

else :
	
	messagebox.showinfo("AntiRansom V5", "Installation finished !!\nDo NOT delete this installation folder")	
				


