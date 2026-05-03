#批量审计设备配置中的 shutdown 接口

import os
import shutil

files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}

result = [ ]
os.makedirs("backup", exist_ok=True)

for filename, content in files.items():
    file_path = os.path.join("backup",filename)
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(content)


    if os.path.isfile(file_path):
        with open(file_path, 'r',encoding='utf-8') as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                

                if "shutdown" in line and "no shutdown" not in line:
                    result.append(filename)
                    break

print ("发现包含 shutdown 接口的设备配置文件:")
for name in result:
    print(name)


shutil.rmtree("backup")
print("backup/ 目录已清理")
    