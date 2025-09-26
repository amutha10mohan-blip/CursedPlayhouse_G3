import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background, Sprite, and Joystick")

# Load background (static PNG)
background = pygame.image.load("bedroom.png")   # <-- your background PNG
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load sprite (your pixel character PNG)
player = pygame.image.load("character.png")     # <-- your sprite PNG
player = pygame.transform.scale(player, (64, 64))  # resize if needed

# Sprite starting position
x, y = 100, 100
speed = 5

# Initialize Joystick
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Joystick detected:", joystick.get_name())
else:
    joystick = None
    print("⚠️ No joystick detected! Falling back to keyboard.")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard fallback
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Joystick movement
    if joystick:
        axis_x = joystick.get_axis(0)  # left/right stick axis
        axis_y = joystick.get_axis(1)  # up/down stick axis

        # Apply movement (analog stick gives values from -1.0 to 1.0)
        x += int(axis_x * speed)
        y += int(axis_y * speed)

    # Draw everything
    screen.blit(background, (0, 0))   # draw background
    screen.blit(player, (x, y))       # draw player sprite
    pygame.display.update()

pygame.quit()
