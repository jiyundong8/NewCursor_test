#paramiko：SSH 登录 Linux 查询默认网关

import paramiko
import re

def ssh_exec(host, port, username, password,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username, password=password, timeout=5, look_for_keys=False, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode()
    ssh.close()
    return result

def get_default_gateway(route_output):
    for line in route_output.splitlines():
        if line.startswith('0.0.0.0'):
            match = re.match(r'0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.*UG', line)
            if match:
                return match.group(1)
    return None

if __name__ == '__main__':
#题目要求地址是196.21.5.228，网关为192.21.5.1. 这不符合我的网络设置，所以改为我机器的地址和网关地址
    host = '192.168.0.16'
    username = 'root'
    password = 'P@ssw0rd@135'

    output = ssh_exec(host, 22, username, password, "route -n")
   
    gateway = get_default_gateway(output)
    
    if gateway:
        print(f'默认网关为: {gateway}')
    else:
        print('未找到默认网关')