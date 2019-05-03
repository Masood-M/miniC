#! /usr/bin/env python

import time
import threading
import os, sys, Queue
from itertools import groupby
from operator import itemgetter
from time import gmtime, strftime
import os.path
import logging
import scan
import unquote
import argparse
import wget, config
import shutil

try:
	import signal
	from signal import SIGPIPE, SIG_IGN
	signal.signal(signal.SIGPIPE, signal.SIG_IGN)
except ImportError:
	pass


queue=Queue.Queue()
logger = logging.getLogger()

def worker():

	urldict = queue.get()	
#this is for the normal visitor output (no error)
	logger.info(str(urldict["counter"]) + ",\t" + urldict["url"]+",\t"+ "Visiting")
	wget.wget(urldict)
	queue.task_done()
	

def threadmaker():
	
	while True:
		
		threadstomake = config.threadnum - threading.active_count()
		
		for i in range(threadstomake):
			thread = threading.Thread(target=worker)
			thread.setDaemon(True)
		 	thread.start()

		time.sleep(5)


def readurl():
	url = sys.argv[2]
	return url


def main():
#Create the threads
	thread = threading.Thread(target=threadmaker)
	thread.setDaemon(True)
	thread.start()
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	parser = argparse.ArgumentParser(description="Examples:\n/miniC.py --file <file path>\n./miniC.py --update\n", formatter_class=argparse.RawTextHelpFormatter)

	parser.add_argument("--file", nargs=1, help="Provide an input file", action="store")
	parser.add_argument("--update", help="Updates the anti-virus signatures", action="store_true")
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)
	args = parser.parse_args()
#	path = config.tmpfolder
	tmp_path=script_path+'/tmp'

#create the tmp folder

	if os.path.isdir(tmp_path):
		shutil.rmtree(tmp_path)
		os.makedirs(tmp_path)     
	else:
		pass
#File

	if args.file:
		if os.path.exists(script_path+"/debug/debug.log"):
			os.remove(script_path+"/debug/debug.log")
		else:
			pass
		mylist = list()
		mylist2 = list()
		counter =0
		fopen3 = open(sys.argv[2],"r")	
		for line in fopen3:
			dict={}
			line = line.strip()
			counter += 1
			if not (line.startswith("http://")) and not (line.startswith("https://")):
				line = "http://"+line
			dict["url"] = line
			dict["counter"] = counter
			queue.put(dict)
		queue.join()
		fopen3.close()
		scan.scanning(script_path)
		unquote.unquoteDirectory(script_path)

#Update antivirus signatures
	if args.update:
		updatecommand=('sudo freshclam')

if __name__ == "__main__":
	main()
