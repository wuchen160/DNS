# PandaDNS
Better Internet

#DEMO

* DNS1:182.254.158.191

* DNS2:120.27.30.176

[more about](http://dns.pandadns.xyz/)

#Principle
* Access to blocked sites , DNS will return an access IP.

#Installation
* yum remove bind*

* git clone https://github.com/zyqf/DNS.git  && cd DNS && python install.py

#DNS server security

* add rule：iptables -A INPUT -p udp --dport 53 -m recent --set --name dnslimit

* add rule：iptables -A INPUT -p udp --dport 53 -m recent --update --seconds 2 --hitcount 18 --name dnslimit -j DROP

* save rule：service iptables save

* restart iptables：service iptables restart



#参考书籍
linux服务范例速查大全 刘丽霞 邱晓华 编著  清华大学出版社 第一版

linux网络服务配置详解 何世晓 编著 清华大学出版社  第一版

#参考途径
www.baidu.com

www.google.com

#查询IP的ISP
www.whatismyip.com/ip-address-lookup

#thanks list
* [@HuanMeng](https://github.com/HuanMeng0)
* [@codexss](https://github.com/codexss)
* [@tonyxue](https://github.com/tonyxue)
