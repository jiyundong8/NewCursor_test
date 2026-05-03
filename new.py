import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#题目要求地址是196.21.5.228，这不符合我的网络设置，所以改为我机器的地址和我自己的密码
ssh.connect('192.168.0.16', port=22, username='root', password='P@ssw0rd@135', timeout=5, look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = ssh.exec_command('hostname')
print(stdout.read().decode())
ssh.close()
