import requests
import csv
import redis
from multiprocessing.pool import ThreadPool

class Test:
    def __init__(self):

        self.li_ip = []
        self.usable_ip = []

    def get_IP_from_csv(self):
        with open("../proxies.csv","r",encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                for i in row:
                    self.li_ip.append(i)

    def single_test_ip(self,ip):
        try:
            protocol = "https" if "https" in ip else "http"
            proxies = {protocol: ip}
            response = requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
            if response.status_code == 200:
                self.usable_ip.append(ip)
                print(ip)

        except Exception as e:
            print(ip + "   unUsable")


    def thread_pool(self):
        pool = ThreadPool(processes=20)
        pool.map(self.single_test_ip,(i for i in self.li_ip))
        pool.close()

    def save(self):
        con = {}
        r = redis.Redis(host='127.0.0.1', port=6379)
        if r.exists("UsableIp"):
            r.delete("UsableIp")
        for i in self.usable_ip:
            r.rpush("UsableIp", i)
        print(r.lrange("UsableIp",0,-1))
        print(r.lrange("UsableIp",0,-1))

    def run(self):
        self.get_IP_from_csv()
        self.thread_pool()
        self.save()

if __name__ == '__main__':
    test = Test()
    test.run()