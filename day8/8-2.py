#While 循环：监控 TCP/80 HTTP 服务是否开放

import os
import time
import re


pattern = re.compile(r'^tcp.*\S+:80\s+.*')



while True:
    result = os.popen('ss -tulnp').read()
    found = False
    
    for line in result.splitlines():
        if pattern.search(line):
            found = True
            break

    if found:
        print("[!] 告警: TCP/80 已开放！请检查是否为授权服务。")
        break
    else:
        print("[*] 检测中... TCP/80 未监听")

    time.sleep(1)
