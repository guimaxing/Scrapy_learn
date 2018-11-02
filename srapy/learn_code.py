# encoding: utf-8
'''
@Software: PyCharm
@author: MoCheng
@file: learn_code.py
@time: 2018/11/3 0003 2:45
@desc:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

import config
# from config import url


print(url)
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon/")
# bsobj = BeautifulSoup(html)
# for link in bsobj.findAll("a"):
#     if 'href'  in link.attrs:
#         print(link.attrs['href'])