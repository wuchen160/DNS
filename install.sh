#!/bin/sh

function Get_OS_Name()
{
	egrep -i "centos" /etc/issue && OS_Name='CentOS';
	[ "$OS_Name" == '' ]
}

function Step1_Install_Package()
{
Get_OS_Name ;
echo '1)Install Package...';
if [ ${OS_Name} == "CentOS" ];then
	yum install bind -y ;
	iptables -A INPUT -p udp --dport 53 -m recent --set --name dnslimit
	iptables -A INPUT -p udp --dport 53 -m recent --update --seconds 2 --hitcount 18 --name dnslimit -j DROP
	service iptables save ;
	service iptables restart ;
	Step2_MkdirAndCopyFiles ;
fi;
if [ ${OS_Name} == '' ];then
	echo "The system does not support.You can manually install." ;
	exit;
fi;
}

function Step2_MkdirAndCopyFiles()
{
echo '2)Create dir and copy files';
mkdir /PandaDNS/named -p ;
mkdir /PandaDNS/named/data ;
mkdir /PandaDNS/named/dynamic ;
mkdir /PandaDNS/named/slaves ; 
cp $(pwd)/named/* /PandaDNS/named/ -a -f ;
cp $(pwd)/named.rfc1912.zones/named.rfc1912.zones /PandaDNS/named.rfc1912.zones -f ;
cp $(pwd)/named.conf /etc/named.conf -f ;
Step3_Service ;
}

function Step3_Service()
{
echo '3)Reload Service'
	service named restart ;
	Step4_Finish ;
}

function Step4_Finish()
{
echo '|-------------------COMPLETE-----------------------|' ;
echo '|      The script was finish.Please Check!         |' ;
echo '|   PandaDNS Project : https://github.com/zyqf/DNS |' ;
echo '|-------------------ENJOY IT!----------------------|' ;
}


Step1_Install_Package ;
