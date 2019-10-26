#!/usr/bin/env python

import psutil
import json
import time
import configparser
import os
from datetime import datetime

config = configparser.ConfigParser()
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config.read(os.path.join(path, 'conf.ini'))
form = config['common']['output']
inter = config['common']['interval']


class Metrics:

    def cpu_load(self):
        return psutil.cpu_percent()

    def virt_memory_used(self):
        return psutil.virtual_memory().used

    def virt_memory_free(self):
        return psutil.virtual_memory().free

    def net_io_packreceived(self):
        return psutil.net_io_counters().packets_recv

    def net_io_packsent(self):
        return psutil.net_io_counters().packets_sent


a = Metrics()
mn = 60


def go():
    i = 0
    if form == "json":
        son = {}
        while True:
            now = datetime.now()
            current = now.strftime("%a, %d %b %Y %H:%M:%S +03:00")
            son['SNAPSHOT ' + str(i + 1)] = []
            son['SNAPSHOT ' + str(i + 1)].append([{
                'TIMESTAMP': current,
                'CPU load': str(a.cpu_load()) + " %",
                'Overall virtual memory used': str(a.virt_memory_used()),
                'Overall virtual memory free': str(a.virt_memory_free()),
                'Number of packets sent': str(a.net_io_packreceived()),
                'Number of packets received': str(a.net_io_packsent())
            }])
            with open('data.json', 'w') as outfile:
                json.dump(son, outfile, indent=3)
            i += 1
            time.sleep(int(inter) * mn)

    if form == "txt":
        while True:
            now = datetime.now()
            current = now.strftime("%a, %d %b %Y %H:%M:%S +03:00")
            txt = open("data.txt", "a+")
            txt.write("SNAPSHOT %d\r\nTIMESTAMP: %s\r\n" % ((i + 1), current))
            txt.write("CPU load: %s\r\nOverall virtual memory used: %s\r\nOverall virtual memory free: %s\r\n" % (
                str(a.cpu_load()) + " %",
                str(a.virt_memory_used()),
                str(a.virt_memory_free())))
            txt.write("Number of packets sent: %s\r\nNumber of packets received: %s\r\n \n" % (
                str(a.net_io_packreceived()),
                str(a.net_io_packsent())))
            txt.close()
            i += 1
            time.sleep(int(inter) * mn)


if __name__ == "__main__":
    go()

