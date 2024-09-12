import pygame
import time 

pygame.init()

screen = pygame.display.set_mode((500,500))

light_off = pygame.image.load("lesson 4/picture/(no bg) light bulb off.png")
light_on = pygame.image.load("lesson 4/picture/(no bg) light bulb on.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
           screen.fill("black")
           screen.blit(light_off,(0,0))
           pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("black")
            screen.blit(light_on,(0,0))
            pygame.display.update()
    
    

