#制作一个能配置路由器的 SSH 交互函数
import paramiko
import time

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    """
    参数说明：
      cmd_list  : 要执行的命令列表，例如 ['terminal length 0', 'show version']
      enable    : enable 密码，若设备无需 enable 则保持默认空字符串
      wait_time : 每条命令发送后等待设备响应的秒数
      verbose   : True 则打印每条命令的返回结果，False 则静默执行
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, look_for_keys=False, allow_agent=False)

    chan = ssh.invoke_shell()
    time.sleep(1)
   
    output = chan.recv(4096).decode()
    if verbose:
        print(output)

    if enable:
        chan.send('enable\n')
        time.sleep(1)
        chan.send(enable +'\n')
        time.sleep(wait_time)

        output = chan.recv(4096).decode()
        if verbose:
            print(output)

    for cmd in cmd_list:
        chan.send(cmd + '\n')
        time.sleep(wait_time)

        output = chan.recv(4096).decode()

        
        if verbose:
            print(f"{'='*20}{cmd}{'='*20}")
            print(output)

    ssh.close()
    return output        
    

if __name__ == '__main__':
    cmd_list = [
    'terminal length 0',
    'show version',
    'config ter',
    'router ospf 1',
    'network 10.0.0.0 0.0.0.255 area 0',
    'end',
]
    ip = '10.10.1.1'
    username = 'admin'
    password = 'Cisco123'
    enable = 'P@ssw0rd@135'
    qytang_multicmd(ip,username,password,cmd_list,enable)