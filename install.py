# -*- coding:utf-8 -*-
import os
os.system('service named stop')
os.system('yum install bind -y')
os.system('mv /etc/named.conf /etc/named.conf.bak')
os.system('mv /etc/named.rfc1912.zones /etc/named.rfc1912.zones.bak')
os.system('cp -f named.rfc1912.zones/named.rfc1912.zones /etc/named.rfc1912.zones')
os.system('cp -a -f named/* /var/named')
os.system('cp -f named.conf /etc/named.conf')
os.system('chmod -R 755 /etc/named.conf /var/named')
os.system('chgrp named /etc/named.conf /var/named')
os.system('setenforce 0')
os.system("sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config")
os.system('service named start')
