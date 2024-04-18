from random import *
from pygame import *
from time import time as timer

window = display.set_mode((1000, 700))
display.set_caption("Molodie pro pingpongeri'")
window.fill((255, 255, 255))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x ,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):  
        window.blit(self.image, (self.rect.x, self. rect.y))

class player(GameSprite):
   def left(self):
      keys_pressed = key.get_pressed()

      if keys_pressed[K_s] and self.rect.y > -300:
         self.rect.y += self.speed
      if keys_pressed[K_w] and self.rect.y < 800:
         self.rect.y -= self.speed

   def right(self):      
      keys_pressed = key.get_pressed()
      if keys_pressed[K_DOWN] and self.rect.y > -300:
         self.rect.y += self.speed
      if keys_pressed[K_UP] and self.rect.y < 800:
         self.rect.y -= self.speed   

speed_x = 5
speed_y = 5
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('ЛЕВЫЙ ПАЦАНЧИК ПРОИГРАЛ!', True, (200, 0, 0))
font2 = font.Font(None, 35)
lose2 = font2.render('ПРАВЫЙ ПАЦАНЧИК ПРОИГРАЛ!', True, (0, 0, 200))


left_side = player('raketka.jpeg', 0, 350, 50, 150, 6)
right_side = player('raketka.jpeg', 950, 350, 50, 150, 6)
ball = GameSprite('pingpong.jpeg', 500, 350, 50, 50, 0)

finish = False
play = True
clock = time.Clock()
while play:  #игровой цикл
    for e in event.get():
       if e.type == QUIT:
           play = False                

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill((255, 255, 255))
        ball.reset()
        left_side.reset()
        right_side.reset()
        right_side.right()
        left_side.left()

    if sprite.collide_rect(left_side, ball) or sprite.collide_rect(right_side, ball):
        speed_x *= -1
    if ball.rect.y <= 0:   
        speed_y *= -1
    if ball.rect.y >= 650:   
        speed_y *= -1
    if ball.rect.x < -50:
        finish = True
        window.blit(lose1, (200, 200)) 
    if ball.rect.x > 1050:
        finish = True
        window.blit(lose2, (200, 200))       

       
    display.update()
    clock.tick(60)