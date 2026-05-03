#制作一个能配置路由器的 SSH 交互函数
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.1.1', port=22, username='admin', password='Cisco123',
            timeout=5, look_for_keys=False, allow_agent=False)

chan = ssh.invoke_shell()
time.sleep(1)
print(chan.recv(2048).decode())   # 查看登录提示符

# chan.send(b'terminal length 0\n')
# time.sleep(1)
# print(chan.recv(2048).decode())

# chan.send(b'show version\n')
# time.sleep(2)
# print(chan.recv(4096).decode())

# chan.send(b'config ter\n')
# time.sleep(1)
# print(chan.recv(2048).decode())

# chan.send(b'router ospf 1\n')
# time.sleep(1)
# print(chan.recv(2048).decode())

ssh.close()