#正则表达式 + os模块解析ifconfig并ping网关
import re
import os
result = os.popen("ifconfig ens33").read()
print(result)

 
row_format = "{:<10}{:<3}{}"
result_mod = re.match(r'(?:\S+\s+){5}((?:\d{1,3}\.){3}\d{1,3})\s+\S+\s+((?:\d{1,3}\.){3}\d{1,3})\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?:\S+\s+){7}((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\s+.*',result).groups()


print (row_format.format("IP",":",result_mod[0]))
print (row_format.format("Netmask",":",result_mod[1]))
print (row_format.format("Broadcast",":",result_mod[2]))
print (row_format.format("MAC",":",result_mod[3]))

ip = result_mod[0]
gateway = ".".join((ip.split("."))[:3]) + ".1"
ping_result = os.popen(f"ping -c 4 {ip}").read()

print(ping_result)