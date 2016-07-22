#/usr/bin/python
#dig @a.root-servers.net . ns > /usr/local/named/var/named.root
import os
import sys
filename = r'usr/local/named/var/named.root'
if os.path.exists(filename):
    print 'OK,file exists.'
else:
 	os.system('touch /usr/local/named/var/named.root')

while True:
	f = open('/usr/local/named/var/named.root','rb')
	text = f.read()
	if 'root-servers' not in text:
		os.system('dig @a.root-servers.net . ns > /usr/local/named/var/named.root')
	else:
		print 'named.root is ok'
		sys.exit()
