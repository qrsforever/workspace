#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import threading
import tkinter as tk
from configparser import ConfigParser
from tkinter import ttk
from TCPClient import TCPClient
from LogThread import LogThread
from res import Strings
from res import Styles
from res import Colors

gStrings = Strings.strings
gStyles = Styles.styles
gColors = Colors.colors

gFormatRuleStr = '''(defrule %s

  =>
    (bind ?c (create-rule-context %s))

)
'''

TOCKEN = '^'

class WindowGUI(object):

    def __init__(self, width, height):# {{{
        """ """
        self.lan = 'cn'
        self.tcp = TCPClient(4096)
        self.log = dict()

        # window
        self.width = width
        self.height = height
        self.win = tk.Tk()
        self.win.protocol('WM_DELETE_WINDOW', self.onCloseWindow)
        self.win.resizable(width=True, height=False)
        self.screenwidth = self.win.winfo_screenwidth()
        self.screenheight = self.win.winfo_screenheight()

        cf = ConfigParser()
        cf.read('config.ini')

        # homebrain address / port
        self.server_addr = tk.StringVar()
        self.server_port = tk.StringVar()
        self.server_addr.set(cf.get('HB', 'ServerAddress'))
        self.server_port.set(cf.get('HB', 'ServerPort'))

        # host address / port
        self.host_addr = tk.StringVar()
        self.host_port = tk.StringVar()
        self.host_addr.set(cf.get('HB', 'LogUDPAddress'))
        self.host_port.set(cf.get('HB', 'LogUDPPort'))

        self.filter_key = tk.StringVar()
        self.grep_key = tk.StringVar()
        self.rule_newn_var = tk.StringVar()
        self.rule_switch_var = tk.StringVar()
        self.rule_btm_sw = 0

        self.onGlobalConfigure()
        self.createConnectView()
        self.win.mainloop()
# }}}

    def onGlobalConfigure(self):# {{{
        self.win.title(gStrings['title'][self.lan])
        style = ttk.Style()
        style.theme_create('monitor', parent="alt", settings=gStyles['monitor'])
        style.theme_use('monitor')
        #  data = {}
        #  for e in style.element_names():
        #      data[e] = style.element_options(e)
        #  print(data)
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
        self.log_tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.log_tab2, text = gStrings['logSet2'][self.lan])
        self.dev_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.dev_tab, text = gStrings['ruleCtrl'][self.lan])
        self.dev_tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.dev_tab2, text = gStrings['ruleEdit'][self.lan])
        self.scene_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.scene_tab, text = gStrings['sceneAuto'][self.lan])
        self.tabControl.pack(expand=1, fill=tk.BOTH)

        self.createBasicInfoView(self.bi_tab)
        self.createLogSetView(self.log_tab)
        self.createLogSetView2(self.log_tab2)
        self.createRuleControlView(self.dev_tab)
        self.createRuleControlView2(self.dev_tab2)
        self.createSceneAutoView(self.scene_tab)
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
        try:
            if self.logthread:
                self.onLogTerminate()
            self.tcp.close()
        except Exception as e:
            print("don't worry, that's ok", e)
        finally:
            cf = ConfigParser()
            cf.add_section('HB')
            cf.set('HB', 'ServerAddress', self.server_addr.get())
            cf.set('HB', 'ServerPort', self.server_port.get())
            cf.set('HB', 'LogUDPAddress', self.host_addr.get())
            cf.set('HB', 'LogUDPPort', self.host_port.get())
            cf.write(open('config.ini', 'w'))
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
                ).pack(side=tk.LEFT)
        ver_frm.pack(anchor=tk.W)

        cols = [gStrings['version'][self.lan], gStrings['creator'][self.lan],
                gStrings['buildtime'][self.lan], gStrings['buildtype'][self.lan]]
        cols_size = (200, 100, 200, 100)
        targets = ['rule-engine', 'clips']

        tree = ttk.Treeview(tab, columns=cols, height=len(targets))
        #  ttk.Style().configure("Treeview", background='red', foreground='yellow')
        #  ttk.Style().configure("Treeview.Heading", foreground='green')
        #  tree.tag_configure("row", font=('Arial', 14))
        tree.pack(fill=tk.X, padx=(30, 30), expand=0) # if expand=1, Y:center
        for i in range(0, len(cols)):
            tree.column(cols[i], minwidth=50, width=cols_size[i], anchor=tk.CENTER, stretch=True)
            tree.heading(cols[i], text=cols[i])

        for j in range(0, len(targets)):
            result = self.tcp.command('getBuildInfo', targets[j])
            tree.insert("", j, text=targets[j], values=result.split(TOCKEN)) # tags=("row",)
