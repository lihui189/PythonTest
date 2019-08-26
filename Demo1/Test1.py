# 导入pygame库
import pygame
import sys
# pygame初始化
pygame.init()
# 设置窗口大小
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
# 设置程序的名字
pygame.display.set_caption('第一个游戏小程序')
#设置背景颜色
bg=(100,111,250)
#加载图片
img = pygame.image.load('Peashooter.gif')
#获取图片矩形
position = img.get_rect()
#定义一个速度变量
speed = [1,0]
# 让窗口一直循环
while True:
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     print ('关闭了')
     sys.exit()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_UP:
           speed = [0,-1]
           print("UP")
       if event.key ==pygame.K_DOWN:
           speed = [0,1]
           print("xia")
       if event.key == pygame.K_LEFT:
           speed = [-1,0]
           print("left")
       if event.key == pygame.K_RIGHT:
           speed = [1,0]
           print("right")
 #填充背景
 screen.fill(bg)
 #循环移动
 position = position.move(speed)
 #更新图片
 screen.blit(img,position)
 #更新界面
 pygame.display.flip()
 #时钟
 pygame.time.Clock().tick(60)
