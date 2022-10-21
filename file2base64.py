#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import os, os.path

#文件编码成base64字符串并存入目标文件
#注意:不会删除原文件
def encode_file(src, dest):
    if os.path.isfile(src):
        with open(src, 'rb') as f:
            file = base64.b64encode(f.read())
        with open(dest, 'wb') as f:
            f.write(file)
        return True
    return False

#base64字符串文件解码成原文件
#不会删除原文件
def decode_file(src, dest):
    if os.path.isfile(src):
        with open(src, 'rb') as f:
            file = f.read()
        with open(dest, 'wb') as f:
            f.write(base64.b64decode(file))
        return True
    return False
        
#file2base(SRC, BASE)
#base2file(BASE, DEST)
