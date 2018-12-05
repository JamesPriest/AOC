#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:51:43 2017

@author: james
"""
import numpy as np

commands = []

file = open("input.txt", "r")

commands = file.read().split('\n')[:-1]

commands = [ int(i) for i in commands ]

indexes = [ 0 for i in range(len(commands)) ]

indexes[10] = 1