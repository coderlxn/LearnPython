#!/usr/bin/env python
# coding=utf-8

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import coverage
    coverage.process_startup()
except ImportError:
    pass


def generate_test_suit():
    current_pwd = os.path.dirname(__file__)
    testcase_directory = current_pwd + os.sep + 'testcase'
    return unittest.defaultTestLoader.discover(testcase_directory)


if __name__ == '__main__':
    suite = generate_test_suit()
    unittest.TextTestRunner().run(suite)
