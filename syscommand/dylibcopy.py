#!/usr/bin/python3

import os
import subprocess
import re

target_path: str = "/Users/lixiaoning/Program/desktopclient/bin/Joywok.app/Contents/Frameworks/VLCQtCore.framework/Versions/1.2.0/lib/vlc/plugins/"
original_path: str = "/usr/local/Frameworks/VLCQtCore.framework/Versions/1.2.0/lib/vlc/plugins/"


def copy_file():
    if not os.path.exists(target_path) or not os.path.exists(original_path):
        print("path not exists")
        return

    files_set = set()
    for root, dirs, files in os.walk(target_path):
        for file in files:
            files_set.add(file)

    tool_command = "otool -L %s%s"
    for file in files_set:
        ret_code, result = subprocess.getstatusoutput(tool_command % (target_path, 'liboggspots_plugin.dylib'))
        # print("processing lib %s" % file)
        link_list = re.findall('@rpath/(.+).dylib', result)
        for link in link_list:
            link = "%s.dylib" % link
            if link not in files_set and link != "libvlccore.dylib":
                print("link %s not in current set" % link)


copy_file()


# def signWithPath(path):
#     signCommand = "codesign --force --sign \"%s\" \"%s\"" % (DEVELOPER_ID, path)
#     retCode, result = subprocess.getstatusoutput(signCommand)
#     if retCode != 0:
#         print(result)
#         print("code sign failed")
#     return retCode
#
# def validateWithPath(path):
#     signCommand = "codesign --verify --deep --verbose=3 \"%s\"" % path
#     retCode, result = subprocess.getstatusoutput(signCommand)
#     if retCode == 0:
#         print("Accepted!")
#         return 0
#     else:
#         print(result)
#         print("Rejected!")
#         return -2
#
# def sign(apppath):
#     print("> signing frameworks & dylibs...")
#
#     if not os.path.exists(apppath):
#         print("where's your app?!")
#         return
#
#     frameworkDir = os.path.join(apppath, "Contents/")
#
#     # sign dylibs
#     for root, dirs, files in os.walk(frameworkDir):
#         for f in files:
#             if f.endswith(".dylib"):
#                 print("signing", f)
#                 dylibPath = os.path.join(root, f)
#                 signWithPath(dylibPath)
#
#     # sign frameworks
#     for root, dirs, files in os.walk(frameworkDir):
#         for d in dirs:
#             if d.endswith(".framework"):
#                 print("signing", d)
#                 if d.startswith("Qt"):
#                     frameworkPath = os.path.join(root, d, "Versions/5")
#                     signWithPath(frameworkPath)
#                 else:
#                     frameworkPath = os.path.join(root, d, "Versions/1.2.0")
#                     signWithPath(frameworkPath)
#
#     print("> singing app...")
#     print("singing", apppath)
#     signWithPath(apppath)
#
#     print("> validate code sign...")
#     if validateWithPath(apppath) == 0:
#         print("Code sign completed!")
#     else:
#         print("Dohhh!")
#
#
# if __name__ == '__main__':
