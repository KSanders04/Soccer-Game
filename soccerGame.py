# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:55:35 2023

@author: sport
"""

#Initialize
import pygame

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((610, 415))
    pygame.display.set_caption("Soccer!")

    #Entities
    #load background image to soccer field
    background = pygame.image.load("soccerField.jpg")
    background = background.convert()

    #load an image
    soccer = pygame.image.load("soccerball.png")
    soccer = soccer.convert_alpha()
    soccer = pygame.transform.scale(soccer, (25, 25))

    # set up some soccer variables
    soccer_x = 0
    soccer_y = 200
    #set up velocity for soccer ball
    velocity_x = 5
    velocity_y = 5
    
    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # Update the ball position
        soccer_x += velocity_x
        soccer_y += velocity_y

       
        #check boundaries
        if soccer_x < 0:
            velocity_x *= -1
        if soccer_x + soccer.get_width() > screen.get_width():
            velocity_x *= -1
        if soccer_y < 0:
            velocity_y *= -1
        if soccer_y + soccer.get_height() > screen.get_height():
            velocity_y *= -1

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(soccer, (soccer_x, soccer_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()