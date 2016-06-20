import subprocess, re, sys, os
import psutil
import time
import locale
import os
import ctypes
import threading


def ownhandle() :
	my_regex = r".*" + re.escape(sys.argv[1]) + r".*"
	
	regex = re.compile(my_regex, re.IGNORECASE)
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid'])
		except psutil.NoSuchProcess:
			pass
		else:
			#print pinfo['pid']
			try:
				proci = psutil.Process(pinfo['pid'])
				for files in proci.open_files() :
					#print files
					#handles = re.match(my_regex, files, re.IGNORECASE)
					match = regex.search(str(files))
					
					#print match
					
					if match is not None and pinfo['pid'] not in safepids :
						
						return(pinfo['pid'])
			except :
				pass
				
	

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
			
				p.suspend()
				
				safepids.append(offpid)
			
				if langlocal[0] == "es_ES" :
				
					splashtext = os.path.dirname(sys.executable) + "\\" + 'splash.exe ' + '\"Anti Ransom ha detectado acceso a la carpeta trampa por parte del programa\n\n' + exefile + '\n\n' + 'Desea detener dicho proceso?\"'
			
				else :
				
					splashtext = os.path.dirname(sys.executable) + "\\" + 'splash.exe ' +  '\"Anti Ransom has detected access to the Honey Folder by process\n\n' + exefile + '\n\n' + 'Do you want to Stop it?\"'
				print splashtext
				splash = subprocess.Popen(splashtext, stdout=subprocess.PIPE)
				streamdata = splash.communicate()[0]
				rc = splash.returncode
			
				if rc == 10:
				
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