# }}}

    def createLogSetView(self, tab):# {{{
        # level frame
        i = 0
        j = 0
        top_frm = ttk.Frame(tab)
        top_frm.pack(anchor=tk.W)

        # Log Level
        level_frm = ttk.Frame(top_frm)
        ttk.Label(level_frm, text=gStrings['loglevel'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).grid(row=i, column=j, columnspan=6, sticky=tk.W)
        level_frm.pack(side=tk.LEFT)

        i += 1
        j += 1
        for t in (gStrings['logModule'][self.lan], gStrings['logError'][self.lan],
                gStrings['logWarn'][self.lan], gStrings['logNormal'][self.lan],
                gStrings['logInfo'][self.lan], gStrings['logTrace'][self.lan]) :
            ttk.Label(level_frm, text=t, anchor=tk.CENTER, width=13).grid(row=i, column=j)
            j += 1
        i += 1
        names = self.tcp.command('getModulesName').split(TOCKEN)
        for name in names:
            level = self.tcp.command('getModuleLogLevel', name)
            if level == "":
                continue
            self.log[name] = tk.IntVar()
            self.log[name].set(int(level))
            ttk.Label(level_frm, text = name, anchor=tk.CENTER, width=13).grid(row=i, column=1)
            for j in range(1, 6):
                ttk.Radiobutton(level_frm,
                        variable = self.log[name],
                        value = j,
                        command = lambda n = name, l = str(j) : self.tcp.command('setModuleLogLevel', n, l)
                        ).grid(row=i, column=j+1)
            i = i + 1

        # CLP Watch
        watch_frm = ttk.Frame(tab)
        watch_frm.pack(anchor=tk.W)

        ttk.Label(watch_frm, text=gStrings['watch'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).grid(row=0, column=0, columnspan=5, pady=(20, 10), sticky=tk.W)

        i = 1
        witems = (('rules', 'statistics', 'facts', 'activations'),
                ('slots', 'instances', 'deffunctions', 'generic-functions'),
                ('globals', 'methods', 'messages', 'message-handlers'))
        for row in witems:
            j = 1
            for item in row:
                var = tk.IntVar()
                ttk.Checkbutton(watch_frm, text=item,
                        width=16, variable=var,
                        command=lambda v=var, m=item:self.onLogWatchCheck(v, m)
                        ).grid(row=i, column=j, padx=(8, 2), pady=5)
                j = j + 1
            i += 1
# }}}

    def createLogSetView2(self, tab):# {{{
        # Log Output
        log_frm = ttk.Frame(tab)
        ttk.Label(log_frm, text=gStrings['logOutput'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(log_frm, text=gStrings['host'][self.lan]).grid(row=1, column=0)
        ttk.Entry(log_frm, width=16, textvariable=self.host_addr).grid(row=1, column=1)
        ttk.Label(log_frm, text=gStrings['port'][self.lan]).grid(row=1, column=2, padx=5)
        ttk.Entry(log_frm, width=7, textvariable=self.host_port).grid(row=1, column=3, padx=5)
        self.output_btn = ttk.Button(log_frm, text = gStrings['output'][self.lan],
                command = self.onLogOutput,)
        self.output_btn.grid(row=1, column=4, sticky=tk.W, padx=5)
        ttk.Button(log_frm, text = gStrings['terminate'][self.lan],
                command = self.onLogTerminate,
                ).grid(row=1, column=5, sticky=tk.W, padx=5)
        ttk.Button(log_frm, text = gStrings['clear'][self.lan],
                command = self.onLogClear,
                ).grid(row=1, column=6, sticky=tk.W, padx=5)
        ttk.Label(log_frm, text=gStrings['filter'][self.lan]).grid(row=1, column=7)
        ttk.Entry(log_frm, width=15, textvariable=self.filter_key).grid(row=1, column=8, padx=5)
        ttk.Entry(log_frm, width=15, textvariable=self.grep_key).grid(row=1, column=9, padx=5)
        ttk.Button(log_frm, text = gStrings['grepText'][self.lan],
                command = self.onLogGrepWindow,
                ).grid(row=1, column=10, sticky=tk.W, padx=(5, 10))
        ttk.Button(log_frm, text = gStrings['printItem'][self.lan],
                command = self.onLogPrintListDialog,
                ).grid(row=1, column=11, sticky=tk.W, padx=(5, 5))

        log_frm.pack(anchor="w")

        # Log Text
        self.log_text = tk.Text(tab, wrap=tk.NONE,
                width=self.width, height=self.height
                )
        self.log_text.bind("<Control-Key-a>", self.onLogSelectText)
        self.log_text.bind("<Control-Key-A>", self.onLogSelectText)
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

    def onLogWatchCheck(self, var, item):# {{{
        self.tcp.command('watchItem', str(var.get()), item)
# }}}

    def onLogOutput(self):# {{{
        self.logthread = LogThread()
        addr = self.host_addr.get()
        port = self.host_port.get()
        def output(log):
            if self.filter_key.get():
                for line in log.splitlines():
                    # TODO using re
                    if self.filter_key.get() in line:
                        self.log_text.insert(tk.END, line+"\n")
                        self.log_text.see(tk.END)
            else:
                self.log_text.insert(tk.END, log)
                self.log_text.see(tk.END)
        self.logthread.start(addr, port, output);
        self.tcp.command('startUDPLog', addr, port);
        self.output_btn.configure(state=tk.DISABLED)
# }}}

    def onLogTerminate(self):# {{{
        self.tcp.command('stopUDPLog')
        for i in range(0, 3):
            if self.logthread.isAlive():
                self.logthread.stop()
                time.sleep(0.2)
        self.output_btn.configure(state=tk.NORMAL)
# }}}

    def onLogClear(self):# {{{
        self.log_text.delete(0.0, tk.END)
# }}}

    def onLogPrintListDialog(self):# {{{
        try:
            self.print_dialog.destroy()
        except Exception as e:
            print("don't worry, that's ok!")
        width = 180
        height = 255
        self.print_dialog = tk.Toplevel()
        self.print_dialog.title(gStrings['selectItem'][self.lan])
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (self.screenwidth - self.width)/2 + (self.width - width) - 40,
                (self.screenheight - self.height)/2 + 60)
        self.print_dialog.geometry(alignstr)
        dialog_frm = ttk.Frame(self.print_dialog,
                padding=10, width=width, height=height)
        self.debug_items = ('mem', 'fact', 'template', 'instance', 'class', 'rule', 'agenda', 'global')
        log_listbox = tk.Listbox(dialog_frm, selectmode=tk.SINGLE,
                height=len(self.debug_items), font=('Arial', 14))
        for item in self.debug_items:
            log_listbox.insert(tk.END, gStrings[item][self.lan])
        log_listbox.bind('<Button-1>', self.onClickDebugListBox)
        log_listbox.pack(side=tk.TOP, anchor=tk.CENTER, fill=tk.BOTH)
        ttk.Button(dialog_frm,
                text = gStrings['quit'][self.lan],
                command = lambda : self.onClickQuit('logprint')
                ).pack(side=tk.RIGHT, pady=(20, 10))
        dialog_frm.pack(side=tk.TOP, anchor=tk.CENTER, fill=tk.BOTH)
# }}}

    def onLogGrepWindow(self):# {{{
        width = self.width
        height = self.height
        grep_dialog = tk.Toplevel()
        grep_dialog.title(gStrings['logGrep'][self.lan])
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (self.screenwidth - width) / 2,
                (self.screenheight - height) / 2 + 30)
        grep_dialog.geometry(alignstr)
        grep_frm = ttk.Frame(grep_dialog,
                padding=10, width=width, height=height)
        grep_text = tk.Text(grep_frm, wrap=tk.NONE,
                width=self.width, height=self.height
                )
        grep_text.bind("<Control-Key-a>", self.onGrepSelectText)
        grep_text.bind("<Control-Key-A>", self.onGrepSelectText)
        hscroll = tk.Scrollbar(grep_frm, orient=tk.HORIZONTAL,
                command=grep_text.xview
                )
        hscroll.pack(side=tk.BOTTOM, fill=tk.X)
        vscroll = tk.Scrollbar(grep_frm, orient=tk.VERTICAL,
                command=grep_text.yview
                )
        vscroll.pack(side=tk.RIGHT, fill=tk.Y)
        grep_text.config(yscrollcommand=vscroll.set)
        grep_text.config(xscrollcommand=hscroll.set)
        grep_text.pack()
        grep_frm.pack(side=tk.TOP, anchor=tk.CENTER)

        if self.grep_key.get():
            txt = self.log_text.get("1.0", tk.END)
            key = self.grep_key.get()
            for line in txt.splitlines():
                if key in line:
                    grep_text.insert(tk.END, line+"\n")
                    grep_text.see(tk.END)
# }}}

    def createRuleControlView(self, tab):# {{{
        sel_frm = ttk.Frame(tab)
        sel_frm.pack(pady=(6, 20))

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
        devices = ('<NONE>',)
        if len(result) > 0:
            devices = result.split(TOCKEN)
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
                width=25, textvariable=self.ins_var,
                exportselection=0, font=('Arial', 14))
        inses = self.tcp.command('getInstaces', devices[0])
        values = ('<NONE>',)
        if len(inses) > 0:
            values = inses.split(TOCKEN)
        self.ins_list['values'] = values
        self.ins_list.current(0)
        self.ins_list.bind("<<ComboboxSelected>>", self.onInstanceSelected)
        self.ins_list.pack(side=tk.LEFT)

        self.manual_refresh_btn = ttk.Button(sel_frm, width=8,
                text=gStrings['manualRefresh'][self.lan],
                command=self.onInstanceSelected)
        self.manual_refresh_btn.pack(side=tk.LEFT, padx=(20,0))

        self.sw_auto_refresh = 0;
        auto_refresh_ins = tk.IntVar()
        auto_refresh_ins.set(3)
        self.auto_refresh_btn = ttk.Button(sel_frm, width=8,
                text=gStrings['autoRefresh'][self.lan],
                command=lambda var=auto_refresh_ins : self.onAutoRefreshInstance(var))
        self.auto_refresh_btn.pack(side=tk.LEFT, padx=(15,0))
        self.auto_refresh_entry = ttk.Entry(sel_frm, width=3, justify=tk.CENTER,
                textvariable=auto_refresh_ins)
        self.auto_refresh_entry.pack(side=tk.LEFT, padx=(8,0))

        self.onInstanceSelected()
# }}}

    def createRuleControlView2(self, tab):# {{{
        rul_frm = ttk.Frame(tab)
        rul_frm.pack(side=tk.TOP, expand=1, fill=tk.Y, pady=(20,0))
        rul_ctl_frm = ttk.Frame(rul_frm);
        rul_ctl_frm.pack(fill=tk.Y, anchor=tk.NW)

        ttk.Label(rul_ctl_frm, text=gStrings['ruleSel'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).pack(side=tk.LEFT)
        self.rule_var = tk.StringVar()
        self.rule_list = ttk.Combobox(rul_ctl_frm,
                takefocus=False, state='readonly',
                width=23, textvariable=self.rule_var,
                exportselection=0, font=('Arial', 14))
        result = self.tcp.command('getRules')
        rules = ('<NONE>',)
        if len(result) > 0:
            rules = result.split(TOCKEN)
        self.rule_list['values'] = rules
        self.rule_list.current(0)
        self.rule_list.bind("<<ComboboxSelected>>", self.onRuleSelected)
        self.rule_list.pack(side=tk.LEFT, padx=(2,8))

        self.rule_refresh_btn = ttk.Button(rul_ctl_frm, width=5,
                text=gStrings['refresh'][self.lan],
                command=self.onRefreshRules,
                )
        self.rule_refresh_btn.pack(side=tk.LEFT, padx=(8,8))
        self.rule_ci_btn = ttk.Button(rul_ctl_frm,
                text=gStrings['commit'][self.lan],
                command = self.onRuleCommit)
        self.rule_ci_btn.pack(side=tk.LEFT, padx=(8,8))
        ttk.Button(rul_ctl_frm,
                text=gStrings['delete'][self.lan],
                command = self.onRuleDeleteDialog
                ).pack(side=tk.LEFT, padx=(8,8))
        ttk.Button(rul_ctl_frm,
                textvariable=self.rule_switch_var,
                command = self.onRuleSwitch
                ).pack(side=tk.LEFT, padx=(8,12))
        self.rule_newn_btn = ttk.Button(rul_ctl_frm,
                text=gStrings['new'][self.lan],
                command=lambda : self.onRuleNew('save'))
        self.rule_newn_btn.pack(side=tk.LEFT, padx=(8,8))
        self.rule_newn_entry = ttk.Entry(rul_ctl_frm,
                textvariable=self.rule_newn_var,
                state=tk.DISABLED, font=('Arial', 14))
        self.rule_newn_entry.pack(side=tk.LEFT, padx=(8,8))
        self.rule_cancel_btn = ttk.Button(rul_ctl_frm, width=5,
                text=gStrings['cancel'][self.lan],
                command=lambda : self.onRuleNew('cancel'))

        self.rule_text = tk.Text(rul_frm, wrap=tk.NONE,
                width=100, height=25, font=('Arial', 14)
                )
        hscroll = tk.Scrollbar(rul_frm,
                orient=tk.HORIZONTAL,
                command=self.rule_text.xview)
        hscroll.pack(side=tk.BOTTOM, fill=tk.X)
        vscroll = tk.Scrollbar(rul_frm,
                orient=tk.VERTICAL,
                command=self.rule_text.yview)
        vscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.rule_text.config(yscrollcommand=vscroll.set)
        self.rule_text.config(xscrollcommand=hscroll.set)
        self.rule_text.pack(side=tk.BOTTOM, anchor=tk.CENTER, expand=1, fill=tk.Y)
        self.rule_text.bind("<Control-Key-a>", self.onRuleSelectText)
        self.rule_text.bind("<Control-Key-A>", self.onRuleSelectText)
        self.onRuleSelected()
# }}}

    def onDeviceSelected(self, *args):# {{{
        inses = self.tcp.command('getInstaces', self.device_list.get())
        values = ('<NONE>',)
        if len(inses) > 0:
            values = inses.split(TOCKEN)
        self.ins_list['values'] = values
        self.ins_list.current(0)
        self.onInstanceSelected()
# }}}

    def onAutoRefreshInstance(self, var):# {{{
        # refresh thread
        def _refresh_thread(delay):
            while not self.stop_auto_refresh:
                #  self.onInstanceSelected() # blinking because fresh by thread.
                self.manual_refresh_btn.invoke()
                time.sleep(delay)

        if self.sw_auto_refresh == 0:
            self.stop_auto_refresh = False
            threading.Thread(target=_refresh_thread, args=(var.get(),)).start()
            self.auto_refresh_btn.configure(text=gStrings['stopRefresh'][self.lan])
            self.auto_refresh_entry.configure(state=tk.DISABLED)
            self.sw_auto_refresh = 1
        else:
            self.stop_auto_refresh = True
            self.auto_refresh_btn.configure(text=gStrings['autoRefresh'][self.lan])
            self.auto_refresh_entry.configure(state=tk.NORMAL)
            self.sw_auto_refresh = 0
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
            slots = result.split(TOCKEN)

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
                        font=('Arial', 12), justify=tk.CENTER,
                        textvariable=self.curslot_vars[pro],
                        ).grid(row=2, column=j, columnspan=2, pady=(10,10))
                ttk.Button(self.pro_frm, width=5,
                        text=gStrings['setVal'][self.lan] + 'R',
                        command=lambda u=uuid, p=pro : self.onUpdateValue('setR', u, p),
                        ).grid(row=3, column=j, pady=5, padx=2, sticky=tk.E)
                ttk.Button(self.pro_frm, width=5,
                        text=gStrings['getVal'][self.lan] + 'R',
                        command=lambda u=uuid, p=pro : self.onUpdateValue('getR', u, p),
                        ).grid(row=4, column=j, pady=5, padx=2, sticky=tk.E)
                ttk.Button(self.pro_frm, width=5,
                        text=gStrings['setVal'][self.lan] + 'D',
                        command=lambda u=uuid, p=pro : self.onUpdateValue('setD', u, p),
                        ).grid(row=3, column=j+1, pady=5, padx=2, sticky=tk.W)
                ttk.Button(self.pro_frm, width=5,
                        text=gStrings['getVal'][self.lan] + 'D',
                        command=lambda u=uuid, p=pro : self.onUpdateValue('getD', u, p),
                        ).grid(row=4, column=j+1, pady=5, padx=2, sticky=tk.W)
            j += 2
        self.pro_frm.pack()
# }}}

    def onUpdateValue(self, target, uuid, pro):# {{{
        if target == 'setR':
            self.tcp.command('updateInstanceValue', uuid, pro, self.curslot_vars[pro].get())
        elif target == 'setD':
            self.tcp.command('updateDeviceValue', uuid, pro, self.curslot_vars[pro].get())
        elif target == 'getR':
            val = self.tcp.command('getInstanceValue', uuid, pro)
            if not val.strip():
                val = 'null'
            self.curslot_vars[pro].set(val)
        elif target == 'getD':
            val = self.tcp.command('getDeviceValue', uuid, pro)
            if not val.strip():
                val = 'null'
            self.curslot_vars[pro].set(val)
        else:
            print('unkown target:', target)
# }}}

    def onRefreshRules(self):# {{{
        result = self.tcp.command('getRules')
        rules = ('<NONE>',)
        if len(result) > 0:
            rules = result.split(TOCKEN)
        self.rule_list['values'] = rules
        self.rule_list.current(0)
        self.onRuleSelected()
# }}}

    def onGrepSelectText(self, event):# {{{
        self.grep_text.tag_add(tk.SEL, "1.0", tk.END)
        return 'break'# }}}

    def onLogSelectText(self, event):# {{{
        self.log_text.tag_add(tk.SEL, "1.0", tk.END)
        return 'break'# }}}

    def onRuleSelectText(self, event):# {{{
        self.rule_text.tag_add(tk.SEL, "1.0", tk.END)
        return 'break'# }}}

    def onRuleCommit(self):# {{{
        name = self.rule_list.get()
        doc = self.rule_text.get(0.0, tk.END)
        self.tcp.command('commitRuleScript', name, doc.strip())
        #  self.rule_refresh_btn.invoke()
# }}}

    def onRuleDeleteDialog(self):# {{{
        width = 320
        height = 120
        self.rule_dialog = tk.Toplevel()
        self.rule_dialog.title(gStrings['delruletitle'][self.lan])
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (self.screenwidth - width) / 2,
                (self.screenheight - height) / 2)
        self.rule_dialog.geometry(alignstr)
        dialog_frm = ttk.Frame(self.rule_dialog,
                padding=10, width=width, height=height)
        ttk.Label(dialog_frm,
                text=gStrings['delete'][self.lan],
                ).grid(row=1, padx=(5, 2))
        ttk.Label(dialog_frm, font=('Arial', 14),
                text=self.rule_list.get() + " ?",
                ).grid(row=1, column=1, columnspan=2, padx=(0,2))
        ttk.Button(dialog_frm,
                text = gStrings['confirm'][self.lan],
                command = lambda : self.onClickConfirm('delrule')
                ).grid(row=3, column=1, padx=12, pady=(20, 20))
        ttk.Button(dialog_frm,
                text = gStrings['cancel'][self.lan],
                command = lambda : self.onClickCancel('delrule')
                ).grid(row=3, column=2, padx=12, pady=(20, 20))
        dialog_frm.pack(side=tk.TOP, anchor=tk.CENTER, fill=tk.X)
