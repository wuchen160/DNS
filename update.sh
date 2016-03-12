#!/bin/bash


function Get_OS_Name()
{
	egrep -i "centos" /etc/issue && OS_Name='CentOS';
	[ "$OS_Name" == '' ]
}

function Update()
{
Get_OS_Name ;
if [ ${OS_Name} == "CentOS" ];then
git pull ; 
cp $(pwd)/named/* /PandaDNS/named/ -a -f ;
cp $(pwd)/named.rfc1912.zones/named.rfc1912.zones /PandaDNS/named.rfc1912.zones -f ;
cp $(pwd)/named.conf /etc/named.conf -f ;
rndc reload ;
echo "Update Complete!";
fi;
if [ ${OS_Name} == '' ];then
	echo "The system does not support." ;
	exit;
fi;
}

Update ;
