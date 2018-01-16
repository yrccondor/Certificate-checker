# -*- coding:utf-8 -*-
import subprocess
import os
import json
import time
 
with open('config.json', 'r', encoding='UTF-8') as fr:
    config = json.load(fr)
output_type = config.get('output', "print")
if output_type == "print_details":
    print("["+time.strftime("%H:%M:%S", time.localtime())+"] Read config.json successfully.")
websitelist = config['website_list']
if output_type == "print_details":
    print("["+time.strftime("%H:%M:%S", time.localtime())+"] Read website_list successfully. "+str(len(websitelist))+" web site(s) will be scaned.")
time_out = str(config.get('timeout', 10))
if output_type == "print_details":
    print("["+time.strftime("%H:%M:%S", time.localtime())+"] Read timeout successfully. Value: "+str(time_out)+"s")
sleep_time = config.get('sleep', 2)
if output_type == "print_details":
    print("["+time.strftime("%H:%M:%S", time.localtime())+"] Read output successfully. Value: "+str(sleep_time)+"s")
for i in range(len(websitelist)):
    if output_type == "print_details":
        print("["+time.strftime("%H:%M:%S", time.localtime())+"] Scanning "+websitelist[i]+"("+str(i+1)+" in "+str(len(websitelist))+").")
    comm0 = "curl https://"+websitelist[i]+" --connect-timeout "+time_out+" -v -s -o /dev/null 2>/tmp/ca.info ; cat /tmp/ca.info"
    out_bytes0 = subprocess.check_output(comm0, shell=True)
    out_text0 = out_bytes0.decode('utf-8')
    if len(out_text0)>370:
        if output_type == "print_details":
            print("["+time.strftime("%H:%M:%S", time.localtime())+"] Read reponse successfully.")
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
        if output_type == "print_details":
            print("["+time.strftime("%H:%M:%S", time.localtime())+"] Read certificate infomation successfully.")
        os.system('rm -f /tmp/ca.info')
        if output_type == "print_details":
            print("["+time.strftime("%H:%M:%S", time.localtime())+"] Environment cleaned.")
        if i == 0:
            print('-----------------------------')
        elif output_type == "print_details":
            print('-----------------------------')
        print('Certificate infomation about '+websitelist[i]+':')
        print('')
        print('Check time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print('Start: '+time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y")))
        print('End: '+time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y")))
        print('Common Name: '+out_text4[16:-1])
        print('Issuer Info: '+out_text3[11:-1])
        print('-----------------------------')
    else:
        if output_type == "print_details":
            print("["+time.strftime("%H:%M:%S", time.localtime())+"] No reponse(Time out).")
        if i == 0:
            print('-----------------------------')
        elif output_type == "print_details":
            print('-----------------------------')
        print('Error: Connect Failed.')
        print('-----------------------------')
        os.system('rm -f /tmp/ca.info')
    time.sleep(sleep_time)