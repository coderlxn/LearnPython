# -*- coding: utf-8 -*-
# @Time    : 9/28/18 5:18 PM
# @Author  : Jax.Li
# @FileName: loader.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import os
from importlib import abc
import importlib
import glob
import hashlib


class Loader(object):
    """
    根据指定模块名，到plugins目录下查找文件并导入
    """

    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def find_plugins(self):
        """变量目录，查找plugin"""

        plugins = []
        items = os.listdir(self.plugin_dir)
        for item in items:
            location = os.path.join(self.plugin_dir, item)

            finder = abc.MetaPathFinder()
            if os.path.isdir(location) and '__init__.py' in os.listdir(location):
                info = finder.find_module('__init__', [location])
            elif os.path.isfile(location) and item.endswith('.py'):
                info = finder.find_module(os.path.splitext(item)[0], [self.plugin_dir])
            else:
                continue

            print('find plugin: %s' % item)
            plugins.append({'name': os.path.splitext(item)[0], 'info': info, 'md5': self.compute_md5(location)})

        return plugins

    def load_plugins(self):
        for plugin in self.find_plugins():
            module = {}
            module['module'] = abc.FileLoader.load_module(plugin['name'], *plugin['info'])
            module['md5'] = plugin['md5']
            self.plugins[plugin['name']] = module

        return self.plugins

    def find_plugin(self, module_name):
        location = os.path.join(self.plugin_dir, module_name)

        finder = abc.MetaPathFinder()
        if os.path.isdir(location) and '__init__.py' in os.listdir(location):
            info = finder.find_module('__init__', [location])
            md5 = self.compute_md5(location)
        elif os.path.isfile(location + ".py"):
            info = finder.find_module(module_name, [self.plugin_dir])
            md5 = self.compute_md5(location + '.py')
        else:
            return False, 'no such module: %s' % module_name
        plugin = {'name': module_name, 'info': info, 'md5': md5}

        return True, plugin

    def load_plugin(self, module_name):
        ok, plugin = self.find_plugin(module_name)
        if not ok:
            return ok, plugin

        if plugin['name'] not in self.plugins:
            print('add plugin: %s' % plugin['name'])
            self.plugins[plugin['name']] = {}
            self.plugins[plugin['name']]['module'] = abc.FileLoader.load_module(plugin['info'])
            self.plugins[plugin['name']]['md5'] = plugin['md5']
        elif plugin['name'] in self.plugins and plugin['md5'] != self.plugins[plugin['name']]['md5']:
            print('update plugin: %s' % plugin['name'])
            self.plugins[plugin['name']]['module'] = abc.FileLoader.load_module(plugin['info'])
            self.plugins[plugin['name']]['md5'] = plugin['md5']

        return True, self.plugins[plugin['name']]['module']

    @staticmethod
    def compute_md5(entry):
        md5 = hashlib.md5()

        if os.path.isfile(entry):
            md5.update(open(entry, 'rb').read())
        elif os.path.isdir(entry):
            for path, dir_list, file_list in os.walk(entry):
                for file in file_list:
                    if glob.fnmatch.fnmatch(file, '*.py'):
                        md5.update(open(os.path.join(path, file), 'rb').read())
        return md5.hexdigest()