# }}}

    def onRuleSelected(self, *args):# {{{
        ruleId = self.rule_list.get()
        doc = self.tcp.command('getRuleScript', ruleId)
        if doc:
            self.rule_text.delete(0.0, tk.END)
            self.rule_text.insert(0.0, doc);
            sw = self.tcp.command('getRuleSwitch', ruleId)
            if sw == '1':
                self.rule_switch_var.set(gStrings['stop'][self.lan])
            else:
                self.rule_switch_var.set(gStrings['start'][self.lan])
# }}}

    def onRuleSwitch(self):# {{{
        ruleId = self.rule_list.get()
        val = self.rule_switch_var.get()
        if val == gStrings['stop'][self.lan]:
            self.tcp.command('switchRule', ruleId, 'false')
        else:
            self.tcp.command('switchRule', ruleId, 'true')
        time.sleep(0.2)
        self.onRuleSelected()
# }}}

    def onRuleNewDialog(self):# {{{
        width = 300
        height = 160
        self.rule_dialog = tk.Toplevel()
        self.rule_dialog.title(gStrings['newruletitle'][self.lan])
        alignstr = '%dx%d+%d+%d' % (
                width, height,
                (self.screenwidth - width) / 2,
                (self.screenheight - height) / 2)
        self.rule_dialog.geometry(alignstr)
        self.rule_newn_var.set('rul-')
        dialog_frm = ttk.Frame(self.rule_dialog,
                padding=10, width=width, height=height)
        ttk.Label(dialog_frm,
                text=gStrings['rulePrompt'][self.lan],
                foreground=gColors['SlateBlue'],
                ).grid(row=0, column=1, columnspan=2, sticky=tk.E)
        ttk.Label(dialog_frm,
                text=gStrings['filename'][self.lan],
                ).grid(row=1, sticky=tk.E)
        ttk.Entry(dialog_frm, font=('Arial', 14),
                textvariable=self.rule_newn_var,
                ).grid(row=1, column=1, columnspan=2, sticky=tk.W)
        ttk.Button(dialog_frm,
                text = gStrings['confirm'][self.lan],
                command = lambda : self.onClickConfirm('newrule')
                ).grid(row=3, column=1, padx=12, pady=(20, 20))
        ttk.Button(dialog_frm,
                text = gStrings['cancel'][self.lan],
                command = lambda : self.onClickCancel('newrule')
                ).grid(row=3, column=2, padx=12, pady=(20, 20))
        dialog_frm.pack(side=tk.TOP, anchor=tk.CENTER)
