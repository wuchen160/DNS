#-*- code:utf-8 -*-
#!/bin/python
#
import hashlib
import os,sys
import platform

DowdloadURL = 'https://o5obpsd7a.qnssl.com/bind.tar.gz'
GccFilepath = '/tmp/bind.tar.gz'
system_platform = platform.platform()

if os.getuid() != 0 :
	print "Please run with root!"
	exit()



def select_platform(system_platform):
	if "buntu" in system_platform:
		print 'start Install on Ubuntu '
		os.system('sudo bash bin/alpha_ubuntu.sh')
	elif "entos" in system_platform:
		print 'start Install on Centos '
		os.system('sudo bash bin/centos.sh')
	else :
		print "WARM:NOT SUPPORT YOUR SYSTEM!"

	
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

def Downloadfile(URL):
	if os.path.exists(GccFilepath):
		print 'File has existed!'
		checkfile(GccFilepath)

	else:
		os.system('cd /tmp')
		os.system('wget -O bind.tar.gz ' + URL)
		if checkfile(GccFilepath) == 'error':
			print 'Download a error file , please check your network! '



def checkfile(ck_filepath):
	MD5 = CalcMD5(ck_filepath)
	if MD5 != '173ce5e83e9ba31f8368367ee1ff7807':
		print 'But it Md5 is error!'
		print 'error MD5:' , MD5
		os.system('rm -rf /tmp/bind.tar.gz')
		Downloadfile(DowdloadURL)
		return 'error'


if __name__ == '__main__':
	
	Downloadfile(DowdloadURL)
	select_platform(system_platform)
