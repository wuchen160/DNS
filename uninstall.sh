#!/bin/bash

function Get_OS_Name()
{
	egrep -i "centos" /etc/issue && OS_Name='CentOS';
	[ "$OS_Name" == '' ]
}

function Uninstall()
{
Get_OS_Name ;
if [ ${OS_Name} == "CentOS" ];then
	yum remove bind* -y ;
	rm -rf /PandaDNS ;
	Finish ;
fi;
if [ ${OS_Name} == '' ];then
	echo "The system does not support." ;
	exit;
fi;
	
}

function Finish()
{
echo '|-------------------COMPLETE-----------------------|' ;
echo '|      The script was finish.Please Check!         |' ;
echo '|   PandaDNS Project : https://github.com/zyqf/DNS |' ;
echo '|--------------------THANKS------------------------|' ;
echo '| @HuanMeng0 @codexss @tonyxue                     |' ;
echo '|-------------------GOODBYE!-----------------------|' ;
}

Uninstall ;
