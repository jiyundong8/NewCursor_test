#获取设备的接口信息


import sys,os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day8_3 import ping_check
from day9_1 import ssh_exec




def get_interface_info(ip_list,username,password):
    for ip in ip_list:
        
        status, rtt = ping_check(ip)
        if status:
            print(f"[*] {ip}可达， 正在采集...")
            print(f"----------{ip} 接口信息----------")
            
            result = ssh_exec(
                ip,
                22,
                username,
                password,
                "show ip interface brief"
            )
            print(result.lstrip() + "\n\n")
        else:
            print(f"[x] {ip}不可达，跳过,不采集")

if __name__ == '__main__':
    ip_list = ['10.10.1.1','10.10.1.2','192.168.1.3']
    username = 'admin'
    password = 'P@ssw0rd@135'
    get_interface_info(ip_list,username,password)