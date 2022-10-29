#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 18:58
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : unimodal_test_functions.py
# @Statement : Uni-modal test functions
import math
import random


def f1(x):
    # Dimension: 30
    # Range: [-100, 100]
    # Global minima: 0
    num = 0
    for i in range(len(x)):
        if not -100 <= x[i] <= 100:
            return 1e6
        num += x[i] ** 2
    return num


def f2(x):
    # Dimension: 30
    # Range: [-100, 100]
    # Global minima: 0
    num1 = 0
    num2 = 1
    for i in range(len(x)):
        if not -10 <= x[i] <= 10:
            return 1e6
        num1 += abs(x[i])
        num2 *= abs(x[i])
    return num1 + num2


def f3(x):
    # Dimension: 30
    # Range: [-100, 100]
    # Global minima: 0
    num1 = 0
    for i in range(len(x)):
        if not -100 <= x[i] <= 100:
            return 1e6
        num2 = 0
        for j in range(i):
            num2 += x[j]
        num1 += num2 ** 2
    return num1


def f4(x):
    # Dimension: 30
    # Range: [-100, 100]
    # Global minima: 0
    num = 0
    for i in range(len(x)):
        if not -100 <= x[i] <= 100:
            return 1e6
        if abs(x[i]) > num:
            num = abs(x[i])
    return num


def f5(x):
    # Dimension: 30
    # Range: [-30, 30]
    # Global minima: 0
    num = 0
    if not -30 <= x[-1] <= 30:
        return 1e6
    for i in range(len(x) - 1):
        if not -30 <= x[i] <= 30:
            return 1e6
        num += 100 * (x[i + 1] - x[i]) ** 2 + (x[i] - 1) ** 2
    return num


def f6(x):
    # Dimension: 30
    # Range: [-100, 100]
    # Global minima: 0
    num = 0
    for i in range(len(x)):
        if not -100 <= x[i] <= 100:
            return 1e6
        num += (x[i] + 0.5) ** 2
    return num


def f7(x):
    # Dimension: 30
    # Range: [-1.28, 1.28]
    # Global minima: 0
    num = 0
    for i in range(len(x)):
        if not -1.28 <= x[i] <= 1.28:
            return 1e6
        num += (i + 1) * x[i] ** 4 + random.random()
    return num
