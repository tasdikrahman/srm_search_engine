#!/usr/bin/env python

# rewriting on the file /etc/resolve.conf
# to have the content nameserver 8.8.8.8

import os 

def rewrite() : 
	# opening the file "/etc/resolve.conf"
	file_is = open('resolv.conf','w')
	file_is.write('nameserver 8.8.8.8\n')
	file_is.close()
	## done with overwriting the file on the server

def change_dir() : 
	current_dir = os.getcwd()
	if current_dir == '/etc' : 
		# if we are already inside the /etc folder 
		rewrite() 
	else : 
		# changing the directory to /etc then 
		os.chdir("/etc")
		rewrite()
		
def reset():  
	print 'rewriting on the file /etc/resolve.conf to have content as \"nameserver 8.8.8.8\"'
	change_dir()

def main() : 
	reset()

if __name__ == '__main__':
	main() 	