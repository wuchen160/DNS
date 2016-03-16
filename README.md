近期将更新编译安装bind9.10.3.p3的脚本，勿运行/bin/ 下的安装脚本。

# PandaDNS
Better Internet

#DEMO

* DNS1:182.254.158.191

* DNS2:120.27.30.176

[more about](http://dns.pandadns.xyz/)

#INSTALLATION
### NOTE  
* Your VPS must be in China
* Only support Centos 6.X
* You need remove old bind version RUN `yum remove bind*`

### RUN
* `git clone https://github.com/zyqf/DNS.git  && cd DNS && sh install.sh`

#UPDATE rpz.zone flie

* `python /root/DNS/bin/update.py`

or

* `crontab -e`

* 00 02 * * * python /root/DNS/bin/update.py

#DNS SERVER SECURITY

* add rule：`iptables -A INPUT -p udp --dport 53 -m recent --set --name dnslimit`

* add rule：`iptables -A INPUT -p udp --dport 53 -m recent --update --seconds 2 --hitcount 18 --name dnslimit -j DROP`

* save rule：`service iptables save`

* restart `iptables：service iptables restart`



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
