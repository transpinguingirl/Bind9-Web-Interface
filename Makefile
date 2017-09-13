#
#MAKEFILE for Bind9-Webinterface
#
.PHONY: clean-pyc
HOST=127.0.0.1
PORT=2000
MAX_Clients=100
INSTALL_PATH=/sbin
LIBRARY_PATH=/lib

clean-pyc:
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
installall:
	@mkdir /etc/Bind9-Webinterface
	@mkdir $LIBRARY_PATH + 'Bind9-Webinterface/'
	#@ln -s $LIBRARY_PATH + 'Bind9-Webinterface/CIL.sh'
installdeamon:
	@mkdir $LIBRARY_PATH + 'Bind9-Webinterface/'
debug:
	cd Deamon ; python3
