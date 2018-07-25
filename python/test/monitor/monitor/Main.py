#!/usr/bin/python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from WindowGUI import WindowGUI

cf = ConfigParser()

cf.read('config.ini')

app = WindowGUI(880, 800,
        cf.get('HB', 'ServerAddress'),
        cf.get('HB', 'ServerPort'),
        cf.get('HB', 'LogUDPAddress'),
        cf.get('HB', 'LogUDPPort')
        )
