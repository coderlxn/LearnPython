#!/usr/bin/env python
# coding=utf-8

def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)

