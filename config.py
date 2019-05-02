#!/usr/bin/python2.7
import sys
import os
import string
from os.path import basename



useragent="Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)" 

#Internet explorer identifies itself as Mozilla/4.0 - MSIE 7.0 is Internet Explorer Version and Windows NT 5.1 is Windows XP
	# "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6",
	# "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.6) Gecko/2009011912 Firefox/3.0.6",
	# "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6 (.NET CLR 3.5.30729)",

acceptlang="en-us,en;q=0.5"

# Referrer
referrer="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source="


# Number of Threads
# Worker threads = threadnum - 2
threadnum=5

