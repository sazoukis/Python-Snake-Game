import pygame as pg
import sys
import time
from random import randint
class Snake:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,key_presse,x):
            if key_presse == "left" or key_presse == "right":
                self.x+=x           #axe x move
            if key_presse == "up" or key_presse=="down":
                self.y+=x           #axe y move
    def foodeat(self,food):
        return (self.x==food.x and self.y==food.y)
class Food:
    def __init__(self):
        self.x=randint(0,70)*10
        self.y=randint(0,50)*10
    def update(self):
        self.x=randint(0,70)*10
        self.y=randint(0,50)*10
def draw(snakelist):
    for i in snakelist:
        pg.draw.rect(gameDsiplay, black, [i[0], i[1], 10, 10])
food=Food()
white=[255,255,255]
black=[0,0,0]
red=[255,0,0]
pg.init()                           # always initial pygame
pg.font.init()                      # initial pygame font
clock=pg.time.Clock()               # initial clock to sleep
pg.event.pump()
exitgame=False
gameDsiplay=pg.display.set_mode((800,600)) # create display size for the game
pg.display.set_caption("sazouki snake")
snake=Snake(300,300)
key_pressed=""
x=int
scr=0
snakeList = []
def msg(scr,text):
    losetext = font.render(text+"you loose your score is %d" % scr, 1, red)
    gameDsiplay.blit(losetext, (200, 300))
    pg.display.update()
    time.sleep(1)
    exitgame = True
    pg.quit()
    sys.exit(0)
right=False
left=False
up=False
down=False
while not exitgame:
    gameDsiplay.fill(white)
    pg.draw.rect(gameDsiplay,red,[food.x,food.y,10,10])
    font=pg.font.Font(None,30)
    scoretext=font.render("score: "+str(scr),1,black)
    gameDsiplay.blit(scoretext, (700,20))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exitgame=True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and not right:
                key_pressed="left"
                x=-10
                left=True
                up=False
                down=False
            if event.key == pg.K_RIGHT and not left:
                key_pressed = "right"
                x = 10
                right=True
                up=False
                down=False
            if event.key == pg.K_DOWN and not up:
                key_pressed = "down"
                x = 10
                down=True
                left=False
                right=False
            if event.key == pg.K_UP and not down:
                key_pressed = "up"
                x = -10
                up=True
                left=False
                right=False
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit(0)
    snake.move(key_pressed,x)
    snakeHead = []
    snakeHead.append(snake.x)
    snakeHead.append(snake.y)
    snakeList.append(snakeHead)
    draw(snakeList)
    if len(snakeList) > scr:
        del snakeList[0]
    clock.tick(15)
    #print(snakeList)
    if snake.foodeat(food):
        scr+=1
        food.update()
    pg.display.update()
    for i in snakeList[:-1]:
        if snakeHead == i:
            text="Tail collision "
            msg(scr,text)
    if snake.x>=810 or snake.y>=610 or snake.x<=-10 or snake.y<=-10:
        text="you hit the border "
        msg(scr,text)
