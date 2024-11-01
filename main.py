import pygame
from agent import *
WIDTH = 800
HEIGHT = 600
black = (0,0,0)
white = (255,255,252)
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#load image 
obstacle = pygame.image.load("img/stone.jpg")
#sizing or scalling the image to fit
obstacle = pygame.transform.scale(obstacle,(35,35))
#image of the agent
agent = pygame.image.load("img/rat.jpg")
agent = pygame.transform.scale(agent,(35,35))

target = pygame.image.load("img/house.jpg")
target = pygame.transform.scale(target,(35,35))

agent1 = Agent(agent,0,0)

last = pygame.time.get_ticks()
#0 represent the obstacles
# 1 represent the paths
#2 is the target
grid = [[3, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
 [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
 [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
 [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
 [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
 [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
 [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
 [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
 [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
 [1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((white))
    #a for loop to separeate the lines in 40s
    for x in range (0,HEIGHT,40):
        # x axis will always be 0
        pygame.draw.line(screen, black,(0,x), (WIDTH,x))
    for y in range (0,WIDTH,40):
        #y is the height and always constant
        pygame.draw.line(screen, black,(y,0), (y,HEIGHT))
        
    for i in range(0,15):
        for j in range(0,20):
            #take row multiply by 40 to have my y
            x = j * 40
            #take the column multiply by 40 to have x
            y = i * 40
            if grid[i][j] == 0:
                #adding an obstacle to our xy cordinate
                screen.blit(obstacle,(x,y))
    
            elif grid[i][j] == 2:
                screen.blit(target,(x,y))
    current_time=pygame.time.get_ticks()
    
    if current_time-last >300 and not agent1.target:
        agent1.move(grid)
        last=current_time
    agent1.draw(screen)
    
    
    pygame.display.update()
pygame.quit()
