import sys, os
andr = None
try:
    import android
    andr = True
except ImportError:
    andr = False
try:
    import pygame
    import sys
    import pygame
    import random
    import time
    from pygame.locals import *
    pygame.init() 
    fps = 1 / 3
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height), FULLSCREEN if andr else 0)
    width, height = pygame.display.get_surface().get_size()
    while True:
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        time.sleep(fps)
except Exception as e:
    open('error.txt', 'w').write(str(e))
    