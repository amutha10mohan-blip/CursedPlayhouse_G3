# ================================
# Music Box Melody – Starter Shell
# Title screen + Room 1 layout
# No external assets required
# ================================

import pygame  # import the pygame library for 2D game functions
import sys     # import sys so we can exit the program cleanly

# --- Initialize pygame and basic settings ---
pygame.init()  # start pygame's internal modules

WIDTH, HEIGHT = 800, 450  # set the window size (16:9 is nice for most screens)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # create the game window surface
pygame.display.set_caption("The Cursed Playhouse – Room 1: Music Box")  # set window title
CLOCK = pygame.time.Clock()  # create a clock to control FPS

# --- Colors (RGB) ---
PASTEL_WALL = (245, 235, 255)      # soft pastel background for the room
PASTEL_FLOOR = (235, 225, 240)     # slightly darker pastel for a floor area
INK = (30, 30, 40)                 # dark text color
MUTED = (90, 90, 110)              # muted UI color for outlines
ACCENT = (120, 90, 200)            # accent color for title and highlights
WHITE = (255, 255, 255)            # white for contrast
GLASS = (210, 230, 255)            # light bluish color for window pane
CAT_COLOR = (220, 170, 120)        # placeholder color for the cat sprite box
BOX_COLOR = (200, 190, 220)        # placeholder color for the music box sprite box

# --- Fonts (use pygame's default if system font not found) ---
TITLE_FONT = pygame.font.SysFont(None, 64)   # big title font
UI_FONT = pygame.font.SysFont(None, 28)      # smaller UI font for tips
ROOM_FONT = pygame.font.SysFont(None, 36)    # medium font for room labels

# --- Game States (simple state machine) ---
STATE_TITLE = "TITLE"   # title screen state
STATE_ROOM1 = "ROOM1"   # room 1 state (playroom)
game_state = STATE_TITLE  # start at the title screen

# --- Layout Rects for Room 1 (placeholders for later sprites) ---
floor_rect = pygame.Rect(0, int(HEIGHT * 0.72), WIDTH, int(HEIGHT * 0.28))  # floor area at bottom

window_outer = pygame.Rect(WIDTH - 260, 40, 220, 140)   # window frame position
window_inner = window_outer.inflate(-20, -20)           # inner glass pane area

music_box_rect = pygame.Rect(100, floor_rect.top - 90, 120, 80)  # music box placeholder on a “shelf”
cat_rect = pygame.Rect(60, floor_rect.top - 170, 90, 90)         # talking cat placeholder sitting nearby

# --- Shadow Progress Placeholder (0–3 for future) ---
shadow_stage = 0  # will be increased later when mistakes happen (not used yet in starter)

