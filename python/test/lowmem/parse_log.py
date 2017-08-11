#!/usr/bin/python3
# -*- coding: utf-8 -*-

# jira日志下载: http://pan.baidu.com/s/1nvn2A3R
import re
import os

pid2Name = {}
pnameDictMaps = {}

TIMEFORMAT = "\d{2}-\d{2} (?P<datetime>\d{2}:\d{2}:\d{2}\.\d{3})"
RE_PID = "(?P<pid>\d+)"
RE_PNAME = "(?P<pname>[a-z\.]+)"
RE_TYPE = "(?P<type>[a-z\ ]+)"
RE_COMP = "(?P<comp>[a-zA-Z\ \./]+)"
re_am_proc_start = re.compile(TIMEFORMAT + ".*am_proc_start: \[\d+," + RE_PID + ",\d+," + RE_PNAME + "," + RE_TYPE + "," + RE_COMP + "\]")

RE_OOMPID = "(?P<pid>\d+)"
re_low_mem_killer = re.compile(TIMEFORMAT + ".*Kernel.* lowmemorykiller: .*\(" + RE_OOMPID + "\), adj.*")

class AmProcStartInfo:
    def __init__(self, datetime, pid, pname, type, component):
        self.datetime = datetime
        self.pid = pid
        self.pname = pname
        self.type = type
        self.component = component
        self.killtime = "00:00:00.000"

    def getDatetime(self):
        return self.datetime

    def getPid(self):
        return self.pid

    def getComponent(self):
        return self.component

    def getType(self):
        return self.type
    
    def getKilltime(self):
        return self.killtime;

    def setKilltime(self, datetime):
        self.killtime = datetime

    def __repr__(self):
        return 'AppStartInfo({0.datetime!r}, {0.pid!r}, {0.pname!r}, {0.type!r}, {0.component!r}, {0.killtime!r})'.format(self)
    
    def __str__(self):
        return '({0.datetime!r}, {0.pid!r}, {0.pname!r}, {0.type!r}, {0.component!r}, {0.killtime!r})'.format(self)

def parse_start(file):
    with open(file, encoding="latin-1") as f:
        for line in f:
            result = re_am_proc_start.search(line)
            if result is not None:
                g = result.groupdict()
                dt = g['datetime']
                pid = g['pid']
                pname = g['pname']
                type = g['type']
                comp = g['comp']
                if not pnameDictMaps.get(pname):
                    pnameDictMaps[pname] = []
                pnameDictMaps[pname].append(AmProcStartInfo(dt, pid, pname, type, comp))
                pid2Name[pid] = pname
                continue
            
            result = re_low_mem_killer.search(line)
            if result is not None:
                g = result.groupdict()
                dt = g['datetime']
                pid = g['pid']
                if not pid2Name.get(g['pid']):
                    continue
                pname = pid2Name[pid]
                for item in pnameDictMaps[pname]:
                    if item.getPid() == pid:
                        item.setKilltime(dt);

def debug_show():
    for key, value in pnameDictMaps.items():
        print(key + ":")
        print("\t启动进程时间\t被杀死时间\t进程号\t启动类型\t启动组件")
        for item in value:
            print("\t" + item.getDatetime() + "\t" + item.getKilltime() + "\t" + item.getPid() + "\t" + item.getType() + "\t" + item.getComponent())

def file_lastnum(fname):
    match = re.search(r'.*\.(?P<num>\d{1,2})', fname)
    if match:
        return int(match.groupdict()['num'])
    
if __name__ == "__main__":
    rootdir = '/home/lidong/Downloads/jira/HERACLES/19165/testPlayHot_20170803_203235/Log.0/'
    #  rootdir = '/home/lidong/Downloads/jira/HERACLES/19165/testMenuView_20170803_203005/Log.0/'
    listfiles = os.walk(rootdir)
    logfiles=[]
    for root, dirs, files in listfiles:
        for f in files:
            match = re.search(r'logcat\.log\.\d{1,2}', f)
            if match:
                logfiles.append(f)
    
    # datetime时间戳和文件名字相关, 先对文件名排序, datetime就不需要了
    sortedfiles = sorted(logfiles, key = file_lastnum, reverse=True)
    for f in sortedfiles:
        parse_start(os.path.join(rootdir, f))

    debug_show()
