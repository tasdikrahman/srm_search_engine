#!/usr/bin/env python

'''
Author : "Tasdik Rahman"

Script to install Hadoop into your system

Note : Run this file as sudo 
'''

import os

def main() : 
	print 'Creating \"hadooop\" user  : '
	os.system("sudo adduser hadoop")

	'''
	You will now be prompted to enter the details of the user and the new password
	'''

	print '\n\n'

	### Addding this user to the sudoers list 
	os.system("sudo adduser hadoop sudo")

	print '\n\n'

	## Switch to the newly created user 

	print '\nSwitching to the newly created user  : \n'
	os.system("su - hadoop")
	print 'Current user is : '
	os.system("whoami")


	print '\n\n'

	print 'Installing default jdk : '
	os.system('sudo apt-get install default-jdk')
	print '#'*70

	print 'Installing openssh-server : '
	os.system('sudo apt-get install openssh-server')


	print 'Generating the keys for the openssh server'
	os.system('ssh-keygen -t rsa -P ""')

	print 'copying the keys : '
	os.system('cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys')

	print 'Copying the keys for password-less ssh into the system'
	os.system('ssh-copy-id -i $HOME/.ssh/id_rsa.pub hadoop@localhost')

	print 'Trying to ssh into the system'
	os.system('ssh hadoop@localhost')
	print 'logging out of localhost'
	os.system('exit')

	print 'Checking the current user'
	os.system('whoami')

	### Checking the current working directory :

	print 'Working directory : '
	os.system('pwd')

	os.chdir('/home/hadoop/')
	print 'downloading the hadoop file from the internet : '

	os.system('wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1.tar.gz')
	print('extracting it : ')

	os.system('sudo tar xzf hadoop-1.2.1.tar.gz')
	## renaming the file
	os.system('sudo mv hadoop-1.2.1 hadoop')

	## setting the permissions

	os.system('sudo chown -R hadoop:hadoop hadoop')

	print 'Modifying your /etc/profile'

	### appending the config of the files into your /etc/profile

	profile = """
export HADOOP_HOME="/home/hadoop/hadoop/"
export JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk-amd64"

unalias fs &> /dev/null
alias fs="hadoop fs"
unalias hls &> /dev/null
alias hls="fs -ls"

export PATH="$PATH:$HADOOP_HOME/bin"
###
	"""

	f = open('/etc/profile','a')  
	f.write("\n")
	f.write(profile)
	f.write("\n")
	f.close()


	############################################################
	### Editing the configuration files inside hadoop

	os.chdir('~/hadoop')
	ipv6 = """
# The java implementation to use.  Required.
export JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk-amd64"
export HADOOP_OPTS=-Djava.net.preferIPv4Stack=true
	"""

	f = open('~/hadoop/conf/hadoop-env.sh', 'a')
	f.write('\n')
	f.write('ipv6')
	f.write('\n')
	f.close()

	print 'Creating the tmp file for hadoop '

	os.system('sudo mkdir -p /app/hadoop/tmp')
	### setting the permissions
	os.system('sudo chown hadoop:hadoop /app/hadoop/tmp')
	os.system('sudo chmod 750 /app/hadoop/tmp')

	print '#'*80
	print 'Editing the core-site.xml'

	## first flushing the contents of the file
	#os.system('echo "" > ~/hadoop/conf/core-site.xml')

	content = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
 <property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
  <description>A base for other temporary directories.</description>
 </property>
 <property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
  <description>The name of the default file system.  A URI whose
  scheme and authority determine the FileSystem implementation.  The
  uri's scheme determines the config property (fs.SCHEME.impl) naming
  the FileSystem implementation class.  The uri's authority is used to
  determine the host, port, etc. for a filesystem.</description>
 </property>
</configuration>
	"""

	f = open('~/hadoop/conf/core-site.xml', 'w') 
	f.write(content)
	f.close()


	###########################################################3

	print '#'*80
	print 'Editing the mapred-site.xml'

	## first flushing the contents of the file
	#os.system('echo "" > ~/hadoop/conf/mapred-site.xml')

	content = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
 <property>
  <name>mapred.job.tracker</name>
  <value>localhost:54311</value>
  <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
  </description>
</property>
</configuration>
	"""

	f = open('~/hadoop/conf/mapred-site.xml', 'w') 
	f.write(content)
	f.close()


	###########################################################3

	print '#'*80
	print 'Editing the mapred-site.xml'

	## first flushing the contents of the file
	#os.system('echo "" > ~/hadoop/conf/mapred-site.xml')

	content = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
 <property>
  <name>mapred.job.tracker</name>
  <value>localhost:54311</value>
  <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
  </description>
</property>
</configuration>
	"""

	f = open('~/hadoop/conf/mapred-site.xml', 'w')  
	f.write(content)
	f.close()


	###########################################################3

	print '#'*80
	print 'Editing the hdfs-site.xml'

	## first flushing the contents of the file
	#os.system('echo "" > ~/hadoop/conf/hdfs-site.xml')

	content = """
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
 <property>
  <name>dfs.replication</name>
  <value>1</value>
  <description>Default block replication.
  The actual number of replications can be specified when the file is created.
  The default is used if replication is not specified in create time.
  </description>
 </property>
</configuration>
	"""

	##### Formatting the hdfs file

	f = open('~/hadoop/conf/hdfs-site.xml', 'w') 
	f.write(content)
	f.close()

	###########################################################3
	#### Starting the node 
	
	print 'formatting the name node :\n\n'
	os.system('~/hadoop/bin/hadoop namenode -format')

	print 'Starting the single node : '
	os.system('~/hadoop/bin/start-all.sh')

	#############################################################
	## checking the status of node 

	os.system('jps')
	
	print 'We are done !'

if __name__ == "__main__" : 
	main()

