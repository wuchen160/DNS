

# PandaDNS
Better Internet

#DEMO

* DNS1:182.254.158.191

* DNS2:120.27.30.176

[more about](https://dns.pandadns.xyz/)

#INSTALLATION
### NOTE  
* Your VPS must be in China
* Only support Centos 6.X or ubuntu 
* You need remove old bind version RUN `yum remove bind*`

####If you want to install on docker,please read [Install with docker](https://github.com/zyqf/DNS/wiki/Install-with-docker)

### RUN
* `cd /root && git clone https://github.com/zyqf/DNS.git  && cd DNS && python install.py`

#UPDATE rpz.zone flie

* `python /root/DNS/bin/update.py`

#OR

* `crontab -e`

* 00 02 * * * python /root/DNS/bin/update.py

#DNS SERVER SECURITY

* add rule：`iptables -A INPUT -p udp --dport 53 -m recent --set --name dnslimit`

* add rule：`iptables -A INPUT -p udp --dport 53 -m recent --update --seconds 2 --hitcount 18 --name dnslimit -j DROP`

* save rule：`service iptables save`

* restart `iptables：service iptables restart`


#查询IP的ISP
www.whatismyip.com/ip-address-lookup

#thanks list
* [@HuanMeng](https://github.com/HuanMeng0)
* [@codexss](https://github.com/codexss)
* [@tonyxue](https://github.com/tonyxue)
