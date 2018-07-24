#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
 
win=tkinter.Tk()
 
mylist=tkinter.Listbox(win,width=100)
mylist.pack()
 
for  item  in ["1","asdsa","asdsadsa","asdsadsad"]:
    mylist.insert(tkinter.END,item)
 
win.mainloop()
