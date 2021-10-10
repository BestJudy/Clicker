import pygame, sys

#setting up pygame
pygame.init()

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Clicker")

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0
score = 0

BLACK = (56,245,876)

score_font = pygame.font.SysFont('Constantia', 30)

def draw_window():
    pygame.draw.rect(win, BLACK, score_font)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill((255,255,255))
            score += 1
            print(score)

    current_time = pygame.time.get_ticks()

    if current_time - button_press_time > 2000:
        screen.fill((0,0,0))

    pygame.display.flip()
    clock.tick(60)    
