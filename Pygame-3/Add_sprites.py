import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Movement Example')

WHITE = pygame.Color('white')
RED = pygame.Color('red')
BLUE = pygame.Color('blue')

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 300, 50, 50)

speed = 5

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        rect2.x -= speed
    if keys[pygame.K_RIGHT]:
        rect2.x += speed
    if keys[pygame.K_UP]:
        rect2.y -= speed
    if keys[pygame.K_DOWN]:
        rect2.y += speed

    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()

