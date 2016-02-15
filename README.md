

#Principle

Access to blocked sites , DNS will return an access IP.

#Installation
* 1.yum install bind -y

* 2.Replace the same file server directory file /etc/named.conf for the project root directory

* 3.Replace the file server directory for the project directory named.rfc1912.zones /etc/named.rfc1912.zones inside named.rfc1912.zones file

* 4.Under this item, the directory named all files uploaded to the server directory /var/named/under

* 5.run: service named start

#DNS server security

iptables -A INPUT -p udp --dport 53 -m recent --set --name dnslimit

iptables -A INPUT -p udp --dport 53 -m recent --update --seconds 2 --hitcount 18 --name dnslimit -j DROP

service iptables save

#原理

访问某些被封锁的网站,DNS将返回一个可以访问的IP.

#优点
较hosts来说,用户只要改个DNS即可省去频繁更新hosts文件的烦恼.

#缺点
* 1.信任问题,DNS服务器既可以返回正确的IP,也可以返回错误的IP,如恶意劫持域名,甚至利用DNS指向钓鱼网站.

* 2.服务器必须位于国内,但是考虑到国内环境,如果DNS服务做的众人皆知,恐怕离查水表不远了,如HelloDNS.

#那么...
那么,希望通过本项目,建立一个又一个的DNS节点~~~~


#快速搭建DNS
* 1.yum install bind -y

* 2.替换服务器目录文件 /etc/named.conf 为本项目 根目录的同名文件



* 3.替换服务器目录文件 /etc/named.rfc1912.zones 为本项目 目录 named.rfc1912.zones 下 named.rfc1912.zones文件



* 4.把本项目 目录 named 下所有文件上传至服务器目录 /var/named/ 下



* 5.启动: service named start


#DNS服务器安全
配置防火墙防止DDos攻击及放大攻击

添加规则：iptables -A INPUT -p udp --dport 53 -m recent --set --name dnslimit

添加规则：iptables -A INPUT -p udp --dport 53 -m recent --update --seconds 2 --hitcount 18 --name dnslimit -j DROP

说明：利用recent和state模块限制单IP在2s内只能与本机建立18个新连接。被限制一分钟后即可恢复访问

保存规则：service iptables save

参看规则是否生效：

iptables -L -n

重启iptables

service iptables restart

#参考书籍
linux服务范例速查大全 刘丽霞 邱晓华 编著  清华大学出版社 第一版

linux网络服务配置详解 何世晓 编著 清华大学出版社  第一版

#参考途径
www.baidu.com

www.google.com

#查询IP的ISP
www.whatismyip.com/ip-address-lookup

#感谢名单

@ codexss
@ tonyxue
