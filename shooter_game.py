from pygame import *
from random import *
from time import time as tm

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

left_pl = Player('dog.png',0,225,5,60,50)
right_pl = Player('dog.png',640,225,5,60,50)











window = display.set_mode((700,500))
display.set_caption('Ping pong')
#задай фон сцены
background = transform.scale(image.load('galaxy.jpg'),(700,500))
window.blit(background,(0,0))
#создай 2 спрайта и размести их на сцене
game = True
finish = False
clock = time.Clock()
FPS = 60
# peashooter = Player('peashooter.png',100,400,10,50,50)
font.init()
font1 = font.SysFont('Arial',70)
win = font1.render('YOU WIN',True,(255,215,0))
lose = font1.render('YOU LOSE',True,(255,10,10))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
                    

            
                
    if finish != True:
        window.blit(background,(0,0))
        left_pl.reset()
        right_pl.reset()
        left_pl.update_l()
        right_pl.update_r()
        

        
        

    display.update()
    clock.tick(FPS)
