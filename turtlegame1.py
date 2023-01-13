import turtle 
import pygame
pygame.init

background_colour = (0, 0, 0)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('G')
screen.fill(background_colour)
pygame.display.flip()
running = True
  
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False