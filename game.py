import sys
import pygame
from pygame.constants import QUIT
positive = lambda a, b : -a-b
negative = lambda a, b : b-a

pygame.init()
size_t = width_t, height_t = 1200, 800
screen = pygame.display.set_mode(size_t)
pic = pygame.image.load('image.PNG')
pic_frame = pic.get_rect()
bounce = [6, 8]
clock = pygame.time.Clock()
while True:
    clock.tick(27)
    screen.fill((150, 150, 150))
    screen.blit(pic, pic_frame)
    pic_frame = pic_frame.move(bounce)
    if pic_frame.left < 0:
        bounce[0] = negative(bounce[0], 1.15)
    if pic_frame.right > width_t:
        bounce[0] = positive(bounce[0], 1.17)
    if pic_frame.top < 0:
        bounce[1] = negative(bounce[1], 1.16)
    if pic_frame.bottom > height_t:
        bounce[1] = positive(bounce[1], 1.14)
    pygame.display.flip()
    for event_close in pygame.event.get():
        if event_close.type == pygame.QUIT:
            pygame.quit()
            sys.exit()