# }}}

    def onRuleNew(self, who):# {{{
        if self.rule_btm_sw == 0:
            # new rule
            self.onRuleNewDialog()
            self.rule_list.configure(state=tk.DISABLED)
            self.rule_ci_btn.configure(state=tk.DISABLED)
            self.rule_refresh_btn.configure(state=tk.DISABLED)
            self.rule_newn_entry.configure(state=tk.NORMAL)
            self.rule_newn_btn.configure(text=gStrings['save'][self.lan])
            self.rule_text.delete(0.0, tk.END)
            self.rule_btm_sw = 1
            return

        # save rule
        if who == 'save':
            name = self.rule_newn_entry.get()
            doc = self.rule_text.get(0.0, tk.END)
            self.tcp.command('commitRuleScript', name, doc)
            time.sleep(1) # wait save cmd finished
            result = self.tcp.command('getRules')
            rules = result.split(TOCKEN)
            if not name in rules:
                return

        self.rule_list.configure(state=tk.NORMAL)
        self.rule_ci_btn.configure(state=tk.NORMAL)
        self.rule_refresh_btn.configure(state=tk.NORMAL)
        self.rule_newn_entry.configure(state=tk.DISABLED)
        self.rule_cancel_btn.forget()
        self.rule_newn_var.set('')
        self.rule_newn_btn.configure(text=gStrings['new'][self.lan])
        self.rule_btm_sw = 0

        self.rule_refresh_btn.invoke()
