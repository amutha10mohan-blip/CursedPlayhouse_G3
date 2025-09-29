import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pulsating Neon Heart with Image")

# Colors
BLACK = (0, 0, 0)
NEON_PINK = (255, 20, 147)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load heart image (replace 'heart.png' with your file later)
# Make sure the image is in the same folder as this script
try:
    heart_image = pygame.image.load("heart.png").convert_alpha()
    use_image = True
except:
    heart_image = None
    use_image = False
    print("No heart image found. Using drawn heart instead.")

# Animation variable
t = 0

# Function to draw heart shape if no image
def draw_heart(surface, x, y, size, color):
    points = []
    for angle in range(0, 360, 1):
        rad = math.radians(angle)
        a = size * (16 * math.sin(rad)**3)
        b = -size * (13*math.cos(rad) - 5*math.cos(2*rad) - 2*math.cos(3*rad) - math.cos(4*rad))
        points.append((x + a, y + b))
    pygame.draw.polygon(surface, color, points)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Pulsate effect
    pulsate = 1 + 0.1 * math.sin(t)
    
    # Flickering/dimming effect
    flicker = 150 + 105 * math.sin(t * 2 + math.sin(t * 0.5))
    heart_color = (flicker, 20, 147)

    if use_image:
        # Scale the image for pulsating
        scale = pulsate
        img_width = int(heart_image.get_width() * scale)
        img_height = int(heart_image.get_height() * scale)
        heart_scaled = pygame.transform.scale(heart_image, (img_width, img_height))

        # Create flicker glow effect
        tint = pygame.Surface((img_width, img_height), pygame.SRCALPHA)
        tint.fill((flicker, 20, 147, 50))  # RGBA with alpha for glow
        heart_scaled.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

        # Draw on screen
        x = WIDTH // 2 - img_width // 2
        y = HEIGHT // 2 - img_height // 2
        screen.blit(heart_scaled, (x, y))
    else:
        # Draw mathematical heart if no image
        heart_size = 10 * pulsate
        draw_heart(screen, WIDTH // 2, HEIGHT // 2, heart_size, heart_color)

    pygame.display.flip()

    # Inc time
    t += 0.05

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # 60 FPS

pygame.quit()

