# -*- coding:utf-8 -*-
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式r只读 w只写 w+读写 a+不删除原来内容写入文件
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
file = open('test.txt', mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 输出文件内容
print(file.read())
# 写入txt
file.write('aa'+'\n')
# 关闭txt
file.close()