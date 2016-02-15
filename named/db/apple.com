$TTL 1D
@	IN SOA	ns1.pandadns.com. root.pandadns.com. (
					1996022534; serial
					1024W	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
@	IN	NS	ns1.pandadns.com.
appldnld	IN	CNAME appldnld.apple.ccgslb.com.cn.
$INCLUDE db/adcdownload	adcdownload.apple.com.
configuration	IN	A	23.13.188.224
deimos3	IN	A	184.50.87.10
deimos3	IN	A	184.50.87.32
$INCLUDE	db/ess	ess.apple.com.
$INCLUDE	db/gamecenter	gc.apple.com.
itunes	IN	CNAME	itunes.apple.ccgslb.com.cn.
$INCLUDE db/itunes itunes.apple.com.
mesu	IN	A	184.50.87.26
mesu	IN	A	184.50.87.66
movies	30	IN	A	184.50.87.24
movies	30	IN	A	184.50.87.41
$INCLUDE db/phobos-chinacache	phobos.apple.com.
guzzoni	IN	A	17.174.4.4
guzzoni	IN	A	17.174.4.9
