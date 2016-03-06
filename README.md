# PandaDNS
Better Internet

#Principle
Access to blocked sites , DNS will return an access IP.

#Installation

git clone https://github.com/zyqf/DNS.git  && cd DNS && python install.py

#DNS服务器安全(DNS server security)
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

#thanks list
* [@HuanMeng](https://github.com/HuanMeng0)
* [@codexss](https://github.com/codexss)
* [@tonyxue](https://github.com/tonyxue)
