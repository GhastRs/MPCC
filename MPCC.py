# -*- coding: utf-8 -*-
import math

#插件源码太烂了 别骂了别骂了孩子要傻了

'''
MC一般指令染色规则
找不到 报错 数值后缀(L/b/d/f) : §c, 红色
坐标 数值 字符串 : §a, 浅绿色
数据 : §6, 金色
括号 玩家 物品或结构名称 : §f, 白色
属性名称 : §b, 水蓝色
'''

MPCC = '''
========[ MCDR ] §bPearl§r §6Cannon§r §cCalculator§r========
MCDR Pearl Cannon Calculator §av2.1§r
现在大多数生电服都装了珍珠炮, 于是我写了这个插件辅助计算~
目前支持FTL-L和FTL-H型珍珠炮

§b!!MPCC§r 显示帮助信息
§6!!MPCC §ccal§r 进行计算

使用举例:
自动获取: §b!!MPCC§r §6cal§r §cal§r
手动输入: §b!!MPCC§r §6cal§r §cts§r 480 2 480 
此处数据分别为珍珠XYZ初速度, 手动输入请填写数据,
自动获取输入cal al即可(照搬示例)

珍珠Y轴速度过大是珍珠炮问题, 没珍珠炮偏向加速Y轴向天上打的.
有Bug或有好想法请在B站私信§dGhastRs§r, 会在v2.2更新
也可以在Github [ MPCC ]的Issue提交(最快查看)

挖个新坑: §b!!MPCC dl§r 模拟TNT在中央起爆起全程珍珠动量, 并计算落地坐标
========================================
'''

def work(server, info, message, text, command):
	if info.content.startswith('!!MPCC'): #判定开始
		if info.content.startswith('!!MPCC cal'): #计算模式
			if info.content.startswith('!!MPCC cal al'): #Auto-Log模式

				X1 = 
				Y1 = 
				Z1 = 
				if X1 >= Z1:
					FinalValue1 = str(X1 * 100)
				else:
					FinalValue2 = str(Z1 * 101)
			elif info.content.startswith('!!MPCC cal ts'): #手动输入模式
				X2 = math.ceil(float(info.content.split()[6]))
				Y2 = math.ceil(float(info.content.split()[7]))
				Z2 = math.ceil(float(info.content.split()[8]))
				if X2 >= Z2:
					FinalValue1 = str(X2 * 100)
				else:
					FinalValue2 = str(Z2 * 101)
			else: #输入错误
				server.say('填写错误, 请阅读帮助信息, 谢谢~')
		elif info.content.startswith('!!MPCC dl'): #模拟模式


		else:
			server.say(MPCC) #帮助信息

def on_load(server, old):
	server.add_help_message('!!MPCC', '珍珠炮计算插件') #添加MCDR!!help内的帮助信息
