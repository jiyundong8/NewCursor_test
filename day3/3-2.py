#正则表达式解析ASA防火墙连接表

import re
conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

row_format = "{:<12}{:<3}{}"
conn1 = re.match(r'^([A-Z]+)\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s+.*',conn).groups()
print (row_format.format("Protocol",":",conn1[0]))
print (row_format.format("Server IP",":",conn1[1]))
print (row_format.format("Server Port",":",conn1[2]))
print (row_format.format("Client IP",":",conn1[3]))
print (row_format.format("Client Port",":",conn1[4]))