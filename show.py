import matplotlib.pyplot as plt
import serial
import random
def sl():
	ser = serial.Serial("COM3", 115200 )
	return [int(str(ser.readline())[4:-3])]
ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据

bx = []                    # 定义一个 x 轴的空列表用来接收动态的数据
by = []                    # 定义一个 y 轴的空列表用来接收动态的数据

plt.ion()                  # 开启一个画图的窗口
for i in range(11):

	ax.append(0.1*i)           # 添加 i 到 x 轴的数据中
	ay.append(random.randint(0,10000))

	bx.append(0.1*i)           # 添加 i 到 x 轴的数据中
	by.append(random.randint(0,10000))

	plt.clf()              # 清除之前画的图
	plt.plot(ax,ay,c='c',ls='-',marker='.',mec='b')        # 画出当前 ax 列表和 ay 列表中的值的图形
	plt.plot(bx, by, c='r', ls='-',marker='.', mec='b')
	plt.pause(0.1)         # 暂停0.1秒
	plt.ion()
	plt.ioff()
plt.pause(0)
