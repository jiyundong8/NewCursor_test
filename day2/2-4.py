# 打印接口状态巡检报告

intf1 = "Gi0/0"
status1 = "up"
speed1 = "1G"
intf2 = "Gi0/1"
status2 = "down"
speed2 = "1G"
intf3 = "Gi0/2"
status3 = "up"
speed3 = "10G"

row_format = "{:<16}{:<16}{}"

print(row_format.format("接口","状态","速率"))
print("-"*37)
print(row_format.format(intf1, status1, speed1))
print(row_format.format(intf2, status2, speed2))
print(row_format.format(intf3, status3, speed3))
