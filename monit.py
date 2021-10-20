import subprocess, re, sys, os
import psutil
import time
import locale
import os
import ctypes
import threading
from subprocess import Popen, PIPE, STDOUT
import win32api
import win32con
import win32evtlog
import win32security
import win32evtlogutil

enforced = 0
try :
	if sys.argv[2] == "enforced":
	
		enforced = 1
		
except:
	pass

def ownhandle() :
	
	cmd = "handle.exe"+" "+ "-accepteula"+" "+ sys.argv[1]

	p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	output = p.stdout.read()
	#print output

	for line in output.split(b'\n'): 
		
		searchObj = re.search( r'(.*) pid: (.*?) .*', line.decode("utf-8"), re.M|re.I)
	
		if searchObj:
		#print(searchObj.group(2))
	
			if  searchObj.group(2) not in safepids :
		
				return(searchObj.group(2))

#borrowed from  https://rosettacode.org/wiki/Write_to_Windows_event_log#Python	
def ToEvent(progname):
 
	ph = win32api.GetCurrentProcess()
	th = win32security.OpenProcessToken(ph, win32con.TOKEN_READ)
	my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
 
	applicationName = "AntiRansom V5"
	eventID = 1
	category = 5
	myType = win32evtlog.EVENTLOG_WARNING_TYPE
	descr = ["Ransomware detected", "Program:", f"{progname}"]
	data =b""
 
	win32evtlogutil.ReportEvent(applicationName, eventID, eventCategory=category, eventType=myType, strings=descr, data=data, sid=my_sid)
	
	
def ScanRansom():
	
	global safepids
	global safeprog
	
	while True: 
			
		offpid = ownhandle()
			
		if offpid :
			
			p = psutil.Process(int(offpid))
			exefile = p.exe()
		
		
			if exefile in safeprog :
			
				continue 
			
			else :
				
				issigned = 0
				
				print (exefile)
				
				powercommand = f"(Get-AuthenticodeSignature \"{exefile}\").Status -eq 'Valid'"
				powerout = subprocess.run(["powershell", "-Command", powercommand], capture_output=True)
				
				if powerout.stdout.decode("utf-8").strip() == "True":
					issigned = 1
					
				
				if issigned == 0:
					
					p.suspend()
				
				safepids.append(offpid)
				
				if enforced == 1 and issigned == 0 :
					
					ToEvent(exefile)
					
					randdump = str(time.time()) + str(offpid) + ".dmp" ;
				
					dumpcmd = os.path.dirname(sys.executable) + "\\" + 'procdump.exe -ma ' + "\"" + str(offpid) + "\"" + ' -accepteula ' + randdump
				
					cmdblock =subprocess.Popen(dumpcmd, stdout=subprocess.PIPE)
					cmdblock.wait()
				
					p.kill()
					
					continue
				
				
				notetextES = ""
				notetextEN = ""
				
				if issigned == 1:
					
					notetextES = "Nota: El fichero detectado está correctamente firmado y parece legítimo\n\n"
					
					notetextEN = "Note: the executable detected has a valid Authenticode signature and seems legit\n\n" 
			
				if langlocal[0] == "es_ES" :
				
					splashtext = os.path.dirname(sys.executable) + "\\" + 'splash.exe ' + '\"Anti Ransom ha detectado acceso a la carpeta trampa por parte del programa\n\n' + exefile + '\n\n' + notetextES + 'Desea detener dicho proceso?\"'
			
				else :
				
					splashtext = os.path.dirname(sys.executable) + "\\" + 'splash.exe ' +  '\"Anti Ransom has detected access to the Honey Folder by process\n\n' + exefile + '\n\n' + notetextEN + 'Do you want to Stop it?\"'
				
				
				print (splashtext)
				splash = subprocess.Popen(splashtext, stdout=subprocess.PIPE)
				streamdata = splash.communicate()[0]
				rc = splash.returncode
			
				if rc == 10:
					
					ToEvent(exefile)
					
					randdump = str(time.time()) + str(offpid) + ".dmp" ;
				
					dumpcmd = os.path.dirname(sys.executable) + "\\" + 'procdump.exe -ma ' + "\"" + str(offpid) + "\"" + ' -accepteula ' + randdump
				
					cmdblock =subprocess.Popen(dumpcmd, stdout=subprocess.PIPE)
					cmdblock.wait()
				
					p.kill()
				
				else :
				
					safeprog.append(exefile)
					p.resume()
			
			
				return(0)
			
		time.sleep(1)	
		


whnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.ShowWindow(whnd, 0)

langlocal = locale.getdefaultlocale()

ownp = psutil.Process(os.getpid())
ownp.nice(psutil.HIGH_PRIORITY_CLASS)

os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))

safeprog = []
safepids = []

d = threading.Thread(target=ScanRansom)
d.setDaemon(True)
d.start()

sizepids =len(safepids)
	
while True:
	
	sizeintpids = len(safepids)
	
	if sizeintpids > sizepids:
		
		d = threading.Thread(target=ScanRansom)
		d.setDaemon(True)
		d.start()
		sizepids = sizeintpids
		
	time.sleep(1)

