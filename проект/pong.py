from pygame import *
from random import *
from time import sleep
window=display.set_mode((700,500))
display.set_caption("понг")

background =transform.scale(image.load("background.png"),(700,500))
window.blit(background,(0,0))
game=True

clock=time.Clock()

x1=0
x2=600
y1=100
y2=200

right=True


class GameSprite_player(sprite.Sprite):
    def __init__(self, image_1, xx, yy, speed_,size_y):
        super().__init__()
        self.image=transform.scale(image.load(image_1),(20,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy
        self.speed=speed_
    def move1(self):
        global keys_pressed    
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>1:
            self.rect.y-=7
        if keys_pressed[K_s] and self.rect.y<400:
            self.rect.y+=7
    def move2(self):
        if keys_pressed[K_UP] and self.rect.y>1:
            self.rect.y-=7
        if keys_pressed[K_DOWN] and y1<400:
            self.rect.y+=7

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, image_1, xx, yy, speed_):
        super().__init__()
        self.image=transform.scale(image.load(image_1),(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy
        self.speed=speed_

    def move_right(self,movement_speed,x_spd):    
        self.rect.x+=x_spd
        self.rect.y+=movement_speed

    def game_reset(self):
        self.rect.x=400

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

size_y_1=120
size_y_2=120

ball1=GameSprite("мяч.png",400,200,5)
sprite1=GameSprite_player("sprite1.png",0,100,5,size_y_1)
sprite2=GameSprite_player("sprite2.png",680,100,5,size_y_2)

speeed=5
x_speed=5

font.init()
font=font.SysFont("Arial",40)

left_score=0
right_score=0


while game:
    window.blit(background,(0,0))
    sprite1.reset()
    sprite1.move1()
    sprite2.reset()
    sprite2.move2()
    ball1.reset()
    keys_pressed=key.get_pressed()

    miss_counter=font.render("Player1: "+str(left_score), True, (50,50,50))
    window.blit(miss_counter,(10,0))

    score_counter=font.render("Player2: "+str(right_score), True, (50,50,50))
    window.blit((score_counter),(550,0))

    win_2=font.render("player 2 wins! ", True, (255,255,255))
    win_1=font.render("player 1 wins! ", True, (255,255,255))

    if ball1.rect.y>=400 and speeed>=0:
        speeed=speeed*(-1)
    if ball1.rect.y<=0 and speeed<=0:
        speeed=speeed*(-1)
    ball1.move_right(speeed,x_speed)

    if sprite.collide_rect(ball1,sprite1):
        if x_speed>0:
            x_speed+=2
        if x_speed<0:
            x_speed-=2
        x_speed=x_speed*(-1)
    if sprite.collide_rect(ball1,sprite2):
        if x_speed>0:
            x_speed+=2
        if x_speed<0:
            x_speed-=2
        x_speed=x_speed*(-1)

    if ball1.rect.x>=1000:
        left_score+=1
        ball1.game_reset()
        x_speed=-5
        speeed=-5
    if ball1.rect.x<=-1000:
        right_score+=1
        ball1.game_reset()
        x_speed=5
        speeed=5
    if left_score>=5:
        window.blit((win_1),(250,230))
    if right_score>=5:
        window.blit((win_2),(250,230))

    for e in event.get():
        if e.type==QUIT:
            game=False
    clock.tick(75)
    display.update()