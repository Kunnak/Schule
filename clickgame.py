import random
import pygame
pygame.init()
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
height = 600
width = 600
screen = pygame.display.set_mode((height, width))
score = 0
fails = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Yannicks Klick Game!")
rect_x = random.randint(0, width - 100)
rect_y = random.randint(30, height - 100)
rect_width = 100
rect_height = 100
time_limit = 30.9
start_time = pygame.time.get_ticks()

def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    global score, rect_x, rect_y, start_time, fails
    running = True
    game_over = False
    while running:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if rect_x <= mouse_x <= rect_x + rect_width and rect_y <= mouse_y <= rect_y + rect_height:
                    score += 1
                    rect_x = random.randint(0, width - 100)
                    rect_y = random.randint(0, height - 100)
                else:
                    fails += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_time = pygame.time.get_ticks()
                    fails = 0
                    score = 0
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        remaining_time = time_limit - elapsed_time
        if not game_over:
            display_text(f"Punkte: {score}", GREEN, 10, 10)
            display_text(f"Fails: {fails}", RED, 10, 40)
            display_text(f"Zeit: {int(remaining_time)}", GREEN, width // 2 - 50, 10)
            if remaining_time <= 0:
                game_over = True
        if game_over:
            display_text("Spiel vorbei", RED, width // 2 - 80, height // 2 - 100)
            display_text("Für Neustart 'LEERTASTE'", RED, width // 2 - 140, height // 2 + 50)
            display_text(f"Punkte: {score}", RED, width // 2 - 65, height // 2 - 50)
            display_text(f"Fails: {fails}", RED, width // 2 - 65, height // 2 - 10)
            pygame.display.update()
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_over = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_over = False
                        score = 0
                        fails = 0
                        rect_x = random.randint(0, width - 100)
                        rect_y = random.randint(0, height - 100)
                        start_time = pygame.time.get_ticks()
                        break
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
