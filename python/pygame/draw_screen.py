import pygame,sys
from pygame.locals import *	#导入pygame的所有常量
pygame.init()	#初始化pygame

screen = pygame.display.set_mode((600,500))	#创建分辨率为600*500大小的屏幕
myfont = pygame.font.Font(None,60)	#创建文字对象
white = 255,255,255		#创建颜色变量
blue = 0,0,255
textImage = myfont.render("Hello pygame",True,white)	#将文字对象渲染到图像上

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	screen.fill(blue)
	screen.blit(textImage,(100,100))
	pygame.display.update()