# }}}

    def onClickDebugListBox(self, event):# {{{
        index = event.widget.nearest(event.y)
        self.filter_key.set('clips_')
        self.tcp.command("printItem", self.debug_items[index]);
# }}}

    def onClickConfirm(self, who):# {{{
        if who == 'newrule':
            rule_id = self.rule_newn_var.get()
            self.rule_text.insert(0.0, gFormatRuleStr % (rule_id, rule_id))
            self.rule_cancel_btn.pack(side=tk.RIGHT, padx=(10,10))
            self.rule_dialog.destroy()
            return

        if who == 'delrule':
            self.tcp.command('deleteRuleScript', self.rule_list.get())
            time.sleep(1) # wait delete cmd finished
            self.rule_dialog.destroy()
            self.rule_refresh_btn.invoke()
            return

        if who == 'assert':
            fact = self.assert_var.get()
            if fact[0] != '(' or fact[-1] != ')':
                fact = "(" + fact + ")"
            self.tcp.command('assertFact', fact)
            self.cmd2_display.set(self.cmd1_display.get())
            self.cmd1_display.set(fact)
            return

# }}}

    def onClickCancel(self, who):# {{{
        if who == 'newrule':
            self.rule_newn_var.set('')
            self.rule_dialog.destroy()
            self.onRuleNew('cancel')
            return

        if who == 'delrule':
            self.rule_dialog.destroy()
            return
