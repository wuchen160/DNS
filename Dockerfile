FROM centos:6.7

RUN yum install -y bind && \
    rm -rf /var/cache/yum/*

ADD ./named.conf  /etc/named.conf
ADD ./named.rfc1912.zones /etc/named.rfc1912.zones
ADD ./named /var/named

CMD ["/usr/sbin/named", "-f", "-u", "named"]
