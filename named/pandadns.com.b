$TTL 1D
@	IN SOA	ns1.pandadns.com. root.pandadns.com. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
@	IN	NS	ns1.pandadns.com.
ns1	IN	A	120.27.30.176 
www	IN	A	120.27.30.177

;需要修改120.27.30.176为vps公网ip 
;
