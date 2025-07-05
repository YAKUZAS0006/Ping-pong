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
ball = GameSprite('pea.png',321,203,3,30,30)

speed_x = 3
speed_y = 3









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
win_l = font1.render('WIN LEFT PLAYER',True,(255,215,0))
win_r = font1.render('WIN RIGHT PLAYER',True,(255,215,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
                    

            
                
    if finish != True:
        window.blit(background,(0,0))
        left_pl.reset()
        right_pl.reset()
        ball.reset()
        left_pl.update_l()
        right_pl.update_r()
        if ball.rect.y >= 470:
            speed_y *= -1
        if ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(left_pl,ball) or sprite.collide_rect(right_pl,ball):
            speed_x *= -1
        if ball.rect.x >= 670:
            window.blit(win_l,(100,200))
        if ball.rect.x <= 0:
            window.blit(win_r,(100,200))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        

        
        

    display.update()
    clock.tick(FPS)
