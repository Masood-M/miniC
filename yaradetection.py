#! /usr/bin/env python


import subprocess
import sys
import os, datetime, time
import string
import config 

#compile the rules



def listandscan():

	start_timeYara = time.time()
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	log_path = script_path+"/scanlogs/Yreport.log"
	with open(log_path, "w") as f:
		print "\n===================================== Yara =====================================" 
		f.write("======================================Yara======================================\n\n")
		f.write(datetime.datetime.now().strftime("%A, %d %B %Y %I:%M:%S%p") + "\n")
		f.write("Command: yara -r "+ script_path+"/yrules/rules.yara " + script_path+"/tmp/" + "\n\n")
		f.write("--------------------------------------------------------------------------------\n\n")
#		os.system("find . -type f -size 0k -exec rm {} \; | awk '{ print $8 }'")

		process = subprocess.Popen("yara -r "+ script_path+"/yrules/rules.yara " + script_path+"/tmp/", shell=True, stdout=subprocess.PIPE)
		for line in iter(process.stdout.readline, ''):
			sys.stdout.write(line)
			f.write(line)

		finish_time = time.time() - start_timeYara, "seconds"
		print "================================================================================\n"
		f.write("\n================================================================================\n\n")
		f.write("Scanning time with Yara engine was: " + str(finish_time) + "\n")
	f.close()

'''
def yaradetect(inputfile):
	ruleinput='Value'
	fin = open(honeypotconfig.wdir+"yrules/rules.yara", 'r')
	if fin:
		ruleinput = fin.read()
		fin.close()
	rules = yara.compile(source=ruleinput)
	f = open(inputfile, 'r')
	matches = rules.match(data=f.read())
	for m in matches:
		print "%s" % m+ " found in file: " +inputfile
		yarareport=reportfile.write(inputfile+"\t\t"+"%s" % m+"\n")

'''
