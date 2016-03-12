!#/usr/bin/python
import hashlib
import os,sys
 
def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash
 
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
         


os.system('rm -rf rpz.zone.nwe')
os.system('wget -O rpz.zone.nwe "https://raw.githubusercontent.com/zyqf/DNS/master-rpz/named/rpz.zone"')

old = CalcMD5("/var/named/rpz.zone")
new = CalcMD5("rpz.zone.nwe")

if old == new:
	print('nothing can update')

else:
	os.system('')	
	os.system('mv /var/named/rpz.zone /var/named/rpz.zone.bak')
	os.system('mv rpz.zone.nwe /var/named/rpz.zone')
	os.system('rndc reload')	
	print('update have done,thanks!')

