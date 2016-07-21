
### NOTE  
* Your VPS must be in China
* Only support Centos 6.7 64  or Ubuntu
* You need remove old bind version RUN `yum remove bind*`

####If you want to install on docker,please read [Install with docker](https://github.com/zyqf/DNS/wiki/Install-with-docker)

### RUN
* `cd /root && git clone https://github.com/zyqf/DNS.git  && cd DNS && python install.py`

#OR

* `crontab -e`

* 00 02 * * * python /root/DNS/bin/update.py
* 00 03 * * * service named restart


#thanks list
* [@HuanMeng](https://github.com/HuanMeng0)
* [@codexss](https://github.com/codexss)
* [@tonyxue](https://github.com/tonyxue)
