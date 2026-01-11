import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game screen")

screen.fill((255, 255, 255))

rect_color = (255, 0, 0)
rect_width, rect_height = 100, 60
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

font = pygame.font.Font(None, 36)
text = font.render("Hello Pygame!", True, (0, 0, 0))
text_rect = text.get_rect(center=(640 // 2, 100))
screen.blit(text, text_rect)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
