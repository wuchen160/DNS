
# NOTE  
* Your VPS must be in China
* Only support Centos 6.7 64  or Ubuntu
* You need remove old bind version RUN `yum remove bind*`

###If you want to install on docker,please read [Install with docker](https://github.com/zyqf/DNS/wiki/Install-with-docker)

# Install 
主机系统中未包含Git组件安装代码（如不确定，请选此项）：

* `yum -y install git && cd /root && git clone https://github.com/zyqf/DNS.git  && cd DNS && python install.py`

主机系统中已包含Git组件安装代码：

* `cd /root && git clone https://github.com/zyqf/DNS.git  && cd DNS && python install.py`

###  Midway will appear the following prompt , enter the public network ip

* `Please enter your vps ip (*.*.*.*):`

#Update file rpz.zone

Centos系统将自动执行任务,Ubuntu暂未测试,如不自动执行请按照下方手动添加

* `crontab -e`

* 0 2 * * * python /root/DNS/bin/update.py
* 0 3 * * * service named restart 


#thanks list
* [@HuanMeng](https://github.com/HuanMeng0)
* [@codexss](https://github.com/codexss)
* [@tonyxue](https://github.com/tonyxue)
