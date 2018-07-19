#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import socket
import time

class MonitorToolApp(tk.Frame):

    def __init__(self, width, height):
        self.connectted = False
        self.width = width
        self.height = height
        super(MonitorToolApp, self).__init__()
        self.master.protocol('WM_DELETE_WINDOW', self.onCloseWindow)
        self.master.title("MonitorTool")
        self.master.geometry(width+'x'+height)  
        self.master.resizable(width=True, height=True)

        self.server_addr = tk.StringVar()
        self.server_port = tk.StringVar()
        self.log = dict()

        self.server_addr.set('10.59.68.13')
        self.server_port.set('8192')

        self.connfrm = self.create_connect_setting()
        self.connfrm.pack(side=tk.TOP)
        #  self.create_widgets()

    def create_connect_setting(self):
        frm = tk.Frame(self.master)
        tk.Label(frm,
                text = '服务器地址: ',
                font = ('Arial', 16)
                ).grid(row=1, sticky=tk.W, pady=10)
        tk.Entry(frm, 
                textvariable=self.server_addr,
                font = ('Arial', 16)
                ).grid(row=1, column=1, sticky=tk.E)
        tk.Label(frm,
                text = '服务器端口: ',
                font = ('Arial', 16)
                ).grid(row=2, sticky=tk.W, pady=10)
        tk.Entry(frm, 
                textvariable=self.server_port,
                font = ('Arial', 16)
                ).grid(row=2, column=1, sticky=tk.E)
        tk.Button(frm,
                text = '连接',
                command = self.onConnect,
                font = ('Arial', 16)
                ).grid(row=3, column=1, columnspan=2, sticky=tk.E)

        return frm

    def create_widgets(self):
        self.setfrm = self.create_log_setting()
        self.setfrm.pack(anchor="w");
        pass

    def create_log_setting(self):
        #  self.srv_socket.send(b'getModulesName')
        #  result = self.srv_socket.recv(1024).decode('utf-8')
        #  print(result)
        result ='default;sqlite;rule-engine'
        names = result.split(';')

        frm = tk.Frame(self.master)
        tk.Label(frm, 
                text = '日志设置', 
                bg = 'YellowGreen',
                font = ('Arial', 20)
                ).grid(row=0, column=0, columnspan=6, sticky=tk.W)
        j = 1
        for t in ('模块名', 'Error', 'Warning', 'Normal', 'Info', 'Trace'):
            tk.Label(frm,
                    text = t,
                    pady = 10,
                    width = 10,
                    font = ('Arial', 16)
                    ).grid(row=1, column=j)
            j = j + 1

        i = 2
        for name in names:
            cmd = 'getModuleLogLevel;' + name
            self.srv_socket.send(cmd.encode())
            result = self.srv_socket.recv(8).decode('utf-8')
            self.log[name] = tk.IntVar()
            self.log[name].set(int(result))
            tk.Label(frm,
                    text = name,
                    pady = 10,
                    width = 10,
                    font = ('Arial', 16)
                    ).grid(row=i, column=1)
            for j in range(1, 6):
                tk.Radiobutton(frm,
                        variable = self.log[name],
                        value = j,
                        command = lambda n = name : self.onLogButton(n)
                        ).grid(row=i, column=j+1)
            i = i + 1

        return frm

    def onLogButton(self, name):
        print("name ---> " + name)
        pass

    def onCloseWindow(self):
        print("close windown")
        if self.connectted:
            self.srv_socket.send(b'quit')
            time.sleep(1)
            self.srv_socket.close()
        self.master.destroy()
        pass

    def onConnect(self):
        addr = self.server_addr.get()
        port = self.server_port.get()
        print("addr = ", addr, " port = ", port)
        self.srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srv_socket.connect((addr, int(port))) 
        result = self.srv_socket.recv(8).decode('utf-8')
        if result == 'success':
            print("connect success")
            self.connectted = True
            self.connfrm.destroy()
            self.create_widgets()

def main():
    app = MonitorToolApp('780', '880')
    app.mainloop()

if __name__ == "__main__":
    main()
