#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from TCPClient import TCPClient
from LogThread import LogThread
from res import Strings
from res import Styles
from res import Colors

gStrings = Strings.strings
gStyles = Styles.styles
gColors = Colors.colors

class WindowGUI(object):

    def __init__(self, width, height, svr_addr, svr_port, host_addr, host_port):# {{{
        """ """
        self.lan = 'cn'
        self.tcp = TCPClient(2048)
        self.logthread = LogThread()
        self.log = dict()

        # window
        self.width = width
        self.height = height
        self.win = tk.Tk()
        self.win.protocol('WM_DELETE_WINDOW', self.onCloseWindow)
        self.win.resizable(width=True, height=True)
        self.screenwidth = self.win.winfo_screenwidth()
        self.screenheight = self.win.winfo_screenheight()

        # homebrain address / port
        self.server_addr = tk.StringVar()
        self.server_port = tk.StringVar()
        self.server_addr.set(svr_addr)
        self.server_port.set(svr_port)

        # host address / port
        self.host_addr = tk.StringVar()
        self.host_port = tk.StringVar()
        self.host_addr.set(host_addr)
        self.host_port.set(host_port)

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
        alignstr = '%dx%d+%d+%d' % (
                self.width, self.height,
                (self.screenwidth - self.width) / 2,
                (self.screenheight - self.height) / 2)
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
        self.bi_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.bi_tab, text = gStrings['basicInfo'][self.lan])
        self.log_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.log_tab, text = gStrings['logSet'][self.lan])
        self.dev_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.dev_tab, text = gStrings['ruleCtrl'][self.lan])
        self.tabControl.pack(expand=1, fill="both")

        self.createBasicInfoView(self.bi_tab)
        self.createLogSetView(self.log_tab)
        self.createRuleControlView(self.dev_tab)
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

    def oShowAbout(self):# {{{
        pass# }}}}}}

    def onCloseWindow(self):# {{{
        if self.logthread:
            self.onLogTerminate()
        self.tcp.close()
        self.win.destroy()
# }}}

    def onConnect(self):# {{{
        addr = self.server_addr.get()
        port = self.server_port.get()
        if self.tcp.connect(addr, int(port)):
            self.conn_frm.destroy()
            self.onInitWindow()
        else:
            self.conn_frm.destroy()
            self.onConnectError()
# }}}

    def onBack(self, destoryFrm, showFunc):# {{{
        destoryFrm.destroy()
        showFunc()
# }}}

    def createConnectView(self):# {{{
        width = 360
        height = 200
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (self.screenwidth - width) / 2,
                (self.screenheight - height) / 2)
        self.win.geometry(alignstr)
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

    def onConnectError(self):# {{{
        width = 360
        height = 150
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (self.screenwidth - width) / 2,
                (self.screenheight - height) / 2)
        self.win.geometry(alignstr)
        self.connerr_frm = ttk.Frame(self.win,
                padding=20, width=width, height=height)
        ttk.Label(self.connerr_frm,
                text = gStrings['connErr'][self.lan],
                ).grid(row=0, sticky=tk.NS, padx=10, pady=10)
        ttk.Button(self.connerr_frm,
                text = gStrings['back'][self.lan],
                command = lambda : self.onBack(self.connerr_frm, self.createConnectView)
                ).grid(row=1, column=1, sticky=tk.W, padx=12)
        ttk.Button(self.connerr_frm,
                text = gStrings['quit'][self.lan],
                command = self.onCloseWindow,
                ).grid(row=1, column=2, sticky=tk.E, padx=12)
        self.connerr_frm.pack(side=tk.BOTTOM, anchor=tk.CENTER)
