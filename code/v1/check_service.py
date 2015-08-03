import commands
output = commands.getoutput('ps -A')

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

	if 'mysqld' in output : 
		print 'mysqld  ------  running'
	else :  
		print 'mysqld  ------  stopped'
	if 'ssh' in output : 
		print 'ssh  ------  running'
	else : 
		print 'ssh  ------  stopped'
	if 'mongodb' in output : 
		print 'mongod  ------  running'
	else : 
		print 'mongodb  ------  stopped'	

	if 'apache2' in output : 
		print 'apache2  ------  running'
	else : 
		print 'apache2  ------  stopped'	

def main() : 
	services()

if __name__ == '__main__' : 
	main()
