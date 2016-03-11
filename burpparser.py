"""
	Burp Suite SiteMap2Backuplist payload generator v2
	(c) Abdulla Ismayilov, 11.03.2016
"""

import sys
import os
from xml.dom import minidom
import time
from urlparse import urlparse


xmlfile = sys.argv[1]

if(not os.path.isfile(xmlfile)):
	sys.exit("[!] Fayl Tapilmadi")
	

siyahi = [".txt",".bak",".backup",".bkp","~","~1",".inc",".src",".java",".cs",".old",".db",".tar",".tar.gz",".zip",".rar",".tmp",".psa",".r19",".datbak0",".ini",".cmp",".pcxm","000",".wspak",".ibz",".sqb",".ckp",".dbk",".ren",".trn",".bkf",".jpa"]

stat = [".js",".css",".jpg",".jpeg",".png",".gif",".ico",".ttf",".txt"]

now = time.time()
suffix = int(now)
name = xmlfile+"_backup_"+str(suffix)+".txt"	
xmldoc = minidom.parse(xmlfile)
itemList = xmldoc.getElementsByTagName("path")
path = []
sec = []
payloads = []

similarFile = []

def addtwo(data):
	filename, file_extension = os.path.splitext(data)
	return filename+"2"+file_extension+"\n"

def hasExtension(data):
	filename, file_extension = os.path.splitext(data)
	if(file_extension==""):
		return False
		
	return True
	
	
def isStatic(data):
	for i in stat:
		if(data.endswith(i)):
			return True
			
	return False
	
	
for i in range(0,len(itemList)):
	if(hasExtension(itemList[i].firstChild.data)):
		if(not isStatic(itemList[i].firstChild.data)):
			if("?" in itemList[i].firstChild.data):
				parsed = urlparse(itemList[i].firstChild.data)
				if(parsed.path not in path):
					path.append(parsed.path)
				if(addtwo(parsed.path) not in sec):
					sec.append(addtwo(parsed.path))
			else:
				if(itemList[i].firstChild.data not in path):
					path.append(itemList[i].firstChild.data)
				
				if(addtwo(itemList[i].firstChild.data) not in sec):
					sec.append(addtwo(itemList[i].firstChild.data))
				
		
for extension in siyahi:
	for uri in path:
		newpath = uri+extension
		payloads.append(newpath+"\n")


payloads.extend(sec)

handle = open(name,"w")
handle.writelines(payloads);
handle.close()
	
kecen_vaxt = time.time() - now
deq = False
if(kecen_vaxt>=60):
	kecen_vaxt = kecen_vaxt/60
	deq = True
	
"""	
for i in payloads:
	print "[+] ",i.strip("\n")	
"""
	
print ""	
print "[*] Muvefeqiyetle backup file list-i hazirlandi."
print "[*] "+name+" adi altinda "+os.getcwd()+"\\"+name+" yadda saxlandi." 
print "[*] Payload-larin sayi: " + str(len(payloads))
if(deq):
	print "[*] Serf olunan zaman:"+ str(kecen_vaxt) +" deqiqe."
else:
	print "[*] Serf olunan zaman:"+ str(kecen_vaxt) +" saniye."