#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_document = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, document, count = line.split('\t',2)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word and current_document == document:
        current_count += count
    else:
        if current_word:
            print('{} ({},{})'.format(current_word,current_document,current_count))
        current_word = word
        current_count = count
        current_document = document


if current_word == word:
    print('{} ({},{})'.format(current_word,current_document,current_count))