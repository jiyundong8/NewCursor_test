#提取接口类型和编号

interface = 'GigabitEthernet0/0/1'

type = interface[:15]
port = interface[-5:]

print(f'接口类型：{type}')
print(f'接口编号：{port}')