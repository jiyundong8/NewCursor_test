#正则表达式练习：从 route -n 输出中查找网关

import os
result = os.popen("route -n").read()

lines = result.strip().split("\n")

print(lines)

gateway = None

for line in lines[2:]:
    parts = line.split()
    if parts[0] == "0.0.0.0" and "UG" in parts[3]:
        gateway = parts[1]

print("网关为:   ", gateway)
