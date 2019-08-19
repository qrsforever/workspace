#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

user_info = {'name': ['letian', 'letian2'], 'password': '123'}
r = requests.post("http://127.0.0.1:8822/register", data=user_info)
 
print(r.text)
