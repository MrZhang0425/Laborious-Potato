import requests
import csv
import redis

li_ip = []
usable_ip = []
with open("proxies.csv","r",encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        for i in row:
            li_ip.append(i)


for ip in li_ip:
    try:
        protocol = "https" if "https" in ip else "http"
        proxies = {protocol: ip}
        response = requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
        if response.status_code == 200:
            usable_ip.append(ip)
            print(ip)

    except Exception as e:
        print(ip + "   unUsable")

r = redis.Redis(host='127.0.0.1',port=6379)
for i in range(len(usable_ip)):
    con = {i:usable_ip[i]}
    r.set("UsableIp",con)
print(r.get("UsableIp"))
print(type(r.get("UsableIp")))