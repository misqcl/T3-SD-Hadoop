#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re
documento = None

for line in sys.stdin:
    line = line.strip()

    if documento is None and line:
        documento=line.split()[0]

    docs = line.lower()
    arr = []
    for char in [",",".",'"',"'","(",")","\\",";",":","$1","$","&"]:
        docs = docs.replace(char, '')

    line = re.sub(r'\W+',' ',line.strip())
    words = line.split()

    for word in words:
        arr.append('{}\t{}\t{}'.format(word,documento,1))

    for i in sorted(arr):
        print(i)