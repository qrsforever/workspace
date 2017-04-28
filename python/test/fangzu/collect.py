#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from room import RoomInfo
from urllib.request import Request, urlopen
from urllib.error import URLError
import matplotlib.pyplot as plt

WEB_SITE = "http://bj.58.com"
AREA = "gaobeidianbj"
TYPE = "zufang"
SUFFIX = "pn"
MAX_PAGES = 20

RE_ROOM = r'<p class="room">(\d{1}.*?)\s+(\d*).*?</p>.*?<div class="money">.*?(\d+).*?</div>'
COLLECT_RE = re.compile(RE_ROOM, re.S)

all_rooms = []

rooms_30to50 = []
rooms_50to70 = []
rooms_70to90 = []

def get_url(page):
    if page > MAX_PAGES:
        return None
    url = "/".join([WEB_SITE, AREA, TYPE, SUFFIX]) + str(page)
    print(url)
    return url

def show():
    #  xdata = []
    #  ydata = []
    #  plt.figure()
    #  print("")
    print("##############面积大小 30 ~ 50 ##########")
    #  cnt = rooms_30to50.count()
    #  plt.xlim(0, cnt);
    #  plt.ylim(2000, 5000)
    #  line, = plt.plot(xdata, ydata, 'r-')
    for i, x in enumerate(rooms_30to50):
        print(x)
        #  xdata.append(i)
        #  ydata.append(x[3])

    print("")
    print("##############面积大小 50 ~ 70 ##########")
    for x in rooms_50to70:
        print(x)
    print("")
    print("##############面积大小 70 ~ 90 ##########")
    for x in rooms_70to90:
        print(x)
    pass

for i in range(20):
    pagei = i + 1
    req = Request(get_url(pagei))
    try:
        html = urlopen(req)
        data = html.read()
        data = data.decode(encoding='UTF-8', errors='ignore')
        with open('pages/' + str(pagei) + '.html', 'wt') as f:
            f.write(data)
        #  with open('pages/' + str(pagei) + '.html', 'rt') as f:
            #  data = f.read()
        data = data.replace("&nbsp;", "")
        result = COLLECT_RE.findall(data)
        for item in result:
            flg = False
            for x in item:
                if x == '':
                    flg = True
                    break
            if flg == True:
                continue
            all_rooms.append(RoomInfo(AREA, *item))

        for item in all_rooms:
            #  print(item)
            area = int(item.getArea())
            if area < 29 or area > 91:
                continue
            if area > 29 and 51 > area:
                rooms_30to50.append(item)
            elif area > 49 and 71 > area:
                rooms_50to70.append(item)
            elif area > 69 and 91 > area:
                rooms_70to90.append(item)
            else:
                pass

        show()


    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print("The server couldn't fulfill the request.")
            print('Error code: ', e.code)
        else:
            print("Unknown error!")
    


#  data = "<p class=\"room\">主卧(2室)                   &nbsp;&nbsp;&nbsp;&nbsp;20㎡</p>"
