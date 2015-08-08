import os

def check_service() : 
	print '---- >>  apache2 << ----'
	os.system('sudo service apache2 status')

	print '---- >>  mongodb << ----'
	os.system('sudo service mongodb status')

	print '\n---- >>  mysql << ----'
	os.system('sudo service mysql status')

	print '\n---- >> ssh << ----'
	os.system('sudo service ssh status')

def main() : 
	check_service()

if __name__ == '__main__' : 
	main()