wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/noarch/bind-9.10.3-3.el6.src.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/noarch/bind-license-9.10.3-3.el6.noarch.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/x86_64/bind-9.10.3-3.el6.x86_64.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/x86_64/bind-chroot-9.10.3-3.el6.x86_64.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/x86_64/bind-debuginfo-9.10.3-3.el6.x86_64.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/x86_64/bind-devel-9.10.3-3.el6.x86_64.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/x86_64/bind-libs-9.10.3-3.el6.x86_64.rpm
wget https://bkraft.fr/files/RPM%20stuff/bind-9.10.3-P3.el6.x86_64/x86_64/bind-utils-9.10.3-3.el6.x86_64.rpm

rpm -ivh bind-9.10.3-3.el6.src.rpm
rpm -ivh bind-license-9.10.3-3.el6.noarch.rpm
rpm -ivh bind-libs-9.10.3-3.el6.x86_64.rpm
rpm -ivh bind-9.10.3-3.el6.x86_64.rpm
rpm -ivh bind-chroot-9.10.3-3.el6.x86_64.rpm
rpm -ivh bind-debuginfo-9.10.3-3.el6.x86_64.rpm
rpm -ivh bind-devel-9.10.3-3.el6.x86_64.rpm
rpm -ivh bind-utils-9.10.3-3.el6.x86_64.rpm
