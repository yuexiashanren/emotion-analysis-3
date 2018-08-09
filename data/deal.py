#! /bin/env python
# -*- coding: utf-8 -*-

with open("n_pos.csv", "w",encoding='utf-8') as n:
    with open("pos.csv", "r",encoding='utf-8') as p:
        for line in p.readlines():
            if line == "\"\n":
                continue
            n.write(line)

line = "\""
print (len(line))