# }}}

    def createBasicInfoView(self, tab):# {{{
        ver_frm = ttk.Frame(tab)
        ttk.Label(ver_frm, text=gStrings['versionInfo'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).grid(row=0, column=0, columnspan=2, sticky=tk.W)
        ver_frm.pack(anchor="w")

        ttk.Label(ver_frm, text=gStrings['hbVer'][self.lan],
                width = 15, font = ('Arial', 12)
                ).grid(row=1, column=0)

        ttk.Label(ver_frm, text=self.tcp.command('getHomeBrainVersion'),
                width = 15, font = ('Arial', 12)
                ).grid(row=1, column=1)

        ttk.Label(ver_frm, text=gStrings['reVer'][self.lan],
                width = 15, font = ('Arial', 12)
                ).grid(row=2, column=0)

        ttk.Label(ver_frm, text=self.tcp.command('getRuleEngineVersion'),
                width = 15, font = ('Arial', 12)
                ).grid(row=2, column=1)
# }}}

    def createLogSetView(self, tab):# {{{
        # level frame
        i = 0
        j = 0
        level_frm = ttk.Frame(tab)
        ttk.Label(level_frm, text=gStrings['loglevel'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
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
            if level == "":
                continue
            self.log[name] = tk.IntVar()
            self.log[name].set(int(level))
            ttk.Label(level_frm, text = name, anchor=tk.CENTER,
                    width = 15, font = ('Arial', 12)
                    ).grid(row=i, column=1)
            for j in range(1, 6):
                ttk.Radiobutton(level_frm,
                        variable = self.log[name],
                        value = j,
                        command = lambda n = name, l = str(j) : self.tcp.command('setModuleLogLevel', n, l)
                        ).grid(row=i, column=j+1)
            i = i + 1

        log_frm = ttk.Frame(tab)
        ttk.Label(log_frm, text=gStrings['logOutput'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(log_frm, text=gStrings['host'][self.lan]).grid(row=1, column=0)
        ttk.Entry(log_frm, textvariable=self.host_addr).grid(row=1, column=1)
        ttk.Label(log_frm, text=gStrings['port'][self.lan]).grid(row=1, column=2, padx=10)
        ttk.Entry(log_frm, textvariable=self.host_port).grid(row=1, column=3)
        ttk.Button(log_frm, text = gStrings['output'][self.lan],
                command = self.onLogOutput,
                ).grid(row=1, column=4, sticky=tk.W, padx=10)
        ttk.Button(log_frm, text = gStrings['terminate'][self.lan],
                command = self.onLogTerminate,
                ).grid(row=1, column=5, sticky=tk.W, padx=10)
        log_frm.pack(anchor="w")
        self.log_text = tk.Text(tab, wrap=tk.NONE,
                width=self.width, height=30
                )
        hscroll = tk.Scrollbar(tab, orient=tk.HORIZONTAL,
                command=self.log_text.xview
                )
        hscroll.pack(side=tk.BOTTOM, fill=tk.X)
        vscroll = tk.Scrollbar(tab, orient=tk.VERTICAL,
                command=self.log_text.yview
                )
        vscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=vscroll.set)
        self.log_text.config(xscrollcommand=hscroll.set)
        self.log_text.pack()
# }}}

    def onLogOutput(self):# {{{
        if self.logthread.isAlive():
            return
        addr = self.server_addr.get()
        port = self.server_port.get()
        def output(log):
            self.log_text.insert(tk.END, log)
        self.logthread.start(addr, port, output);
        self.tcp.command('startUDPLog', addr, port);

    def onLogTerminate(self):
        self.logthread.stop()
        self.tcp.command('stopUDPLog')

# }}}

    def createRuleControlView(self, tab):# {{{
        sel_frm = ttk.Frame(tab)
        sel_frm.pack()

        #  Devices
        ttk.Label(sel_frm, text=gStrings['deviceSel'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).pack(side=tk.LEFT)
        self.device_var = tk.StringVar()
        self.device_list = ttk.Combobox(sel_frm,
                takefocus=False, state='readonly',
                width=20, textvariable=self.device_var,
                exportselection=0, font=('Arial', 14))
        result = self.tcp.command('getDevices')
        devices = ('<NONE>')
        if len(result) > 0:
            devices = result.split(';')
        self.device_list['values'] = devices
        self.device_list.current(0)
        self.device_list.bind("<<ComboboxSelected>>", self.onDeviceSelected)
        self.device_list.pack(side=tk.LEFT)
        ttk.Label(sel_frm, text=gStrings['deviceID'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).pack(side=tk.LEFT, padx=(15, 0))

        #  Instances
        self.ins_var = tk.StringVar()
        self.ins_list = ttk.Combobox(sel_frm,
                takefocus=False, state='readonly',
                width=35, textvariable=self.ins_var,
                exportselection=0, font=('Arial', 14))
        inses = self.tcp.command('getInstaces', devices[0])
        values = ('<NONE>')
        if len(inses) > 0:
            values = inses.split(';')
        self.ins_list['values'] = values
        self.ins_list.current(0)
        self.ins_list.bind("<<ComboboxSelected>>", self.onInstanceSelected)
        self.ins_list.pack(side=tk.LEFT)

        ttk.Button(sel_frm, width=5,
                text=gStrings['refresh'][self.lan],
                command=self.onInstanceSelected,
                ).pack(side=tk.LEFT, padx=(20,0))

        self.onInstanceSelected()
# }}}

    def onDeviceSelected(self, *args):# {{{
        inses = self.tcp.command('getInstaces', self.device_list.get())
        values = ('<NONE>')
        if len(inses) > 0:
            values = inses.split(';')
        self.ins_list['values'] = values
        self.ins_list.current(0)
        self.onInstanceSelected()
# }}}

    def onInstanceSelected(self, *args):# {{{
        try:
            self.pro_frm.destroy()
            del self.curslot_vars
        except Exception as e:
            print("don't worry, that's ok!")
        self.pro_frm = ttk.Frame(self.dev_tab)
        slots = ()
        self.curslot_vars = {}
        result = self.tcp.command('getSlots', self.device_list.get())
        if len(result) > 0:
            slots = result.split(';')

        j = 0
        for pro in slots:
            ttk.Label(self.pro_frm, text=pro, anchor=tk.CENTER,
                    relief=tk.GROOVE, width=15
                    ).grid(row=1, column=j, columnspan=2, pady=(10,10), padx=(5,5))
            uuid = self.ins_list.get()
            if uuid != '<NONE>':
                self.curslot_vars[pro] = tk.StringVar()
                val = self.tcp.command('getInstanceValue', uuid, pro)
                if not val.strip():
                    val = 'null'
                self.curslot_vars[pro].set(val)
                ttk.Entry(self.pro_frm, width=10,
                        font=('Arial', 12),
                        textvariable=self.curslot_vars[pro],
                        ).grid(row=2, column=j, columnspan=2, pady=(10,10))
                ttk.Button(self.pro_frm, width=5,
                        text=gStrings['setVal'][self.lan] + 'R',
                        command=lambda u=uuid, p=pro : self.onUpdateValue('R', u, p),
                        ).grid(row=3, column=j, pady=5, padx=2, sticky=tk.E)
                ttk.Button(self.pro_frm, width=5,
                        text=gStrings['setVal'][self.lan] + 'D',
                        command=lambda u=uuid, p=pro : self.onUpdateValue('D', u, p),
                        ).grid(row=3, column=j+1, pady=5, padx=2, sticky=tk.W)
            j += 2
        self.pro_frm.pack()
# }}}

    def onUpdateValue(self, target, uuid, pro):# {{{
        if target == 'R':
            self.tcp.command('updateInstanceValue', uuid, pro, self.curslot_vars[pro].get())
        else:
            self.tcp.command('updateDeviceValue', uuid, pro, self.curslot_vars[pro].get())
# }}}

if __name__ == "__main__":
    app = WindowGUI(880, 800)
