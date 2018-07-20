#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from TCPClient import TCPClient
from res import Strings
from res import Styles
from res import Colors

gStrings = Strings.strings
gStyles = Styles.styles
gColors = Colors.colors

class WindowGUI(object):

    def __init__(self, width, height):# {{{
        """ """
        self.lan = 'en'
        self.tcp = TCPClient(2048)
        self.log = dict()
        self.width = width
        self.height = height
        self.win = tk.Tk()
        self.win.protocol('WM_DELETE_WINDOW', self.onCloseWindow)
        self.win.resizable(width=True, height=True)
        self.onGlobalConfigure()
        self.createConnectView()
        self.win.mainloop()
# }}}

    def onGlobalConfigure(self):# {{{
        self.win.title(gStrings['title'][self.lan])
        style = ttk.Style()
        style.theme_create('monitor', parent="alt", settings=gStyles['monitor'])
        style.theme_use('monitor')
# }}}

    def onInitWindow(self):# {{{
        # set window place and size
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
                self.width, self.height,
                (screenwidth - self.width) / 2,
                (screenheight - self.height) / 2)
        self.win.geometry(alignstr)

        # set menu
        self.menu_bar = tk.Menu(self.win)
        menu_set = tk.Menu(self.menu_bar)
        menu_set.add_command(
                label=gStrings['lanSwitch'][self.lan],
                command=self.onSwitchLang)
        self.menu_bar.add_cascade(label=gStrings['set'][self.lan], menu=menu_set)

        self.menu_bar.add_command(
                label=gStrings['quit'][self.lan],
                command=self.onCloseWindow)

        self.menu_bar.add_command(
                label=gStrings['about'][self.lan],
                state=tk.DISABLED,
                command=self.oShowAbout)
        self.win.config(menu=self.menu_bar)

        # set tabpage
        self.tabControl = ttk.Notebook(self.win) 
        bi_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(bi_tab, text = gStrings['basicInfo'][self.lan]) 
        log_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(log_tab, text = gStrings['logSet'][self.lan])
        dev_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(dev_tab, text = gStrings['devCtrl'][self.lan])
        self.tabControl.pack(expand=1, fill="both") 

        self.createBasicInfoView(bi_tab)
        self.createLogSetView(log_tab)
        self.createDevControlView(dev_tab)
# }}}

    def onSwitchLang(self):# {{{
        if self.lan == 'en' :
            self.lan = 'cn'
        else:
            self.lan = 'en'
        self.menu_bar.destroy()
        self.tabControl.destroy()
        self.onInitWindow()
# }}}

    def oShowAbout(self):
        pass

    def onCloseWindow(self):# {{{
        self.tcp.close()
        self.win.destroy()
# }}}

    def onConnect(self):# {{{
        addr = self.server_addr.get()
        port = self.server_port.get()
        if self.tcp.connect(addr, int(port)):
            self.conn_frm.destroy()
            self.onInitWindow()
# }}}

    def onLogButton(self, name):
        print("name ---> " + name)
        pass

    def createConnectView(self):# {{{
        width = 400
        height = 200
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (screenwidth - width) / 2,
                (screenheight - height) / 2)
        self.win.geometry(alignstr)
        self.server_addr = tk.StringVar()
        self.server_port = tk.StringVar()
        self.server_addr.set('10.59.68.13')
        self.server_port.set('8192')
        self.conn_frm = ttk.Frame(self.win, 
                padding=20, width=width, height=height)
        ttk.Label(self.conn_frm,
                text = gStrings['serverAddr'][self.lan],
                ).grid(row=1, sticky=tk.E, padx=10, pady=10)
        ttk.Entry(self.conn_frm,
                textvariable=self.server_addr,
                ).grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)
        ttk.Label(self.conn_frm,
                text = gStrings['serverPort'][self.lan],
                ).grid(row=2, sticky=tk.E, padx=10, pady=10)
        ttk.Entry(self.conn_frm, 
                textvariable=self.server_port,
                ).grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        ttk.Button(self.conn_frm,
                text = gStrings['connect'][self.lan],
                command = self.onConnect,
                ).grid(row=3, column=1, columnspan=2, sticky=tk.E, padx=12)
        self.conn_frm.pack(side=tk.BOTTOM, anchor=tk.CENTER)
# }}}

    def createBasicInfoView(self, tab):
        pass

    def createLogSetView(self, tab):# {{{
        # level frame
        i = 0
        j = 0
        level_frm = ttk.Frame(tab)
        ttk.Label(level_frm, text=gStrings['loglevel'][self.lan],
                foreground=gColors['Tomato'],
                font=('Calibri', 14)
                ).grid(row=i, column=j, columnspan=6, sticky=tk.W)
        level_frm.pack(anchor="w")

        i += 1
        j += 1
        for t in (gStrings['logModule'][self.lan], gStrings['logError'][self.lan],
                gStrings['logWarn'][self.lan], gStrings['logNormal'][self.lan],
                gStrings['logInfo'][self.lan], gStrings['logTrace'][self.lan]) :
            ttk.Label(level_frm, text=t, anchor=tk.CENTER,
                    width=12, font=('Arial', 12)
                    ).grid(row=i, column=j)
            j += 1
        i += 1
        names = self.tcp.command('getModulesName').split(';')
        for name in names:
            level = self.tcp.command('getModuleLogLevel', name)
            self.log[name] = tk.IntVar()
            self.log[name].set(int(level))
            ttk.Label(level_frm, text = name, anchor=tk.CENTER,
                    width = 15, font = ('Arial', 12)
                    ).grid(row=i, column=1)
            for j in range(1, 6):
                ttk.Radiobutton(level_frm,
                        variable = self.log[name],
                        value = j,
                        command = lambda n = name : self.onLogButton(n)
                        ).grid(row=i, column=j+1)
            i = i + 1
# }}}

    def createDevControlView(self, tab):
        pass

if __name__ == "__main__":
    app = WindowGUI(800, 800)
