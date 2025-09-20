import pygame, random

pygame.init()

# Window setup
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background color (black)
BLACK = (0, 0, 0)

# This code is to add the font size and font type
font = pygame.font.SysFont("Times New Roman", 50)

# Words split  using list 
Original_Text=("Lets End The Faith With Puzzle 3")
Text = ["Let's", "End", "The", "Faith", "With", "Puzzle", "3"]


# make an empty list to store where each word goes
positions = []
x_left_right = 50   # start position left and right
y_up_down = 250     # start position up and down

for word in words:
    positions.append((x_left_right, y_up_down))  # This save the last word
    x_left_right += font.size(Text)[0] + 25

# Function for  the animation red light
def red_flash(Text, pos):#The pos means position like what we did just now in x and y
    base = font.render(word, True, (220, 0, 0))#The word render means u convert the text to image because the text now is in string so u need to convert to text and will show it in the main screen

    # Draw aura (dark red) around it
for horizontal in [-2, -1, 0, 1, 2]:#The horizontal means left and right like the position we did
    for vertical in [-2, -1, 0, 1, 2]:#The vertical means up and down same like the position 
        if horizontal == 0 and vertical == 0:
            continue
        glow = font.render(word, True, (120, 0, 0))#Trur word True just makes the Text more neater at the edge 
        screen.blit(glow, (pos[0] + horizontal, pos[1] + vertical))#This actually copy the text that the font.render did and paste in the main page so the player can see
								   #And all in tuple are the movement that makes it move left,right,up and down


# Game loop 
run = True#This makes the window to keep running 
while run:#This keeps the window open and not close immediately 
    for event in pygame.event.get(): #This checks all the action from the player like mouse, clicking, keyboard
        if event.type == pygame.QUIT:#This is used when player click X button in the  main screen
            run = False#Stop the loop so window can close 

    screen.fill(BLACK)

    # This code actually loops each words and change the colour the text randomly
    for i, Text in enumerate(Text):#This is used to count the text so that it can loop with colours
        effect_roll = random.random()

        if effect_roll < 0.8:
            # Normal white (most of the time)
            text = font.render(word, True, (255, 255, 255))
            screen.blit(Text, positions[i])

        elif effect_roll < 0.95:
            # Dim ghostly
            text = font.render(Text, True, (150, 150, 150))
            screen.blit(Text, positions[i])

        else:
            # Rare blood red aura flash
            draw_red_flash(Text, positions[i])

    pygame.display.flip()
    pygame.time.delay(120)

pygame.quit()#This one make sure the x button in the main screen closes 
