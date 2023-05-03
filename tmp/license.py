import subprocess
import os
import re

result=os.popen('wsl ifconfig').read()
with open('F:/temp.txt',mode='wb') as f:
    f.write(result.encode())
    print('临时文件保存完成')

f=open("F:/temp.txt","r")
d=f.read()
print(d)
eth=re.findall('ether (.*?)  txqueuelen',d)[0]
eth0=eth.replace(':','')
print(eth0)

os.system('C:/Users/44572/Documents/scl_keygen/scl_keygen.exe')
#cp /mnt/c/Users/44572/Documents/scl_keygen /home/wen/synopsys/scl/admin/license
os.remove('F:/temp.txt')