#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime
import matplotlib.pyplot as plt  

logfile_live = "./android-live.logcat"
logfile_app = "./android-app.logcat"

TIMEFORMAT = "\d{2}-\d{2} (?P<datetime>\d{2}:\d{2}:\d{2}\.\d{3})"

re_keyevent = re.compile(TIMEFORMAT + ".*action=0x0, flags=0x8, keyCode=21.*")
re_l_pause = re.compile(TIMEFORMAT + ".*am_pause_activity.*Launcher\]$")
re_s_new_intent = re.compile(TIMEFORMAT + ".*am_new_intent.*com\.stv\.signalsourcemanager.*\]$")
re_l_on_pause = re.compile(TIMEFORMAT + ".*am_on_paused_called.*Launcher\]$")
re_s_resume = re.compile(TIMEFORMAT + ".*am_resume_activity.*com\.stv\.signalsourcemanager/\.MainActivity]$")
re_s_on_resume = re.compile(TIMEFORMAT + ".*am_on_resume_called.*com\.stv\.signalsourcemanager\.MainActivity]$")
re_s_draw_ok = re.compile(TIMEFORMAT + ".*ActivityManager: Draw ok$")

def parser(file):
    all_times=[]
    
    try:
        with open(file, 'rt') as lfile:
            for line in lfile:
                keyevent_ret = re_keyevent.search(line)
                if keyevent_ret is None:
                    continue
                time_sample=[]
                time_sample.append(keyevent_ret.groupdict()['datetime'])
    
                for line in lfile:
                    l_pause_ret = re_l_pause.search(line) 
                    if l_pause_ret is not None:
                        time_sample.append(l_pause_ret.groupdict()['datetime'])
    
                    s_new_intent_ret = re_s_new_intent.search(line)
                    if s_new_intent_ret is not None:
                        time_sample.append(s_new_intent_ret.groupdict()['datetime'])
    
                    l_on_pause_ret = re_l_on_pause.search(line)
                    if l_on_pause_ret is not None:
                        time_sample.append(l_on_pause_ret.groupdict()['datetime'])
    
                    s_resume_ret = re_s_resume.search(line)
                    if s_resume_ret is not None:
                        time_sample.append(s_resume_ret.groupdict()['datetime'])
    
                    s_on_resume_ret = re_s_on_resume.search(line) 
                    if s_on_resume_ret is not None:
                        time_sample.append(s_on_resume_ret.groupdict()['datetime'])
    
                    s_draw_ok_ret = re_s_draw_ok.search(line)
                    if s_draw_ok_ret is not None:
                        time_sample.append(s_draw_ok_ret .groupdict()['datetime'])
                        if len(time_sample) == 7:
                            all_times.append(time_sample)
                        break
                #  print(time_sample)
        #  print(all_times)
    
    except IOError as err:
        print("File Err: " + str(err))
    
    return all_times

def cal_time_ticks(time_sample):
    ticks=[0]
    basetime = datetime.strptime(str(time_sample[0]),"%H:%M:%S.%f")
    for i, s_time in enumerate(time_sample):
        if i == 0:
            continue
        dt = datetime.strptime(str(s_time),"%H:%M:%S.%f")
        diff = dt - basetime
        ticks.append(diff.seconds * 1000 + diff.microseconds/1000)
    return ticks


x_axes = [0, 1, 2, 3, 4, 5, 6]
x_descr = ['Input', 'L.pause', 'S.new_inent', 'L.on_pause', 'S.resume', 'S.on_resume', 'S.Draw']
colors = ['r', 'b', 'y', 'g', 'k', 'c', 'm']

plt.figure()
plt.xlim(0.0, 7)
plt.ylim(0.0, 1500)

for i, time_sample in enumerate(parser(logfile_live)):
    ticks = cal_time_ticks(time_sample)
    if i >= len(colors):
        break
    s = "sample{}".format(i)
    plt.plot(x_axes, ticks, color=colors[i], linewidth=4.5, linestyle="-", label=s)

plt.xticks(x_axes, x_descr, rotation=30)
plt.xlabel("EventStatus")
plt.ylabel("Time(ms)")
plt.title("Start Activity Time")
plt.grid(True)
plt.legend(loc='upper left')
plt.show()
