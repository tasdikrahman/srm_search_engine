import commands
import os
output = commands.getoutput('ps -A')

def print_spaces() : 
	print "\n-----XXXXXXXXXXX----------XXXXXXXXXX--------\n"

def mongo() : 
	if 'mongodb' in output : 
		print 'mongod  ------  running'
	else : 
		print 'mongodb  ------  stopped'	
		print 'starting mongodb :  '

		os.system('sudo service mongodb start')

		print '------ >> now checking the status : << ------ '
		os.system('sudo service mongodb status')

def apache() : 
	if 'apache2' in output : 
		print 'apache2  ------  running'

	else : 
		print 'apache2  ------  stopped'	
		print 'starting apache2 :  '

		os.system('sudo service apache2 start')

		print '------ >> now checking the status : << ------ '
		os.system('sudo service apache2 status')

def mysql() : 
	if 'mysqld' in output : 
		print 'mysqld  ------  running'
	else :  
		print 'mysqld  ------  stopped'
		print 'starting mysql :  '

		os.system('sudo service mysql start')

		print '------ >> now checking the status : << ------ '
		os.system('sudo service mysql status')

def ssh() : 
	if 'ssh' in output : 
		print 'ssh  ------  running'
	else : 
		print 'ssh  ------  stopped'	
		print 'starting ssh :  '

		os.system('sudo service ssh start')

		print '------ >> now checking the status : << ------ '
		os.system('sudo service ssh status')
	
def services(): 
	''' 
	Here are the services which need to be checked whether they are running on the server or not ! 
	- mysqld
	- ssh
	- mongodb 
	- apache2
	### further functions to be added would be to ###
	- start the services if they are not running
	''' 

	print "====== >> Service check module <<====== "
	print "service  ---|| ---  Status\n"

	print_spaces()
	mongo()
	########
	print_spaces()
	apache()
	########
	print_spaces()
	mysql()
	########
	print_spaces()
	ssh()

def main() : 
	services()

if __name__ == '__main__' : 
	main()
