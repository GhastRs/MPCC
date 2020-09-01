import math

MPCC = '''
========[ MCDR ] §bPearl§r §6Cannon§r §cCalculator§r========
MCDR Pearl Cannon Calculator v1.2

§b!!MPCC§r 显示这条信息
§b!!MPCC calculate§r来进行计算
目前有§d平射§r(0~10度角,填写1)和§d抛射§r(15~45度角,填写2)

使用方法:
§b!!MPCC§r §6calculate§r [< 模式 >] [< 珍珠初速度(推荐Carpet) >]
[< 珍珠与TNT角度(视情况而定,平射模式不填) >]
例如:
平射: §b!!MPCC§r §6calculate§r §c1§r 320
抛射: §b!!MPCC§r §6calculate§r §c2§r 320 16

各项数据越精确, 结果越精确
对于填写错误,作者对错误结果§c概不负责§r
有Bug请§d在Bilibili私信GhastRs§r,会在v1.3更新
================================
'''

def work(server, info):
	if info.is_player == 1:
		if info.content.startswith('!!MPCC'):
			if info.content.startswith('!!MPCC calculate'):
				if info.content.startswith('!!MPCC calculate 1'):
					PearlSpeed1 = math.ceil(float(info.content.split()[3]))
					FinalValue1 = str(PearlSpeed1 * 100)
					server.say('[ MPCC ] 计算结果 : ' + FinalValue1)
				elif info.content.startswith('!!MPCC calculate 2'):
					PearlSpeed2 = math.ceil(int(info.content.split()[3]))
					Angle = math.ceil(float(info.content.split()[4]))
					FinalValue2 = str(PearlSpeed2 * 100 * ( Angle + 100 ) / 100)
					server.say('[ MPCC ] 计算结果 : ' + FinalValue2)
				else:
					server.say('填写错误,请认真阅读帮助信息,谢谢~')
			else:
				server.say(MPCC)

def on_info(server, info):
	if info.is_player :
		work(server, info)