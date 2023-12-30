# Pong Game using Tkinter
# Developed with reference to the official Tkinter documentation:
# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
from tkinter import simpledialog
import random

# Class representing the Pong game
class PongGame:
    def __init__(self, master, width, height):
        # Initialize the game window
        self.master = master
        self.width = width
        self.height = height

        # Create a canvas for drawing game elements
        self.canvas = tk.Canvas(master, width=width, height=height, bg='black')
        self.canvas.pack()

        # Create instances of the Ball and Paddle classes
        self.ball = Ball(self.canvas, width / 2, height / 2)
        self.paddle = Paddle(self.canvas, width / 2 - 50, height - 20)

        # Bind keyboard events to paddle movement
        self.canvas.bind_all('<KeyPress-Left>', self.paddle.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.paddle.move_right)

        # Initialize game timer
        self.timer = 0 

    # Method to update the game state
    def update(self):
        self.timer += 0.01 
        self.update_timer_display()

        self.ball.move()
        self.paddle.move()

        if self.ball.hit_paddle(self.paddle):
            self.ball.bounce()

        if self.ball.hit_wall():
            self.ball.bounce_wall()

        if self.ball.out_of_bounds():
            self.game_over()

        # Schedule the next update after 10 milliseconds
        self.master.after(10, self.update)

    # Method to update the timer display on the canvas
    def update_timer_display(self):
        self.canvas.delete("timer_text")
        timer_text = f"Time: {self.timer:.2f} s"
        self.canvas.create_text(
            self.width - 70, 20,
            text=timer_text,
            font=("Helvetica", 12),
            fill="white",
            anchor=tk.NE,
            tags="timer_text"
        )

    # Method to display a game-over message and close the window
    def game_over(self):
        score_message = f"Game Over\nTime: {self.timer:.2f} s"
        simpledialog.messagebox.showinfo("Game Over", score_message)
        self.master.destroy()

# Class representing the game ball
class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # Create an oval representing the ball on the canvas
        self.id = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='white')
        # Set initial random speed for the ball
        self.x_speed = random.choice([-3, -2, 2, 3])
        self.y_speed = -3

    # Method to move the ball and handle collisions
    def move(self):
        self.canvas.move(self.id, self.x_speed, self.y_speed)
        pos = self.canvas.coords(self.id)

        # Bounce if the ball hits the top or bottom wall
        if pos[1] <= 0 or pos[3] >= 400:
            self.y_speed = -self.y_speed

    # Method to check if the ball hits the paddle
    def hit_paddle(self, paddle):
        paddle_pos = paddle.get_position()
        ball_pos = self.canvas.coords(self.id)

        return (ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and
                ball_pos[3] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3])

    # Method to make the ball bounce off the paddle
    def bounce(self):
        self.y_speed = -3

    # Method to check if the ball hits the left or right wall
    def hit_wall(self):
        pos = self.canvas.coords(self.id)
        return pos[0] <= 0 or pos[2] >= 500

    # Method to make the ball bounce off the left or right wall
    def bounce_wall(self):
        self.x_speed = -self.x_speed

    # Method to check if the ball goes out of bounds at the bottom
    def out_of_bounds(self):
        pos = self.canvas.coords(self.id)
        return pos[3] >= 400

# Class representing the game paddle
class Paddle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # Create a rectangle representing the paddle on the canvas
        self.id = canvas.create_rectangle(x, y, x + 100, y + 10, fill='white')
        self.x_speed = 0

    # Method to move the paddle to the left
    def move_left(self, event):
        self.x_speed = -5

    # Method to move the paddle to the right
    def move_right(self, event):
        self.x_speed = 5

    # Method to move the paddle within the canvas boundaries
    def move(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.x_speed >= 0 and pos[2] + self.x_speed <= 500:
            self.canvas.move(self.id, self.x_speed, 0)

    # Method to get the current position of the paddle
    def get_position(self):
        return self.canvas.coords(self.id)

# Class representing a play button to start the game
class PlayButton:
    def __init__(self, master, game):
        self.master = master
        self.game = game

        # Create a button with a callback to start the game
        self.play_button = tk.Button(master, text="Play", command=self.start_game)
        self.play_button.pack()

    # Method to disable the play button and start the game
    def start_game(self):
        self.play_button.config(state=tk.DISABLED)  
        self.game.canvas.focus_set()  
        self.game.update() 

# Main program entry point
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Pong Game")
    root.resizable(False, False)

    # Initialize the PongGame and PlayButton instances
    game = PongGame(root, 500, 400)
    play_button = PlayButton(root, game)

    # Start the Tkinter event loop
    root.mainloop()
