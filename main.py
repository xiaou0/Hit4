print("Debug")

import pygame #pygame for game development
from pygame.locals import *

pygame.init() #初始化

font=pygame.font.SysFont('Arial Black',24)

gridsize=5 #max 10
GOAL=4 #目标点数

size=(gridsize*50,gridsize*50+50)

screen=pygame.display.set_mode(size)
grid=pygame.image.load("grid.png").convert_alpha()
grid1=pygame.image.load("grid1.png").convert_alpha()
grid2=pygame.image.load("grid2.png").convert_alpha()
grid3=pygame.image.load("grid3.png").convert_alpha()
fgrid=pygame.image.load("grid_black.png").convert_alpha()

board=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

own=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

score=[0,0]

color=[(0,0,0),(255,0,0),(0,0,255)]
p=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def outOfRange(X,Y):
    return (X>=gridsize or X<0 or Y>=gridsize or Y<0)
def isEmptyNeighbor(X,Y):
    for i in range(0,4): #遍历四个方向
        nx=X+dx[i]
        ny=Y+dy[i]
        if outOfRange(nx,ny):
            continue
        if board[ny][nx]!=0 and board[ny][nx]!=GOAL:
            return False
    return True

done=False
while not done:
    for event in pygame.event.get():#事件列表
        if event.type==pygame.QUIT:#退出事件
            done=True
        if event.type==MOUSEBUTTONDOWN:
            x=int(event.pos[0]/50)
            y=int(event.pos[1]/50)
            if outOfRange(x,y):
                continue
            if event.button==1:
                if board[y][x]==GOAL:
                    continue
                print("DEBUG: LCLICK")
                print(p)
                board[y][x]+=1
                if board[y][x]!=GOAL:
                    board[y][x]%=GOAL
                if board[y][x]==GOAL:
                    own[y][x]=1+p
                    score[p]+=1
                p=1-p
            if event.button==3:
                if isEmptyNeighbor(x,y):
                    continue
                if board[y][x]==GOAL:
                    continue
                print("DEBUG: RCLICK")
                print(p)
                for i in range(0,4): #遍历四个方向
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if outOfRange(nx,ny):
                        continue
                    if board[ny][nx]!=GOAL:
                        board[y][x]+=board[ny][nx]
                for i in range(0,4): #遍历四个方向
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if outOfRange(nx,ny):
                        continue
                    if board[ny][nx]!=GOAL:
                        board[ny][nx]=0
                if board[y][x]!=GOAL:
                    board[y][x]%=GOAL
                if board[y][x]==GOAL:
                    own[y][x]=1+p
                    score[p]+=1
                p=1-p
    screen.fill(color[0])
    for i in range(0,gridsize):
        for j in range(0,gridsize):
            if board[i][j]==GOAL:
                screen.blit(fgrid,(j*50,i*50))
            elif board[i][j]==1:
                screen.blit(grid1,(j*50,i*50))
            elif board[i][j]==2:
                screen.blit(grid2,(j*50,i*50))
            elif board[i][j]==3:
                screen.blit(grid3,(j*50,i*50))
            else:
                screen.blit(grid,(j*50,i*50))
            numshow=font.render(str(board[i][j]),True,color[own[i][j]])
            screen.blit(numshow,(j*50+(
                (50-numshow.get_width())/2
            ),i*50+(
                (50-numshow.get_height())/2
            )))#每格居中
    RedScore=font.render(str(score[0]),True,color[1])
    Cmp=font.render(":",True,(255,255,255))
    Wcmp=Cmp.get_width()
    BlueScore=font.render(str(score[1]),True,color[2])
    
    screen.blit(Cmp,(50*gridsize/2-Wcmp/2+25,50*gridsize+10))
    screen.blit(RedScore,(50*gridsize/2-Wcmp/2-RedScore.get_width()+25,50*gridsize+10))
    screen.blit(BlueScore,(50*gridsize/2+Wcmp/2+25,50*gridsize+10))
    
    pygame.draw.rect(screen,color[p+1],(0,50*gridsize,50,50))
    pygame.display.update()
    
    if score[0]+score[1]>=gridsize**2:
        done=True

done=False
while not done:
    for event in pygame.event.get():
        if event.type==QUIT:
            dont=True()
    if score[0]>score[1]:
        screen.fill(color[1])
    elif score[1]>score[0]:
        screen.fill(color[2])
    pygame.display.update()