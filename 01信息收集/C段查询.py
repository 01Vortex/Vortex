#coding:utf-8
import requests
import json

def get_c(ip):
    print("正在收集{}".format(ip))
    url="http://api.webscan.cc/?action=query&ip={}".format(ip)
    req=requests.get(url=url)
    html=req.text
    data=req.json()
    if 'null' not in html:
        with open("resulit.txt", 'a', encoding='utf-8') as f:
            f.write(ip + '\n')
            f.close()
        for i in data:
            with open("resulit.txt", 'a',encoding='utf-8') as f:
                f.write("\t{} {}\n".format(i['domain'],i['title']))
                print("     [+] {} {}[+]".format(i['domain'],i['title']))
                f.close()

def get_ips(ip):
    iplist=[]
    ips_str = ip[:ip.rfind('.')]
    for ips in range(1, 256):
        ipadd=ips_str + '.' + str(ips)
        iplist.append(ipadd)
    return iplist


ip=input("请输入你要查询的ip:")

ips=get_ips(ip)
for p in ips:
    get_c(p)
