import pygame, random

pygame.init()

# Window setup
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background color (black)
BLACK = (0, 0, 0)

# This code is to add the font size and font type
font = pygame.font.SysFont("Times New Roman", 32)

# Words split  using list 
Original_Text=("Lets End The Faith With Puzzle 3")
Text = ["Let's", "End", "The", "Faith", "With", "Puzzle", "3"]

# Puzzle3 class
class Puzzle3:
    def __init__(self, screen, font, words):
        self.screen = screen
        self.font = font
        self.words = words
        self.positions = []
        x_left_right = 50   # start position left and right
        y_up_down = 250     # start position up and down

        for word in self.words:
            self.positions.append((x_left_right, y_up_down))  # This save the last word
            x_left_right += self.font.size(word)[0] + 25

    # Function for  the animation red light
    def red_flash(self, word, pos):#The pos means position like what we did just now in x and y
        base = self.font.render(word, True, (220, 0, 0))#The word render means u convert the text to image because the text now is in string so u need to convert to text and will show it in the main screen
        self.screen.blit(base, pos)

        # Draw aura (dark red) around it
        for horizontal in [-2, -1, 0, 1, 2]:#The horizontal means left and right like the position we did
            for vertical in [-2, -1, 0, 1, 2]:#The vertical means up and down same like the position 
                if horizontal == 0 and vertical == 0:
                    continue
                glow = self.font.render(word, True, (120, 0, 0))#Trur word True just makes the Text more neater at the edge 
                self.screen.blit(glow, (pos[0] + horizontal, pos[1] + vertical))#This actually copy the text that the font.render did and paste in the main page so the player can see
                                            #And all in tuple are the movement that makes it move left,right,up and down

    def draw(self):
        # This code actually loops each words and change the colour the text randomly
        for i, word in enumerate(self.words):#This is used to count the text so that it can loop with colours
            effect_roll = random.random()

            if effect_roll < 0.7:  
                # Grey (70%)
                text = self.font.render(word, True, (150, 150, 150))
                self.screen.blit(text, self.positions[i])
            else:  
                # Red flash (30%)
                self.red_flash(word, self.positions[i])


# Game loop 
run = True#This makes the window to keep running 
puzzle3 = Puzzle3(screen, font, Text)

while run:#This keeps the window open and not close immediately 
    for event in pygame.event.get(): #This checks all the action from the player like mouse, clicking, keyboard
        if event.type == pygame.QUIT:#This is used when player click X button in the  main screen
            run = False#Stop the loop so window can close 

    screen.fill(BLACK)

    puzzle3.draw()

    pygame.display.flip()
    pygame.time.delay(120)

pygame.quit()#This one make sure the x button in the main screen closesAnd this is actually the main code for my Puzzle3 which just say let's end the fate with Puzzle3. So is it correct, uh, terms I use according with the class diagram? Can you check it and tell me whether I use the correct term like the class diagram, like the current room, player, start, all that. I mean, I just have started with the front, like, interior of the page where I put let's end, let's end the Puzzle3 with our fate.
