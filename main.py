import pygame
import math
import time
import sys

# Created by: Tyler Waltner
# Date: 05/15/2026
# Email: waltnertyler@gmail.com

# Constants
WIDTH = 1200
HEIGHT = 1000
G = 10 # Gravitation constant
S = 100 # Softening factor of collisions
R = 5 # Radius
D = R * 5 # Density
B = 0.7 # Bounce factor (how much momentum ball keeps when bouncing from wall)


class ball:
    def __init__(self, pos: list[float, float], old_pos: list[float, float], r: int, d: float):
        self.pos = pos
        self.old_pos = old_pos
        self.r = r
        self.d = d
        # Mass = Density * Volume (area in this case as we are in 2D)
        self.m = self.d * math.pi * self.r**2
        self.ax = 0
        self.ay = 0

    def update_pos(self, dt: float): # Update x/y using Verlet integration 
        # calculate velocity from previous position 
        vx = self.pos[0] - self.old_pos[0]
        vy = self.pos[1] - self.old_pos[1]
        
        # Update old position
        self.old_pos = [self.pos[0], self.pos[1]]

        # Verlet integration
        # New Position = cur_pos + velocity + (acceleration * dt^2)
        self.pos[0] = self.pos[0] + vx + self.ax * dt**2
        self.pos[1] = self.pos[1] + vy + self.ay * dt**2

        # Handle Wall Collision
        # X-axis walls
        if self.pos[0] < self.r: # left wall
            self.pos[0] = self.r # teleport to pos
            self.old_pos[0] = self.pos[0] + vx * B # old pos = current pos plus velocity & neg Bounce factor
        elif self.pos[0] > WIDTH - self.r:
            self.pos[0] = WIDTH - self.r
            self.old_pos[0] = self.pos[0] + vx * B
        
        # Y-axis walls
        if self.pos[1] < self.r: # top wall
            self.pos[1] = self.r
            self.old_pos[1] = self.pos[1] + vy * B
        elif self.pos[1] > HEIGHT - self.r:
            self.pos[1] = HEIGHT - self.r
            self.old_pos[1] = self.pos[1] + vy * B

        # reset acceleration
        self.ax = 0
        self.ay = 0



def dist_sq(pos1: list[float, float], pos2: list[float, float]) -> float:
    return (pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2 + S


def update(balls: list[ball], dt: float): # Update velocity of each ball
    for i, b1 in enumerate(balls):
        for j, b2 in enumerate(balls):
            if i == j: # Don't wanna pull ourself
                continue
            
            dst_sq = dist_sq(b1.pos, b2.pos)
            dst = dst_sq**0.5

            # Acceleration (m/s^2) = Force / Target mass
            a = (G  * b2.m) / dst_sq
            
            # Unit vectors (delta_axis / distance) (figure out ratio to apply to acceleration)            
            if (dst != 0): 
                dx = (b2.pos[0] - b1.pos[0]) / dst
                dy = (b2.pos[1] - b1.pos[1]) / dst
            else: # handle rare case dist == S
                dx = (b2.pos[0] - b1.pos[0]) / dst + 0.1
                dy = (b2.pos[1] - b1.pos[1]) / dst + 0.1

            # Update acceleration
            b1.ax += a * dx
            b1.ay += a * dy

    for b in balls:
        # Update positions 
        b.update_pos(dt)


def main():
    # Pygame setup
    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # array to hold all balls
    balls = []

    # Inquire if user wants sun in middle of display
    sun = False

    while True:
        i = input('Would you like a high density circle to be present in the middle of the display? Type "Y" or "N"\n')

        if i.upper() == "Y" or i.lower() == 'yes':
            sun = True
            break
        elif i.upper() == "N" or i.lower() == 'no':
            sun = False
            break
        else: 
            print('Please enter a valid input, either "Y" or "N"')
    
    # variable to track if sun is stationary
    stationary = False

    # if sun, add sun to balls
    if sun:
        # Inquire user on desired density of ball
        density = 0

        while True:
            i = input("Please enter a desired density (int) of high density circle: (Minimum value recommended > 100)\n")    
            try:
                density = int(i)
                break
            except: 
                print('Please enter a valid input, must be INTEGER!!! Ex: "1000"')
        
        balls.append(ball([WIDTH/2, HEIGHT/2], [WIDTH/2, HEIGHT/2], 10, density))

        while True:
            i = input('Would you like the high density circle to be stationary? (Not affected by gravity, immovable object) Type "Y" or "N"\n')

            if i.upper() == "Y" or i.lower() == 'yes':
                stationary = True
                break                
            elif i.upper() == "N" or i.lower() == 'no':
                stationary = False
                break
            else: 
                print('Please enter a valid input, either "Y" or "N"')


    while True:
        # Actual time passed, convert to seconds (0.016 == 60fps)
        dt = clock.tick(60) / 1000.0

        # Handle events such as mouse events and quitting event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # On click, get pos of mouse and create ball at location
                pos = list(pygame.mouse.get_pos())
                balls.append(ball(pos, pos[:], R, D))    
        
        screen.fill((0,0,0)) # Clear screen
        
        if stationary: # if stationary, set position and old_pos of center ball to center
            balls[0].pos = [WIDTH/2, HEIGHT/2]
            balls[0].old_pos = [WIDTH/2, HEIGHT/2]

        for b in balls: # Generate all of our balls
            pygame.draw.circle(screen, (255,255,255), b.pos, b.r)

        # Update our balls
        update(balls, dt)
        
        pygame.display.flip() # Update display


main()