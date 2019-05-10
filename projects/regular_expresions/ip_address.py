
import re
f=open('F:/projects/regular_expresions/device_config.txt')

fobj=f.read()
ip=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',fobj)
count=0
for i in ip:
   count+=1
   print(i)
print('total number of ip_addresses:',count)