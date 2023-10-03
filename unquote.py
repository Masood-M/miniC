import os

infected_files = dict()


def unquoteDirectory(script_path):
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	#currentdir = os.getcwd()
	# Open the Clam-AV log


#	with open(script_path + "/scanlogs/f-prot.log") as f:
#		start = False
#		for line in f:
#			line = line.split("\t")[1].strip()				
#			infected_files[line] = " F-Prot"


	infected_urls = dict()

	for k, v in infected_files.iteritems():

		# Check if "http" string not in folder name
		# If "http" not in folder name, use parent directory as "website"
		# Else use folder with first occurrence of "http"
		if k.rfind("/") < k.find("http") or k.find("http") == -1:
					website = k[:k.rfind("/")]
		else:
			website = k[k.find("http"):].split("/")[0]

		# Place files(Value) under respective folder(Key)
		# If folder(Key) exist, append
		# Else create
		if website in infected_urls:
			infected_urls[website] = infected_urls[website] + "\n\t" + k + v
		else:
			infected_urls[website] = "\n\t" + k + v


	# Write to file, replacing %3A%2F%2F with ://
	with open(script_path + "/scanlogs/Malicious-Websites.log", "w") as f:
		f.write("Infected directories: " + str(len(infected_urls)) + "\n")
		for k, v in infected_urls.iteritems():
			f.write("\n\n" + k.replace("%3A%2F%2F" , "://"))
			f.write(v)

