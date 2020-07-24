# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import serial
import time
import random
# def sl():
# 	ser = serial.Serial("COM3", 115200 )
# 	return [int(str(ser.readline())[4:-3])]
ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据

bx = []                    # 定义一个 x 轴的空列表用来接收动态的数据
by = []                    # 定义一个 y 轴的空列表用来接收动态的数据

plt.ion()                  # 开启一个画图的窗口
for i in range(300):

	ax.append(time.strftime('%M:%S',time.localtime(time.time())))           # 添加 i 到 x 轴的数据中
	ay.append(random.randint(0,10000))

	bx.append(time.strftime('%M:%S',time.localtime(time.time())))           # 添加 i 到 x 轴的数据中
	by.append(random.randint(0,10000))
	plt.clf()              # 清除之前画的图
	plt.plot(ax,ay,c='c',ls='-',marker='.',mec='b')        # 画出当前 ax 列表和 ay 列表中的值的图形
	plt.plot(bx, by, c='r', ls='-',marker='.', mec='b')
	plt.pause(0.05)         # 暂停一秒
	plt.ion()
	plt.ioff()
plt.pause(0)
