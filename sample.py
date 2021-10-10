import pygame
from pygame.locals import *
import sys
import random
import os
os.chdir('C:\\Users\\91930\\OneDrive\\Desktop')
fps=32
width=289
height=511
screen=pygame.display.set_mode((width,height))
sprite={}
ground=height*0.8
sound={}
player="bird.png"
background="screen1.jpg"
pipe="pipe.png"
base="base.jpg"
def welcomescreen():
    playerx=int(width/5)
    palyery=int((height-sprite["player"].get_height())/2)
    msgx=int((width-sprite["message"].get_width())/2)
    msgy=int(height*0.13)
    basex=0
    while True:
        for event in pygame.event.get():
            if (event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.type == K_SPACE or event.key== K_UP):
                return
            else:
                #screen.blit(sprite["backgroung"],(0,0))
                screen.blit(sprite["player"], (playerx,palyery))
                screen.blit(sprite["message"], (msgx,msgy))
                screen.blit(sprite["base"], (basex,ground))
                pygame.display.update()
                fpsclock.tick(fps)
def main_game():
    score=0
    playerx = int(width / 5)
    playery = int(width / 2)
    basex=0
    newpipe1 = getrandompipe()
    newpipe2 = getrandompipe()
    upperPipes = [
        {'x': width + 200, 'y': newpipe1[0]['y']},
        {'x': width + 200 + (width / 2), 'y': newpipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': width + 200, 'y': newpipe1[1]['y']},
        {'x': width + 200 + (width / 2), 'y': newpipe2[1]['y']},
    ]
    def getrandompipe():
        pipe_height=sprite['pipe'][0].get_height()
        offset=height/3
        y2=offset+random.randrange(0,int(height-sprite['base'].get_height()-1.2*offset))
        pipex=width+10
        y1=pipe_height-y2+offset
        pipe=[
            {'x':pipex,'y':-y1},
            {'x':pipex,'y':y2}
        ]
        return pipe


if __name__=="__main__":
    pygame.init()
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption("bach sakte ho to bach lo")
    sprite["number"]=(
        pygame.image.load("0.png").convert_alpha(),
        pygame.image.load("1.png").convert_alpha(),
        pygame.image.load("2.png").convert_alpha(),
        pygame.image.load("3.png").convert_alpha(),
        pygame.image.load("4.png").convert_alpha(),
        pygame.image.load("5.png").convert_alpha(),
        pygame.image.load("6.png").convert_alpha(),
        pygame.image.load("7.png").convert_alpha(),
        pygame.image.load("8.png").convert_alpha(),
        pygame.image.load("9.png").convert_alpha()
    )
    sprite["message"]=pygame.image.load("message.png")
    sprite["base"]=pygame.image.load(base)
    sprite["pipe"]=((pygame.transform.rotate(pygame.image.load(pipe),180)),pygame.image.load(pipe))
    sprite["player"]=pygame.image.load(player)
    while True:
        welcomescreen()
        main_game()

