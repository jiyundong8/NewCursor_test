#把防火墙状态信息表存为字典
import re


asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

asa_dict = {}

for line in asa_conn.split('\n'):
    match = re.match(r'\S+\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s+\S+\s+\S+,\s+\S+\s+(\d+),\s+\S+\s+(\S+)', line).groups() 
          
    key = match[:4]
    value = match[4:]
    asa_dict[key] = value

#打印字典
print(asa_dict)


print("\n格式化输出:\n")

#格式化输出
for key,value in asa_dict.items():
    src_ip, src_port, dst_ip, dst_port = key
    bytes, flags = value
    print("src       : {:<15} | src_port  : {:<6} | dst       : {:<15} | dst_port  : {:<6}".format(src_ip,src_port,dst_ip,dst_port))
    print("bytes     : {:<15} | flags     : {}".format(bytes,flags))
    print("=" * 84)





