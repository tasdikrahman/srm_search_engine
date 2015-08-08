import commands
import os
output_mongo = commands.getoutput('sudo service mongodb status')
if 'running' not in output_mongo : 
	os.system('sudo service mongodb stop')
	os.system('sudo service mongodb start')

output_apache = commands.getoutput('sudo service apache2 status')
if 'not' in output_apache : 
	os.system('sudo service apache2 stop')
	os.system('sudo service apache2 start')

output_mysql = commands.getoutput('sudo service mysql status')
if 'running' not in output_mysql : 
	os.system('sudo service mysql stop')
	os.system('sudo service mysql start')

output_ssh = commands.getoutput('sudo service ssh status')
if 'running' not in output_ssh : 
	os.system('sudo service ssh stop')
	os.system('sudo service ssh start')