# --- Helper: draw the title screen ---
def draw_title_screen():
    SCREEN.fill(PASTEL_WALL)  # fill background with pastel wall color

    # draw a soft floor strip so the title screen matches room vibe
    pygame.draw.rect(SCREEN, PASTEL_FLOOR, floor_rect)  # draw the floor rectangle

    # render and place the main title
    title_surf = TITLE_FONT.render("The Cursed Playhouse", True, ACCENT)  # create title text surface
    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 3))   # center it
    SCREEN.blit(title_surf, title_rect)  # draw title on the screen

    # render and place the room label subtitle
    subtitle = ROOM_FONT.render("Room 1 — Music Box Melody", True, INK)  # create subtitle surface
    sub_rect = subtitle.get_rect(center=(WIDTH // 2, title_rect.bottom + 35))  # place under title
    SCREEN.blit(subtitle, sub_rect)  # draw subtitle

    # draw a simple “press key to start” hint
    hint = UI_FONT.render("Press SPACE or CLICK to start", True, MUTED)  # hint text
    hint_rect = hint.get_rect(center=(WIDTH // 2, sub_rect.bottom + 40))  # place hint under subtitle
    SCREEN.blit(hint, hint_rect)  # draw hint

# --- Helper: draw Room 1 (playroom shell) ---
def draw_room1():
    SCREEN.fill(PASTEL_WALL)  # pastel wall background

    pygame.draw.rect(SCREEN, PASTEL_FLOOR, floor_rect)  # draw floor area

    # draw a simple window (future: overlay shadow images by stage)
    pygame.draw.rect(SCREEN, MUTED, window_outer, border_radius=8)  # window frame outline
    pygame.draw.rect(SCREEN, GLASS, window_inner, border_radius=6)  # window glass area

    # window crossbars for style
    mid_x = window_inner.x + window_inner.w // 2  # vertical bar x position
    mid_y = window_inner.y + window_inner.h // 2  # horizontal bar y position
    pygame.draw.line(SCREEN, WHITE, (mid_x, window_inner.y + 6), (mid_x, window_inner.bottom - 6), 2)  # vertical bar
    pygame.draw.line(SCREEN, WHITE, (window_inner.x + 6, mid_y), (window_inner.right - 6, mid_y), 2)  # horizontal bar

    # placeholder villain shadow intensity (stage not yet used for visuals here)
    stage_text = UI_FONT.render(f"Shadow Stage: {shadow_stage}", True, MUTED)  # show stage value for debugging
    SCREEN.blit(stage_text, (window_outer.x, window_outer.bottom + 6))  # place debug text near window

    # draw a shelf line under the music box to suggest depth
    shelf_y = music_box_rect.bottom + 6  # y position for shelf line
    pygame.draw.line(SCREEN, MUTED, (music_box_rect.x - 40, shelf_y), (music_box_rect.right + 40, shelf_y), 3)  # shelf line

    # draw the music box placeholder
    pygame.draw.rect(SCREEN, BOX_COLOR, music_box_rect, border_radius=6)  # music box body
    lid_rect = pygame.Rect(music_box_rect.x, music_box_rect.y - 14, music_box_rect.w, 14)  # simple lid
    pygame.draw.rect(SCREEN, BOX_COLOR, lid_rect, border_radius=6)  # draw lid
    label = UI_FONT.render("Music Box", True, INK)  # label text for the box
    SCREEN.blit(label, (music_box_rect.x + 10, music_box_rect.y + 26))  # place label on box

    # draw the talking cat placeholder
    pygame.draw.rect(SCREEN, CAT_COLOR, cat_rect, border_radius=12)  # cat body box
    cat_text = UI_FONT.render("Talking Cat", True, INK)  # label text for cat
    SCREEN.blit(cat_text, (cat_rect.x + 2, cat_rect.y + cat_rect.h + 6))  # label under cat

    # draw a simple dialogue bubble (static placeholder for now)
    bubble_rect = pygame.Rect(cat_rect.right + 14, cat_rect.y - 10, 260, 70)  # dialogue bubble rectangle
    pygame.draw.rect(SCREEN, WHITE, bubble_rect, border_radius=12)  # bubble background
    pygame.draw.rect(SCREEN, MUTED, bubble_rect, 2, border_radius=12)  # bubble outline
    bubble_text = UI_FONT.render("“Can you fix the melody?”", True, INK)  # sample line
    SCREEN.blit(bubble_text, (bubble_rect.x + 12, bubble_rect.y + 20))  # draw the line inside the bubble

    # draw a small on-screen tip for controls
    tip = UI_FONT.render("Press ESC to return to Title", True, MUTED)  # tip text
    SCREEN.blit(tip, (14, 14))  # draw tip at top-left

# --- Main loop (handles states, input, and drawing) ---
def main():
    global game_state  # allow changing the state variable inside this function

    running = True  # main loop flag
    while running:  # loop until the user quits
        for event in pygame.event.get():  # process all events (keyboard, mouse, quit)
            if event.type == pygame.QUIT:  # user clicked the window close button
                running = False  # end the loop

            if game_state == STATE_TITLE:  # inputs on the title screen
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # SPACE to start
                    game_state = STATE_ROOM1  # switch to Room 1
                if event.type == pygame.MOUSEBUTTONDOWN:  # any mouse click also starts
                    game_state = STATE_ROOM1  # switch to Room 1

            elif game_state == STATE_ROOM1:  # inputs inside Room 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # ESC to go back to title
                    game_state = STATE_TITLE  # return to title

        # --- Drawing per state ---
        if game_state == STATE_TITLE:  # if we are on the title screen
            draw_title_screen()  # draw title UI
        elif game_state == STATE_ROOM1:  # if we are inside Room 1
            draw_room1()  # draw room layout and placeholders

        pygame.display.flip()  # update the window with everything we’ve drawn this frame
        CLOCK.tick(60)  # cap the frame rate at ~60 FPS for smoothness

    # when loop ends, quit pygame and exit the program
    pygame.quit()  # cleanly shut down pygame modules
    sys.exit()     # exit the Python script

# --- Entry point (so the game runs when you press F5 in IDLE) ---
if __name__ == "__main__":  # only run main() if this file is executed directly
    main()  # start the game loop
