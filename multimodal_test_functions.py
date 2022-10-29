#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 12:46
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : multimodal_test_functions.py
# @Statement : Multi-modal test functions
import math


def two_peak_trap(x):
    # Ref: Ackley D H. An empirical study of bit vector function optimization[J]. Genetic Algorithms and Simulated Annealing, 1987: 170-204.
    # Dimension: 1
    # Number of global peaks: 1
    # Range: [0, 20]
    if 0 <= x < 15:
        return 160 / 15 * (15 - x)
    elif 15 <= x <= 20:
        return 200 / 5 * (x - 15)
    else:
        return 1e6


def central_two_peak_trap(x):
    # Ref: Ackley D H. An empirical study of bit vector function optimization[J]. Genetic Algorithms and Simulated Annealing, 1987: 170-204.
    # Dimension: 1
    # Number of global peaks: 1
    # Range: [0, 20]
    if 0 <= x < 10:
        return 160 * x / 10
    elif 10 <= x < 15:
        return 160 * (15 - x) / 5
    elif 15 <= x <= 20:
        return 200 * (x - 15) / 5
    else:
        return 1e6


def equal_maxima(x):
    # Ref: Deb K. Genetic algorithms in multimodal function optimization[D]. Clearinghouse for Genetic Algorithms, Department of Engineering Mechanics, University of Alabama, 1989.
    # Dimension: 1
    # Number of global peaks: 5
    # Range: [0, 1]
    if 0 <= x <= 1:
        return math.sin(5 * math.pi * x) ** 6
    else:
        return 1e6


def uneven_maxima(x):
    # Ref: Deb K. Genetic algorithms in multimodal function optimization[D]. Clearinghouse for Genetic Algorithms, Department of Engineering Mechanics, University of Alabama, 1989.
    # Dimension: 1
    # Number of global peaks: 5
    # Range: [0, 1]
    if 0 <= x <= 1:
        return math.sin(5 * math.pi * (x ** (3 / 4) - 0.05)) ** 6
    else:
        return 1e6


def inverted_Shubert_function(x):
    # Ref: Li J P, Balazs M E, Parks G T, et al. A species conserving genetic algorithm for multimodal function optimization[J]. Evolutionary Computation, 2002, 10(3): 207-234.
    # Dimension: n
    # Number of global peaks: n \times 3^n
    # Range: [-10, 10]
    num = -1
    for i in range(x):
        if not -10 <= x[i] <= 10:
            return 1e6
        num1 = 0
        for j in range(5):
            num1 += j * math.cos((j + 1) * x[i] + j)
        num *= num1
    return num


def inverted_Vincent_function(x):
    # Ref: Shir O M, Bäck T. Niche radius adaptation in the cma-es niching algorithm[M]//Parallel Problem Solving from Nature-PPSN IX. Springer, Berlin, Heidelberg, 2006: 142-151.
    # Dimension: n
    # Number of global peaks: 6^n
    # Range: [0.25, 10]
    num = 0
    for i in range(len(x)):
        if not 0.25 <= x[i] <= 10:
            return 1e6
        num += math.sin(10 * math.log(x[i]))
    return num / len(x)


def inverted_Rastrigin_function(x):
    # Ref: Global optimization[M]. Berlin, Heidelberg: Springer Berlin Heidelberg, 1989.
    # Dimension: n
    # Number of global peaks: 1
    # Range: [-1.5, 1.5]
    num = 0
    for i in range(len(x)):
        if not -1.5 <= x[i] <= 1.5:
            return 1e6
        num += x[i] ** 2 + 10 * math.cos(2 * math.pi * x[i]) + 10
    return -num
