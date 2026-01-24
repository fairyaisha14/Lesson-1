import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sprite Color Change')

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 300, 50, 50)

RED = pygame.Color('red')
BLUE = pygame.Color('blue')

rect1_color = RED
rect2_color = BLUE

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 3000)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            rect1_color = pygame.Color('green') if rect1_color == RED else RED
            rect2_color = pygame.Color('yellow') if rect2_color == BLUE else BLUE

    pygame.draw.rect(screen, rect1_color, rect1)
    pygame.draw.rect(screen, rect2_color, rect2)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
