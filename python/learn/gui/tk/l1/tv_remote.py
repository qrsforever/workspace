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
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.master.title("TV Remote")
        self.master.geometry(self.width+"x"+self.height)

        tk.Label(
                master=self,
                text="Leeco", 
                bg="white", 
                font=("Arial", 12), 
                width=40, 
                height=2).pack(side=tk.TOP, pady=8)

        self._fill_digit_frame(tk.Frame(self)).pack()
        self._fill_middle_frame(tk.Frame(self)).pack()
        self._fill_direct_frame(tk.Frame(self)).pack()
        self._fill_media_frame(tk.Frame(self)).pack()

        tk.Label(
                master=self,
                text="----------割线-----------",
                bg="gray",
                font=("Arial", 12),
                width=self.width,
                height=2
                ).pack(anchor=(tk.N+tk.W), pady=8)

        self._make_text_frame(tk.Frame(self)).pack()


    def _input_event_btn_enter(self, c):
        cmd="adb shell input keyevent {}".format(keymap[c])
        print(cmd)
        os.system(cmd)

    def _input_text_btn_enter(self, o):
        cmd="adb shell input text {}".format(o.get())
        print(cmd)
        os.system(cmd)

    def _fill_digit_frame(self, ifr):
        i = 0
        j = 0
        for txt in ('123456789'):
            tk.Button( 
                    master=ifr, 
                    text=txt,
                    width=10,
                    height=2, # 如果为text， 是指字符的宽高, 不是像素
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(
                            row=int(i/3),
                            column=j%3,
                            rowspan=1,
                            columnspan=1,
                            padx=6,
                            pady=6
                            )
            i += 1
            j += 1
        return ifr
    
    def _fill_middle_frame(self, ifr):
        strs_zh = ["回看", "0", "列表", "音量+", "静音", "频道+",  "音量-",  "设置", "频道-"]
        strs_en = ["vod", "0", "list", "vol+", "mute", "chl+", "vol-", "set", "chl-"]
        i = 0
        j = 0
        for txt in strs_en:
            m = int(i / 3)
            n = j % 3
            tk.Button(
                    master=ifr,
                    text=strs_zh[j],
                    width=10,
                    height=2,
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(row=m, column=n, padx=6, pady=6)
            i += 1
            j += 1
        return ifr

    def _fill_direct_frame(self, ifr):
        strs_zh = ["显示", "上", "信号源", "左", "确定", "右", "菜单", "下", "返回"]
        strs_en = ["display", "up", "signal", "left", "enter", "right", "menu", "down", "back"]
        i = 0
        j = 0
        for txt in strs_en:
            m = int(i / 3)
            n = j % 3
            tk.Button(
                    master=ifr,
                    text=strs_zh[j],
                    width=10,
                    height=2,
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(row=m, column=n, padx=6, pady=6)
            i += 1
            j += 1
        return ifr

    def _fill_media_frame(self, ifr):
        top = tk.Frame(ifr)
        top.pack()
        i = 0
        for txt in ["|<<", "HOME", ">>|"]:
            tk.Button(
                    master=top,
                    text=txt,
                    width=10,
                    height=2,
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(row=0, column=i, padx=6, pady=6)
            i += 1

        bottom = tk.Frame(ifr)
        bottom.pack()
        j = 0
        for txt in ["<<", ">/||", "O", ">>"]:
            tk.Button(
                    master=bottom,
                    text=txt,
                    width=6,
                    height=2,
                    command=lambda c=txt:self._input_event_btn_enter(c)
                    ).grid(row=1, column=j, padx=6, pady=6)
            j += 1
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

