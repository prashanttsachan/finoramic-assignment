import re
import subprocess
import sys

file = open('hello.txt', 'r')
filedata = file.read()
filedata = filedata.replace("\t", "")
filedata = filedata.replace("{", "")
filedata = filedata.replace("}", "")
filedata = filedata.replace(" ", "")
filedata = filedata.replace("Dependencies=", "")
filedata = filedata.replace(",", "")
filedata = filedata.strip(",")
filedata = filedata.strip("\n")
file = open('requirements.txt','w')
file.write(filedata)
file.close() 

filedata = filedata.split("\n")
error = []
for rows in filedata:
	line = rows.split("==")
	try:
		subprocess.check_call([sys.executable, "-m", "pip", "install", line[0]])
	except subprocess.CalledProcesError as cd:
		error.append(line[0])
		print ("error code", cd.returncode)

if len(error) == 0:
	println ("success")
else:
	for err in error:
		println (err)
