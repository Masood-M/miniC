#! /usr/bin/env python

import config
import re
import os, errno, logging
import threading
import urlparse, urllib, urllib2
import mimetypes
import httplib, datetime, time
from datetime import datetime
from time import gmtime, strftime

try:
    import signal
    from signal import SIGPIPE, SIG_IGN
    signal.signal(signal.SIGPIPE, signal.SIG_IGN)
except ImportError:
    pass



def create_directory(directory_name):
 	try:
		os.makedirs(directory_name)
	except OSError as exc:
		if exc.errno == errno.EEXIST:
			pass
		else:	
			raise



def wget(urldict):
	useragent=config.useragent.replace("(","")
	useragent=useragent.replace(")","")	
	url = urldict["url"]
	url_no = urldict["counter"]
	script_path = os.path.dirname(os.path.abspath( __file__ ))	
	debugfile=str(script_path+"/debug/debug.log")
	try:
		# Convert url into valid file name
		fdirname = urllib.quote_plus(url)
		if (len(fdirname) > 250):
			fdirname = fdirname[:247]
# Folder Generation

		# Gets first character of website to store alphabetically
		first_char = re.sub(r"(http://|https://)?(www.)?", "", url)[:1]
		second_char = re.sub(r"(http://|https://)?(www.)?", "", url)[1:3]
		script_path=script_path+'/'
		tmp_path=script_path+'/tmp'
		directory_name = os.path.join(script_path, tmp_path, first_char,  second_char, fdirname)
 		create_directory(directory_name)
		command = 'echo "\n******Visiting Website "'+str(url_no)+' "on the List: '+'"'+url+'"'+'\n"'
		os.system(command)

		if not config.filetypes.strip():
			command1='cd '+directory_name+" && "+'wget -o /dev/stdout -t 2 --waitretry=1 --referer='+'"'+config.referrer+'"'+" "+'--user-agent='+'"'+useragent+'"'+'--header='+'"'+"Accept-Encoding: gzip"+'" '+url+ ' | tee -a '+debugfile
		else:
			command1='cd '+directory_name+" && "+'wget -o /dev/stdout -A '+'"'+config.filetypes+'" '+'-t 2 --waitretry=1 --referer='+'"'+config.referrer+'"'+" "+'--user-agent='+'"'+useragent+'"'+'--header='+'"'+"Accept-Encoding: gzip"+'" '+url+ ' | tee -a '+debugfile
		print command1		
		os.system(command1.strip())


	except Exception, e:   #this is for normal errors (No .js)
		print "error"	
