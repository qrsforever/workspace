#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import os

keymap=dict()
keymap['0'] = 7
keymap['1'] = 8
keymap['2'] = 9
keymap['3'] = 10
keymap['4'] = 11
keymap['5'] = 12
keymap['6'] = 13
keymap['7'] = 14
keymap['8'] = 15
keymap['9'] = 16
keymap['up'] = 19
keymap['down'] = 20
keymap['left'] = 21
keymap['right'] = 22
keymap['enter'] = 23
keymap['vol+'] = 24
keymap['vol-'] = 25
keymap['menu'] = 82
keymap['list'] = 257
keymap['HOME'] = 3
keymap['back'] = 4
keymap['display'] = 165
keymap['chl+'] = 166
keymap['chl-'] = 167
keymap['set'] = 176
keymap['mute'] = 164
keymap['vod'] = 4403
keymap['signal'] = 4404
keymap['|<<'] = 88
keymap['>>|'] = 87
keymap['<<'] = 89
keymap['>>'] = 90
keymap['>/||'] = 85
keymap['O'] = 86


class RemoteContrl(tk.Frame):
    """docstring for RemoteContrl"""
    def __init__(self, width, height):
        self.width=width
        self.height=height
        super(RemoteContrl, self).__init__()
        self.label=tk.StringVar()
        self.maindev="unkown"
        self.master.title("TV Leeco Remote")
        self.master.geometry(self.width+"x"+self.height)
        tk.Button(
                master=self,
                bg="white", 
                font=("Arial", 12), 
                textvariable=self.label, 
                width=40,
                height=2,
                command=lambda:self._init_or_reload(1)
                ).pack(side=tk.TOP, pady=8)
        self._init_or_reload()

    def _init_or_reload(self, reload=0):
        if reload == 1:
            self.prptFm.destroy()
            self.mainFm.destroy()

        self.prptFm = self._check_devices()
        self.mainFm = self._init_main_gui()
        self.prptFm.pack()
        self.pack(expand=tk.YES, fill=tk.BOTH)

    def _radio_select_btn_enter(self, var):
        self.maindev = var.get()
        self.label.set("当前设备: "+self.maindev)
        #  self.prptFm.pack_forget()
        self.prptFm.destroy()
        self.mainFm.pack()
        pass

    def _input_event_btn_enter(self, c):
        d = "-s " + self.maindev
        cmd="adb {} shell input keyevent {}".format(d, keymap[c])
        print(cmd)
        os.system(cmd)

    def _input_text_btn_enter(self, o):
        d = "-s " + self.maindev
        cmd="adb {} shell input text {}".format(d, o.get())
        print(cmd)
        os.system(cmd)

    def _check_devices(self):
        res = os.popen("adb devices", 'r')
        devices=[]
        lineit = iter(res)
        next(lineit)
        for line in lineit:
            if (line is not None and len(line) > 2):
                devices.append(line.split('\t')[0])
        res.close() 

        prptFm = tk.Frame(self)

        v = tk.StringVar()
        v.set("")

        for text in devices:
            tk.Radiobutton(
                    master=prptFm, 
                    font=("Arial", 12), 
                    text=text,
                    variable=v, 
                    value=text,
                    #  indicatoron=0,
                    command=lambda v=v:self._radio_select_btn_enter(v)
                    ).pack(anchor=tk.W)
        if len(devices) > 0:
            self.maindev = devices[0]

        self.label.set("选择设备")
        return prptFm


    def _init_main_gui(self):

        mainFm = tk.Frame(self)

        self._fill_digit_frame(tk.Frame(mainFm)).pack()
        self._fill_middle_frame(tk.Frame(mainFm)).pack()
        self._fill_direct_frame(tk.Frame(mainFm)).pack()
        self._fill_media_frame(tk.Frame(mainFm)).pack()

        tk.Label(
                master=mainFm,
                text="----------割线-----------",
                bg="gray",
                font=("Arial", 12),
                width=self.width,
                height=2
                ).pack(anchor=(tk.N+tk.W), pady=8)

        self._make_text_frame(tk.Frame(mainFm)).pack()
        return mainFm

    def _fill_digit_frame(self, ifr):
        for idx, txt in enumerate('123456789'):
            tk.Button( 
                    master=ifr, 
                    text=txt,
                    width=10,
                    height=2, # 如果为text， 是指字符的宽高, 不是像素
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(
                            row=int(idx/3),
                            column=idx%3,
                            rowspan=1,
                            columnspan=1,
                            padx=6,
                            pady=6
                            )
        return ifr
    
    def _fill_middle_frame(self, ifr):
        strs_zh = ["回看", "0", "列表", "音量+", "静音", "频道+",  "音量-",  "设置", "频道-"]
        strs_en = ["vod", "0", "list", "vol+", "mute", "chl+", "vol-", "set", "chl-"]
        for idx, (txt_zh, txt_en) in enumerate(zip(strs_zh,strs_en)):
            m = int(idx / 3)
            n = idx % 3
            tk.Button(
                    master=ifr,
                    text=txt_zh,
                    width=10,
                    height=2,
                    command=lambda c=txt_en:self._input_event_btn_enter(c)
                    ).grid(row=m, column=n, padx=6, pady=6)
        return ifr

    def _fill_direct_frame(self, ifr):
        strs = [("显示", "display"), ("上", "up"), ("信号源", "signal"), ("左", "left"),
                ("确定", "enter"), ("右", "right"), ("菜单", "menu"), ("下", "down"), ("返回", "back")]
        for idx, (txt_zh, txt_en) in enumerate(strs):
            m = int(idx / 3)
            n = idx % 3
            tk.Button(
                    master=ifr,
                    text=txt_zh,
                    width=10,
                    height=2,
                    command=lambda c=txt_en:self._input_event_btn_enter(c)
                    ).grid(row=m, column=n, padx=6, pady=6)
        return ifr

    def _fill_media_frame(self, ifr):
        top = tk.Frame(ifr)
        top.pack()
        for idx, txt in enumerate(["|<<", "HOME", ">>|"]):
            tk.Button(
                    master=top,
                    text=txt,
                    width=10,
                    height=2,
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(row=0, column=idx, padx=6, pady=6)

        bottom = tk.Frame(ifr)
        bottom.pack()
        for idx, txt in enumerate(["<<", ">/||", "O", ">>"]):
            tk.Button(
                    master=bottom,
                    text=txt,
                    width=6,
                    height=2,
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(row=1, column=idx, padx=6, pady=6)
        return ifr

    def _make_text_frame(self, ifr):
        content = tk.StringVar()
        e = tk.Entry(
                master=ifr, 
                textvariable=content,
                font=("Arial", 16), 
                justify=tk.LEFT
                )
        e.pack(side=tk.LEFT, padx=5)
        tk.Button(
                master=ifr,
                text="Send",
                command=lambda o=e:self._input_text_btn_enter(e)
                ).pack(side=tk.RIGHT, padx=5)
        return ifr


if __name__ == "__main__":
    RemoteContrl("420", "800").mainloop()

# Learn more see: http://effbot.org/tkinterbook/
