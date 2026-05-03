#处理show version输出

version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

#去掉首尾空格
strip = version_raw.strip()
print (strip)

#把字符串转成全大写
upper = strip.upper()
print (upper)

#替换版本号
version = strip.replace('17.03.04','17.06.01')
print(version)
