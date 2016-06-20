from random import randint
import random
import string
import xlsxwriter
from fpdf import FPDF
import os
import urllib
import sys
import zipfile
import os.path
import win32ui
from shutil import copyfile
import subprocess
import re
import locale

# XLS Files

def randomxls (path) :

	numxls = (randint(2000,5000))

	for i in range(10):
	
		name = path + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))]) + ".xlsx"
	
		workbook = xlsxwriter.Workbook(name)
		worksheet = workbook.add_worksheet()


		numrows = (randint(100,500))

		for i in range(numrows):

			coord = 'A' + str(i)
	
			textinrow = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))])
	
			worksheet.write(coord , textinrow)
	

		workbook.close()
		
		for i in range(numxls):
			
			dupli =  path + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))]) + ".xlsx"
			
			copyfile(name, dupli)
	
	
#PDF Files

def randompdf (path) :

	numpdf = (randint(1500,2000))

	for i in range(10):
	
		name = path + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))]) + ".pdf"
	
		numwords = (randint(200,1000))
	
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=12)
	
		words =[]
	
		for i in range(numwords):
		
			randomword  = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))])
			words.append(randomword)
	
		wordsinstring = ''.join(words)
	
		pdf.cell(200, 10, txt=wordsinstring, align="C")
		
		pdf.output(name)
		
		for i in range(numpdf):
			
			dupli = path + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))]) + ".pdf"
			
			copyfile(name, dupli)

url1 = 'https://download.sysinternals.com/files/Procdump.zip'

file1 = 'Procdump.zip';

try :
	urllib.urlretrieve (url1, file1)

except :
	
	if not os.path.isfile(file1):
		win32ui.MessageBox("Can't download Sysinternals's Files\nTry manually", "Error", 4096)
		sys.exit()


zip_ref = zipfile.ZipFile(file1, 'r')
zip_ref.extractall()
zip_ref.close()

langlocal = locale.getdefaultlocale()

if langlocal[0] == "es_ES" :
				
	win32ui.MessageBox("La instalacion puede durar hasta 5 minutos\nPor favor, sea paciente", "Aviso", 4096)			

else :
	win32ui.MessageBox("Installation could take up to 5 minutes\nPlease be patient", "Warning", 4096)


finalpathsys = os.environ['USERPROFILE'] + "\\" + str((randint(1,100))) + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))]) + "\\"

os.mkdir (finalpathsys)

randomxls(finalpathsys)
randompdf(finalpathsys)

finalpathexes = os.environ['USERPROFILE'] + "\\" + ''.join([random.choice(string.ascii_letters) for n in xrange(randint(5,15))]) + "\\"

os.mkdir (finalpathexes)

procdumpfinal = finalpathexes + 'procdump.exe'

copyfile("procdump.exe", procdumpfinal)


monitexe = str((randint(1,9))) +  ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))]) + ".exe"

namemonit = finalpathexes + monitexe
namesplash = finalpathexes+ 'splash.exe'

copyfile("monit.exe", namemonit)
copyfile("splash.exe", namesplash)

taskrandom = str((randint(1,100))) +  ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(randint(5,15))])

taskpath = re.sub(r"\\", r"\\\\", finalpathsys) 

taskcommand = 'schtasks /create /tn ' + taskrandom + " /tr " + "\"" + namemonit +" " + taskpath[:-2] + "\"" + ' /sc onlogon /RL HIGHEST'

os.system(taskcommand) 

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
				
	win32ui.MessageBox("Instalacion finalizada !!\nNo borreo la carpeta desde la que instalo Anti Ransom", "Done", 4096)			

else :
	win32ui.MessageBox("Installation finished !!\nDo NOT delete this installation folder", "Done", 4096)
				


