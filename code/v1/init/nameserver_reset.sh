#! /bin/sh
# /etc/init.d/

case "$1" in
	start)
		echo "starting namesetter.py"
		## running the application in the 

		python /usr/local/sbin/namesette.py
		;;
	stop)
		echo "stopping namesetter.py"
		;;
	*)
		echo "Error !"
		exit 1
		;;
esac

exit 0