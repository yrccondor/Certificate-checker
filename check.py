# -*- coding:utf-8 -*-
import subprocess
import os
import json
import time
 
with open('config.json', 'r', encoding='UTF-8') as fr:
    config = json.load(fr)
websitelist = config['website_list']
print('------------')
time_out = str(config.get('timeout', 10))
for i in range(len(websitelist)):
    comm0 = "curl https://"+websitelist[i]+" --connect-timeout "+time_out+" -v -s -o /dev/null 2>/tmp/ca.info ; cat /tmp/ca.info"
    out_bytes0 = subprocess.check_output(comm0, shell=True)
    out_text0 = out_bytes0.decode('utf-8')
    if len(out_text0)>370:
        comm1 = "cat /tmp/ca.info | grep 'start date: '" #利用curl检查证书开始时间
        out_bytes1 = subprocess.check_output(comm1, shell=True)
        out_text1 = out_bytes1.decode('utf-8')
        comm2 = "cat /tmp/ca.info | grep 'expire date: '" #检查证书到期时间
        out_bytes2 = subprocess.check_output(comm2, shell=True)
        out_text2 = out_bytes2.decode('utf-8')
        comm3 = "cat /tmp/ca.info | grep 'issuer: '" #获取证书颁发机构
        out_bytes3 = subprocess.check_output(comm3, shell=True)
        out_text3 = out_bytes3.decode('utf-8')
        comm4 = "cat /tmp/ca.info | grep 'common name: '"
        out_bytes4 = subprocess.check_output(comm4, shell=True)
        out_text4 = out_bytes4.decode('utf-8')
        os.system('rm -f /tmp/ca.info')
        print('Certificate infomation about '+websitelist[i]+':')
        print('')
        print('Check time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print('Start: '+time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y")))
        print('End: '+time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y")))
        print('Common Name: '+out_text4[16:-1])
        print('Issuer Info: '+out_text3[11:-1])
        print('------------')
    else:
        print('Error: Connect Failed.')
        print('------------')
    time.sleep(2) #睡两秒