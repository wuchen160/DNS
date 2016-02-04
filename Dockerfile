FROM centos:latest

RUN yum install -y bind && \
    rm -rf /var/cache/yum/*

ADD named.conf  /etc/named.conf
ADD named.rfc1912.zones/named.rfc1912.zones /etc/named.rfc1912.zones
ADD named /var/named

#RUN ln -sf /dev/stdout /var/named/data/named.run

EXPOSE 53/udp

CMD ["/usr/sbin/named", "-f", "-u", "named"]