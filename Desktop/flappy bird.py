# flappy.py - Simple Flappy Bird using tkinter (works in IDLE)
import tkinter as tk
import random
import time

# ----- Config -----
WIDTH = 400
HEIGHT = 600
BIRD_SIZE = 20
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_INTERVAL = 1800   # milliseconds between new pipes
PIPE_SPEED = 4         # pixels per frame
GRAVITY = 0.5
FLAP_STRENGTH = -9
FPS = 30

# ----- Game state -----
root = tk.Tk()
root.title("Flappy (tkinter)")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#87CEEB")  # sky blue
canvas.pack()

score_text = canvas.create_text(10, 10, anchor="nw", text="Score: 0", font=("Arial", 16), fill="white")
game_over_text = None

# Bird: represented by a simple oval
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_vy = 0

# Keep pipes as list of dicts: {x, gap_y, id_top, id_bottom, passed}
pipes = []
score = 0
running = True
last_pipe_time = 0

# ----- Functions -----
def reset_game():
    global bird_y, bird_vy, pipes, score, running, last_pipe_time, game_over_text
    canvas.delete("pipe")
    bird_y = HEIGHT // 2
    bird_vy = 0
    pipes = []
    score = 0
    running = True
    canvas.itemconfigure(score_text, text=f"Score: {score}")
    if game_over_text:
        canvas.delete(game_over_text)
    spawn_pipe()  # spawn initial pipe
    root.after(1000, game_loop)  # start game loop

def flap(event=None):
    global bird_vy
    if running:
        bird_vy = FLAP_STRENGTH
    else:
        # Restart when game over
        reset_game()

def spawn_pipe():
    # Create a pipe with random gap y
    gap_y = random.randint(120, HEIGHT - 120)
    x = WIDTH + 10
    top = canvas.create_rectangle(x, 0, x + PIPE_WIDTH, gap_y - PIPE_GAP//2, fill="#228B22", width=0, tags="pipe")
    bottom = canvas.create_rectangle(x, gap_y + PIPE_GAP//2, x + PIPE_WIDTH, HEIGHT, fill="#228B22", width=0, tags="pipe")
    pipes.append({"x": x, "gap_y": gap_y, "top": top, "bottom": bottom, "passed": False})
    # schedule next pipe spawn
    root.after(PIPE_INTERVAL, spawn_pipe)

def game_loop():
    global bird_y, bird_vy, pipes, score, running, last_pipe_time, game_over_text

    if not running:
        return

    # Physics: gravity
    bird_vy += GRAVITY
    bird_y += bird_vy

    # Move pipes left
    for p in list(pipes):
        p["x"] -= PIPE_SPEED
        canvas.move(p["top"], -PIPE_SPEED, 0)
        canvas.move(p["bottom"], -PIPE_SPEED, 0)

        # If pipe passes bird and not counted -> increase score
        if (not p["passed"]) and (p["x"] + PIPE_WIDTH < bird_x):
            p["passed"] = True
            score += 1
            canvas.itemconfigure(score_text, text=f"Score: {score}")

        # Remove pipes off-screen
        if p["x"] + PIPE_WIDTH < -10:
            try:
                canvas.delete(p["top"])
                canvas.delete(p["bottom"])
            except:
                pass
            pipes.remove(p)

    # Draw bird (redraw)
    canvas.delete("bird")
    bird = canvas.create_oval(bird_x - BIRD_SIZE//2, bird_y - BIRD_SIZE//2,
                              bird_x + BIRD_SIZE//2, bird_y + BIRD_SIZE//2,
                              fill="yellow", outline="orange", width=2, tags="bird")

    # Collision detection: ground/ceiling
    if bird_y - BIRD_SIZE//2 <= 0 or bird_y + BIRD_SIZE//2 >= HEIGHT:
        running = False

    # Collision with pipes
    for p in pipes:
        # pipe rectangles coordinates
        x1_top, y1_top, x2_top, y2_top = canvas.coords(p["top"])
        x1_bot, y1_bot, x2_bot, y2_bot = canvas.coords(p["bottom"])
        # bird bbox
        bx1, by1, bx2, by2 = canvas.coords(bird)
        # overlap check
        overlap_top = not (bx2 < x1_top or bx1 > x2_top or by2 < y1_top or by1 > y2_top)
        overlap_bot = not (bx2 < x1_bot or bx1 > x2_bot or by2 < y1_bot or by1 > y2_bot)
        if overlap_top or overlap_bot:
            running = False
            break

    if not running:
        # Show game over
        game_over_text = canvas.create_text(WIDTH//2, HEIGHT//2, text=f"Game Over\nScore: {score}\nPress Space to Restart",
                                            font=("Arial", 20), fill="white", justify="center")
        return

    # tilt bird a bit based on velocity (visual effect)
    # (not rotating the oval, but could change color/shade)
    root.after(int(1000/FPS), game_loop)


# ----- Bind controls -----
root.bind("<space>", flap)
root.bind("<Button-1>", flap)  # click to flap

# ----- Start -----
canvas.create_text(WIDTH//2, 30, text="Flappy (Press Space or Click to flap)", font=("Arial", 12), fill="white")
spawn_pipe()
root.after(1000, game_loop)
root.mainloop()
