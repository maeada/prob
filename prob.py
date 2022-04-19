## Class: https://docs.python.org/3/tutorial/classes.html
## https://www.programiz.com/python-programming/class
## dict.get(): https://www.tutorialspoint.com/python/dictionary_get.htm

import bisect
import copy
import logging
import math
import random
import re

from collections import Counter
from operator import itemgetter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def odds(p):
    """Computes odds for a given probability.

        Example: p=0.75 means 75 for and 25 against, or 3:1 odds in favor.

        Note: when p=1, the formula for odds divides by zero, which is
        normally undefined.  But I think it is reasonable to define Odds(1)
        to be infinity, so that's what this function does.

        p: float 0-1

        Returns: float odds
        """
    if p==1:
        return float('inf')
    return p / (1-p)

def dice(num):
    """
    :param num: number of throw dice
    :return: Frequency of each outcome. (dictionary)
    """

    ls = []  # generate list
    for i in range(num):
        x = random.randint(1, 6)
        ls.append(x)  ## keep outcome in list
    # print(ls)

    ## Keep outcome and frequecy of outcome in dictionary
    ## dic.get(k, 0) หมายความว่า ถ้ามันเจอค่า key='k' มันจะreturn valueให้  ถ้าไม่เจอ มันจะreturn 0
    dic = {}  # generate dictionary
    for k in ls:
        dic[k] = dic.get(k, 0) + 1  # นับจำนวน outcome ที่ได้ในแต่ละตัว โดยเริ่มต้นที่0 และบวไปทีละ1
    return dic

# class _DictWrapper(object):
#     """An object that contains a dictionary."""

if __name__ == '__main__':
    # x = random.randint(1, 6)
    # n = 10
    # ls = [] # generate list
    # for i in range(10):
    #     x = random.randint(1, 6)
    #     ls.append(x) ## keep outcome in list
    # print(ls)
    #
    # dic = {} # generate dic
    # for k in ls:
    #     dic[k] = dic.get(k, 0) + 1 # นับจำนวน outcome ที่ได้ในแต่ละตัว โดยเริ่มต้นที่0 และบวไปทีละ1
    # print(dic)
    x  = dice(100)
    print(x)
    print(x[1] + x[2])
    # for i in range(len(x)):
    #     print(x[i])

    print(len(x))
    print(sorted(x.keys()))

    # sum = 0
    # for i in sorted(x.keys()):
    #     print(x[i])
    #     sum = sum + x[i]
    # print(sum)
    print(sum(x.values()))
    print(x.values())
    # x.update((8, 5))
    # print(x)
    # print(help(x.update()))
    # print(help(random))