# }}}

    def onClickQuit(self, who):# {{{
        if who == 'logprint':
            self.print_dialog.destroy()
            self.filter_key.set('')
            return
# }}}

    def createSceneAutoView(self, tab):# {{{
        mode_frm = ttk.Frame(tab)
        mode_frm.pack(anchor=tk.W)

        ttk.Label(mode_frm, text=gStrings['modeTrigger'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).pack(side=tk.LEFT)

        modes_list_frm = ttk.Frame(tab)
        modes_list_frm.pack(anchor=tk.CENTER)

        scenes = (
                    ('comehome', 'leavehome', 'entermovie', 'exitmovie', 'sleep', 'getup'),
                )
        i = 0
        for ms in scenes:
            for j in range(0, 6):
                btn = ttk.Button(modes_list_frm, width=10,
                        text=gStrings[ms[j]][self.lan],
                        command=lambda m=ms[j]:self.onSceneSelected(m))
                btn.grid(row=i, column=j, padx=(10, 20), pady=(20, 10))
            i += 1

        virtual_frm = ttk.Frame(tab)
        virtual_frm.pack(anchor=tk.W)

        ttk.Label(virtual_frm, text=gStrings['virtualmode'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).pack(side=tk.LEFT)

        virtual_mode_frm = ttk.Frame(tab)
        virtual_mode_frm.pack(anchor=tk.CENTER)
        modes = (
                    ('vnone', 'vgetup', 'vsleep', 'vwater', 'vsmoke', 'vgas', 'vsos', 'vinfrared'),
                )
        k = 0
        for ms in modes:
            for j in range(0, 8):
                btn = ttk.Button(virtual_mode_frm, width=6,
                        text=gStrings[ms[j]][self.lan],
                        command=lambda idx=j:self.onVirtualModeSelected(idx))
                btn.grid(row=k, column=j, padx=(10, 20), pady=(20, 10))
            k += 1

        fact_frm = ttk.Frame(tab)
        fact_frm.pack(anchor=tk.W)

        ttk.Label(fact_frm, text=gStrings['factTrigger'][self.lan],
                foreground=gColors['Tomato'],
                font=('Arial', 14)
                ).pack(side=tk.LEFT)

        fact_stmt_frm = ttk.Frame(tab)
        fact_stmt_frm.pack(anchor=tk.CENTER)

        self.assert_var = tk.StringVar()
        ttk.Entry(fact_stmt_frm, font=('Arial', 14), width=50,
                textvariable=self.assert_var,
                ).grid(row=1, column=1, sticky=tk.W)
        ttk.Button(fact_stmt_frm,
                text = gStrings['assert'][self.lan],
                command = lambda : self.onClickConfirm('assert')
                ).grid(row=1, column=2, padx=20)


        cmd_rec_frm = ttk.Frame(tab, width=self.width)
        cmd_rec_frm.pack(side=tk.BOTTOM, fill=tk.X)
        self.cmd1_display = tk.StringVar()
        self.cmd2_display = tk.StringVar()
        ttk.Label(cmd_rec_frm, textvariable=self.cmd1_display,
                foreground=gColors['Black'], font=('Arial', 12),
                borderwidth=0, padding=2, anchor=tk.W,
                ).pack(side=tk.RIGHT)
        ttk.Label(cmd_rec_frm, textvariable=self.cmd2_display,
                foreground=gColors['Gray'], font=('Arial', 12),
                borderwidth=0, padding=2, anchor=tk.E,
                ).pack(side=tk.LEFT)
# }}}

    def onSceneSelected(self, mode):# {{{
        fact = "(switch-scene room1 " + mode + ")"
        self.tcp.command('assertFact', fact)
        self.cmd2_display.set(self.cmd1_display.get())
        self.cmd1_display.set(fact)
# }}}

    def onVirtualModeSelected(self, index):# {{{
        self.tcp.command('setVirtualMode', str(index))
# }}}

if __name__ == "__main__":
    app = WindowGUI(880, 800)
