#监控设备配置改变

import sys,os
import re
import hashlib
import time
from day9_1 import ssh_exec

def get_config_md5(config):
    m = hashlib.md5()
    m.update(config.encode())
    return m.hexdigest()

def monitor_config(ip,username,password):
    last_md5 = None

    while True:
        result = ssh_exec(
            ip,
            22,
            username,
            password,
            "show running-config"
        )
    #print(result)
        output = re.search(r'(hostname[\s\S]+end)', result)
        if output:
            config = output.group()
            current_md5 = get_config_md5(config)                      

            if last_md5 and current_md5 != last_md5:
                print ("[!] 告警: 配置已改变！新 MD5: ",current_md5)
                break

            print("[*] 当前配置 MD5:", current_md5)  

            last_md5 = current_md5            
       
       
        else:
            print("No Match Found")

        time.sleep(5)
    


if __name__ == '__main__':
    ip = '10.10.1.1'
    username = 'admin'
    password = 'P@ssw0rd@135'
    monitor_config(ip,username,password)