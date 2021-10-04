import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))

black = (0,0,0)

#фон
rect(screen, (231, 231, 231), (0, 0, 1000, 500))
rect(screen, (255, 255, 255), (0, 500, 1000, 1123))

#избушка
ellipse(screen, (231, 231, 231), (60, 460, 380, 340))
ellipse(screen, black, (60, 460, 380, 340), 3)
rect(screen, (250, 250, 250), (0, 630, 530, 170))
line (screen, (0, 0, 0), (155, 479), (343, 479), 1)
line (screen, (0, 0, 0), (105, 530), (393, 530), 1)
line (screen, (0, 0, 0), (75, 580), (425, 580), 1)
line (screen, (0, 0, 0), (55, 630), (445, 630), 1)
line (screen, (0, 0, 0), (75, 580), (425, 580), 1)

line (screen, (0, 0, 0), (300, 479), (325, 530), 1)
line (screen, (0, 0, 0), (250, 479), (255, 530), 1)
line (screen, (0, 0, 0), (200, 479), (175, 530), 1)

line (screen, (0, 0, 0), (350, 530), (380, 580), 1)
line (screen, (0, 0, 0), (300, 530), (305, 580), 1)
line (screen, (0, 0, 0), (225, 530), (215, 580), 1)
line (screen, (0, 0, 0), (150, 530), (120, 580), 1)

line (screen, (0, 0, 0), (170, 580), (150, 630), 1)
line (screen, (0, 0, 0), (250, 580), (250, 630), 1)
line (screen, (0, 0, 0), (340, 580), (365, 630), 1)

#чукча
ellipse(screen, (228, 223, 219), (560, 600, 140, 90))
ellipse(screen, (145, 124, 112), (550, 660, 150, 260))
#pygame.draw.arc(screen, (0,255,255), [100, 300, 100, 100], 0, 3.14, 100)
ellipse(screen, (173, 158, 148), (577, 616, 105, 60))
ellipse(screen, (228, 219, 219), (594, 630, 70, 39))
rect(screen, (255, 255, 255), (540, 806, 4000, 4000))
ellipse(screen, (145, 124, 112), (580, 780, 40, 75))
ellipse(screen, (145, 124, 112), (640, 780, 40, 75))
rect(screen, (110, 93, 82), (606, 680, 40, 100))
rect(screen, (110, 93, 82), (553, 785, 147, 21))
line (screen, (0, 0, 0), (601, 643), (620, 650), 1)
line (screen, (0, 0, 0), (635, 650), (655, 646), 1)
#ellipse(screen, (0, 0, 0), (577 + 25, 661 - 5, 50, 30), 1)
arc(screen, (0, 0, 0), (577 + 25, 661 - 5, 50, 30), 0.9, 2, 1)
ellipse(screen, (145, 124, 112), (521, 695, 80, 25))
line (screen, (0, 0, 0), (528, 610), (533, 826), 1)



#rect(screen, (255, 255, 255), (0, 0, 400, 400))
#circle(screen, (255, 255, 0), (200, 175), 100)
#polygon(screen, (0, 0, 0), [(100,85), (190,140),
#(185,150), (95,95), (100,85)])
#ellipse(screen, (0, 0, 0), (0, 0, 0, 0))
#line (screen, (0, 0, 0), (0, 0), (0, 0), 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
