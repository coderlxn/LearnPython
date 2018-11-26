# -*- coding: utf-8 -*-
# @Time    : 11/20/18 11:34 AM
# @Author  : Jax.Li
# @FileName: unittestpatch.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from moduledemo.printurl import url_print


class TestURLPRINT(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}/{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            url_print(protocol, host, domain)
            self.assertEqual(expected_url, 'abc')
