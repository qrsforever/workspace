#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk


# Demo just soso
class App:
    def __init__(self, master):
        fm1 = tk.Frame(master)
        tk.Button(fm1, text='Top').pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=tk.YES)
        tk.Button(fm1, text='Center').pac?!?jedi=0, k(side=tk.TOP, ancho?!? (cnf={}, *_***kw*_*) ?!?jedi?!?r=tk.W, fill=tk.X, expand=tk.YES)
        tk.Button(fm1, text='Bottom').pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=tk.YES)

        #  tk.Button(fm1, text='Top').pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
        #  tk.Button(fm1, text='Center').pack(side=tk.TOP, anchor=tk.W, fill=tk.X)
        #  tk.Button(fm1, text='Bottom').pack(side=tk.TOP, anchor=tk.W, fill=tk.X)

        #  tk.Button(fm1, text='Top').pack(anchor=tk.W, fill=tk.X, expand=tk.YES)
        #  tk.Button(fm1, text='Center').pack(anchor=tk.W, fill=tk.X, expand=tk.YES)
        #  tk.Button(fm1, text='Bottom').pack(anchor=tk.W, fill=tk.X, expand=tk.YES)

        #  fm1.pack(fill=tk.BOTH, expand=tk.YES) #  错误
        fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        fm2 = tk.Frame(master)
        tk.Button(fm2, text='Left').pack(side=tk.LEFT)
        tk.Button(fm2, text='This is the Center button').pack(side=tk.LEFT)
        tk.Button(fm2, text='Right').pack(side=tk.LEFT)
        fm2.pack(side=tk.LEFT, padx=10)

root = tk.Tk()
root.title("Pack - Example")
display = App(root)
root.mainloop()
