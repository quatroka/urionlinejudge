#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = input().split()
if int(N[0]) == int(N[1]):
    print(N[0])
elif int(N[0]) > int(N[1]):
    print(N[0])
else:
    print(N[1])
