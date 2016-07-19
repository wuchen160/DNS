#!/usr/bin/python
# -*- coding: utf-8 -*-
# /usr/local/named/etc/named.conf
# @zyqf
# email:qq767026763@gmail.com
IP_ADR= raw_input('Please enter your vps ip (*.*.*.*): ')
IP_ADR_list = IP_ADR.split('.')


print "\n Creating named.conf ....... \n"
named_conf =''' 
options {
	directory "/usr/local/named/var";          
	pid-file "named.pid";
	listen-on port 53 { any; };
	#listen-on port 5353 { any; };
	listen-on-v6 port 53 { any; };
	allow-query     { any; };
	recursion yes;

	dnssec-enable yes;
	dnssec-validation yes;
	dnssec-lookaside auto;
	
	
	rate-limit {
            ipv4-prefix-length 32;
            window 10;
            responses-per-second 20;
            errors-per-second 5;
            nxdomains-per-second 5;
            slip 2;
        };

	
	response-policy { 
   		zone "rpz.zone" policy given; 
	} 
	qname-wait-recurse no;             
};

zone "." IN {
        type hint;         
        file "named.root"; 
};


zone "rpz.zone" {
    type master;
    file "/usr/local/named/var/rpz.zone";
};
include "/usr/local/named/var/named.rfc1912.zones";

'''
f=open('/usr/local/named/etc/named.conf','a')
f.write(str(named_conf))
f.close()

print "named.conf have created! \n"
print "--------------------------------------------------------- \n"



print "Creating named.empty ......."

named_empty ='''
$TTL 3H
@	IN SOA	@ rname.invalid. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	127.0.0.1
	AAAA	::1
'''

f=open('/usr/local/named/var/named.empty','a')
f.write(str(named_empty))
f.close()
print "named.empty have created! \n"
print "--------------------------------------------------------- \n"



print "Creating named.localhost ......."


named_localhost ='''
$TTL 1D
@	IN SOA	@ rname.invalid. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	127.0.0.1
	AAAA	::1
'''

f=open('/usr/local/named/var/named.localhost','a')
f.write(str(named_localhost))
f.close()

print "named.localhost have created! \n"
print "--------------------------------------------------------- \n"



print "Creating named.loopback ......."



named_loopback ='''
$TTL 1D
@	IN SOA	@ rname.invalid. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	@
	A	127.0.0.1
	AAAA	::1
'''

f=open('/usr/local/named/var/named.loopback','a')
f.write(str(named_loopback))
f.close()
print "named.loopback have created! \n"
print "--------------------------------------------------------- \n"



print "Creating named.rfc1912.zones ......."

named_rfc1912_zones ='''
// named.rfc1912.zones:
//
// Provided by Red Hat caching-nameserver package 
//
// ISC BIND named zone configuration for zones recommended by
// RFC 1912 section 4.1 : localhost TLDs and address zones
// and http://www.ietf.org/internet-drafts/draft-ietf-dnsop-default-local-zones-02.txt
// (c)2007 R W Franks
// 
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//

zone "localhost.localdomain" IN {
	type master;
	file "named.localhost";
	allow-update { none; };
};

zone "localhost" IN {
	type master;
	file "named.localhost";
	allow-update { none; };
};

zone "1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa" IN {
	type master;
	file "named.loopback";
	allow-update { none; };
};

zone "1.0.0.127.in-addr.arpa" IN {
	type master;
	file "named.loopback";
	allow-update { none; };
};

zone "0.in-addr.arpa" IN {
	type master;
	file "named.empty";
	allow-update { none; };
};

// 
zone "pandadns.com" IN {
	type master;
	file "pandadns.com.b";
};

zone "%s.%s.%s.in-addr.arpa" IN {
type master;
file "pandadns.com.arpa";
};
'''%(IP_ADR_list[2],IP_ADR_list[1],IP_ADR_list[0])

f=open('/usr/local/named/var/named.rfc1912.zones','a')
f.write(str(named_rfc1912_zones))
f.close()

print "named.rfc1912.zones have created! \n"
print "--------------------------------------------------------- \n"


print "Creating pandadns.com.arpa ......."



pandadns_com_arpa ='''
$TTL 1D
@	IN SOA	ns1.pandadns.com. root.pandadns.com. (
					1997022700	; serial
					28800	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
@	IN	NS	ns1.pandadns.com.
%s	IN	PTR	ns1.pandadns.com.
'''%IP_ADR_list[3]

f=open('/usr/local/named/var/pandadns.com.arpa','a')
f.write(str(pandadns_com_arpa))
f.close()
print "pandadns.com.arpa have created! \n"
print "--------------------------------------------------------- \n"


print "Creating pandadns.com.b ......."



pandadns_com_b ='''
$TTL 1D
@	IN SOA	ns1.pandadns.com. root.pandadns.com. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
@	IN	NS	ns1.pandadns.com.
ns1	IN	A	%s 
www	IN	A	%s
'''%(IP_ADR,IP_ADR)

f=open('/usr/local/named/var/pandadns.com.b','a')
f.write(str(pandadns_com_b))
f.close()
print "pandadns.com.b have created! \n"









