import pygame
import math
import sys

# Created by: Tyler Waltner
# Date: 05/13/2026
# Email: waltnertyler@gmail.com

# Constants
WIDTH = 1200
HEIGHT = 1200
G = 100 # Gravitation constant
S = 100 # Softening factor of collisions
R = 5
D = R * 5

class ball:
    def __init__(self, pos: list[float, float], vx: float, vy: float, r: int, d: float):
        self.pos = pos
        self.vx = vx
        self.vy = vy
        self.r = r
        self.d = d

    def update_pos(self): # Update x/y based off of respective velocities
        self.pos[0] += self.vx
        self.pos[1] += self.vy


def distance(pos1: list[float, float], pos2: list[float, float]) -> float:
    return ((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)**0.5


def update(balls: list[ball]): # Update velocity of each ball
    for i, b1 in enumerate(balls):
        for j, b2 in enumerate(balls):
            if i == j: # Don't wanna pull ourself
                continue
            
            # Mass = Density / Volume (area in this case as we are in 2D)
            m1 = b1.d / (math.pi * b1.r**2)
            m2 = b2.d / (math.pi * b2.r**2)

            dist = distance(b1.pos, b2.pos)

            # Acceleration (m/s^2) = Force / Target mass
            a =  (G  * m2) / dist**2
            
            # Unit vectors (figure out ratio to apply to acceleration)            
            if (dist != S): 
                dx = (b2.pos[0] - b1.pos[0]) / (dist + S)
                dy = (b2.pos[1] - b1.pos[1]) / (dist + S)
            else: # handle rare case dist == S
                dx = (b2.pos[0] - b1.pos[0]) / (dist + S + 0.01)
                dy = (b2.pos[1] - b1.pos[1]) / (dist + S + 0.01)

            # Apply acceleration to velocity
            b1.vx += a * dx
            b1.vy += a * dy

            # Update position
            b1.update_pos()


# Setup
pygame.init() 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_on = True

balls = []


while game_on:
    # Handle events such as mouse events and quitting event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: # On click, get pos of mouse and create ball at location
            pos = list(pygame.mouse.get_pos())
            balls.append(ball(pos, 0, 0, R, D))    
    
    screen.fill((0,0,0)) # Clear screen
    
    for b in balls: # Generate all of our balls
        pygame.draw.circle(screen, (255,255,255), b.pos, b.r)     

    # Update our balls
    update(balls)
    
    pygame.display.flip() # Update display
    
    clock.tick(60) # 60 fps