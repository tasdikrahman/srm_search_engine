import commands
import os
# output = commands.getoutput('ps -A')
## we can do with the above command too, but since this script is going to run on a cron tab. It will take much RAM 
## on the server, so we are individually checking for each service.


def print_spaces() : 
	print "\n-----XXXXXXXXXXX----------XXXXXXXXXX--------\n"

def mongo() : 
	output_mongo = commands.getoutput('sudo service mongodb status')
	if 'running' not in output_mongo : 

		os.system('sudo service mongodb stop')
		os.system('sudo service mongodb start')

def apache() : 
	output_apache = commands.getoutput('sudo service apache2 status')
	if 'not' in output_apache : 

		os.system('sudo service apache2 stop')
		os.system('sudo service apache2 start')

def mysql() : 
	output_mysql = commands.getoutput('sudo service mysql status')
	if 'running' not in output_mysql : 

		os.system('sudo service mysql stop')
		os.system('sudo service mysql start')

def ssh() : 
	output_ssh = commands.getoutput('sudo service ssh status') 
	if 'running' not in output_ssh : 
		os.system('sudo service ssh stop')
		os.system('sudo service ssh start')
	
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
