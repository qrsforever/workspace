#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from res import Strings
from res import Styles

gStrings = Strings.strings
gStyles = Styles.styles

class WindowGUI(object):

    """Docstring for WindowGUI. """

    def __init__(self, width, height):
        """ """
        self.width = width
        self.height = height
        self.win = tk.Tk()
        self.win.protocol('WM_DELETE_WINDOW', self.onCloseWindow)
        self.win.resizable(width=True, height=True)
        self.onConfigure()
        self.lan = 'en'
        self.onInitWindow()
        self.win.mainloop()

    def onConfigure(self):
        style = ttk.Style()
        style.theme_create('app', parent="alt", settings=gStyles['app'])
        style.theme_use('app')


    def onInitWindow(self):
        # set window size and title
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
                self.width, self.height,
                (screenwidth - self.width) / 2,
                (screenheight - self.height) / 2)
        self.win.geometry(alignstr)
        self.win.title(gStrings['title'][self.lan])

        # set menu
        self.menu_bar = tk.Menu(self.win)
        menu_set = tk.Menu(self.menu_bar)
        menu_set.add_command(
                label=gStrings['lanSwitch'][self.lan],
                command=self.switchLang)
        self.menu_bar.add_cascade(label=gStrings['set'][self.lan], menu=menu_set)

        self.menu_bar.add_command(
                label=gStrings['about'][self.lan],
                state=tk.DISABLED,
                command=self.showAbout)
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
        
    def switchLang(self):
        if self.lan == 'en' :
            self.lan = 'cn'
        else:
            self.lan = 'en'
        self.menu_bar.destroy()
        self.tabControl.destroy()
        self.onInitWindow()

    def showAbout(self):
        pass
            
    def onCloseWindow(self):
        self.win.destroy()

    def createBasicInfoView(self, tab):
        pass

    def createLogSetView(self, tab):
        # level frame
        level_frm = ttk.Frame(tab)
        ttk.Label(level_frm,
                text = gStrings['loglevel'][self.lan],
                font = ('Arial', 20)
                ).grid(row=0, column=0, columnspan=6, sticky=tk.W)
        level_frm.pack(anchor="w")


        # j = 1
        # for t in ('模块名', 'Error', 'Warning', 'Normal', 'Info', 'Trace'):
        #     tk.Label(frm,
        #             text = t,
        #             pady = 10,
        #             width = 10,
        #             font = ('Arial', 16)
        #             ).grid(row=1, column=j)
        #     j = j + 1

        # i = 2
        # for name in names:
        #     cmd = 'getModuleLogLevel;' + name
        #     self.srv_socket.send(cmd.encode())
        #     result = self.srv_socket.recv(8).decode('utf-8')
        #     self.log[name] = tk.IntVar()
        #     self.log[name].set(int(result))
        #     tk.Label(frm,
        #             text = name,
        #             pady = 10,
        #             width = 10,
        #             font = ('Arial', 16)
        #             ).grid(row=i, column=1)
        #     for j in range(1, 6):
        #         tk.Radiobutton(frm,
        #                 variable = self.log[name],
        #                 value = j,
        #                 command = lambda n = name : self.onLogButton(n)
        #                 ).grid(row=i, column=j+1)
        #     i = i + 1

        # return frm
        pass

    def createDevControlView(self, tab):
        pass

if __name__ == "__main__":
    app = WindowGUI(800, 800)
