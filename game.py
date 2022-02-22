import time
import sys
import os
import pygame
from pygame import mixer
pygame.init()
pygame.font.init() 
win = pygame.display.set_mode((500,500))
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Game")
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1,0.0)
font = pygame.font.SysFont('Comic Sans MS', 50)
font2 = pygame.font.SysFont('Comic Sans MS', 30)
game_over = font.render('GAME OVER', True, (255, 255, 255))
retry = font2.render('Press enter to restart',True,(255,255,255))
player_alive = True
x = -0
y = 450
ex = 50
ey = 450
width = 40
height = 40
vel = 20
run = True  
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel    
    if x > 450:
        x = 450 
    if x < -0:
        x = -0 
    if keys[pygame.K_RETURN] and player_alive == False:
        pygame.quit()
        run = False
        os.system("python game.py")
    win.fill((0,0,0))
    if player_alive == True:  
        obstacle = pygame.draw.rect(win, (255,0,0), (ex, ey, width, height)) 
        player = pygame.draw.rect(win, (255,255,255), (x, y, width, height))   
    if player.colliderect(obstacle):
        player_alive = False
        pygame.mixer.music.stop()
        win.blit(game_over,(100,200))
        win.blit(retry,(100,300))
    pygame.display.update() 
    
pygame.quit()