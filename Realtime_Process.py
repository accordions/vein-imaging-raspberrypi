import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
size = (640,480)
d = pygame.display.set_mode(size,0)
s = pygame.surface.Surface(size,0,d)
c = pygame.camera.list_cameras()

cam = pygame.camera.Camera(c[0],size)
cam.start()

going = True

# Main Loop
while going:
    if cam.query_image():
        s = cam.get_image(s)
    d.blit(s, (0,0))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == QUIT:
            cam.stop()
            going = False

                # Processing Images with Numpy
last_array = None
diffs = None
s = pygame.surface.Surface(size)
                # inner loop, if statement body:
s = cam.get_image(s)
s2d = pygame.surfarray.array2d(s)
diffs = s2d
if last_array != None:
    diffs = s2d - last_array
last_array = s2d
pygame.surfarray.blit_array(s, diffs)

