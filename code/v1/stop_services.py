import os

def stop_services() : 
	print '---- >> stopping apache2 << ----'
	os.system('sudo service apache2 stop')
	os.system('sudo service apache2 status')

	print '\n---- >> stopping mysql << ----'
	os.system('sudo service mysql stop')
	os.system('sudo service mysql status')

	print '\n---- >> stopping ssh << ----'
	os.system('sudo service ssh stop')
	os.system('sudo service ssh status')

def main() : 
	stop_services()

if __name__ == '__main__' : 
	main()