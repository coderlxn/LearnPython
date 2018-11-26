# -*- coding: utf-8 -*-
# @Time    : 10/31/18 3:54 PM
# @Author  : Jax.Li
# @FileName: wordappear.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import sys
import re

WORD_RE = re.compile(r"\w+")

index = {}
with open("/Users/lixiaoning/Program/Python/LearnPython/UNIT/aifunctions.py", encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # 这其实是一种很不好的实现，这样写只是为了证明论点
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences

            # 使用setdefault可以快速的完成查询和插入
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
