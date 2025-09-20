import pygame

import pygame
import sys

# --- Initialize pygame ---
pygame.init()

# --- Window setup ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Haunted Playroom")
clock = pygame.time.Clock()

# --- Fonts ---
font = pygame.font.Font(None, 70)  # size of the font 70

# --- Game states ---
current_level = 3   # (pretend Puzzle 1 and 2 are finished already)

# --- Game loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # close with X button
            running = False

    # Black background
    screen.fill((0, 0, 0))

    # If we are in Puzzle 3 → show welcome text
    if current_level == 3:
        text = font.render("Welcome to Puzzle 3", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

