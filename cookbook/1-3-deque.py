# -*- coding: utf-8 -*-
# @Time    : 10/9/18 5:08 PM
# @Author  : Jax.Li
# @FileName: 1-3-deque.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open("somefile.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-" * 20)
