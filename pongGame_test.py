import unittest
import tkinter as tk
from pongGame import Ball,Paddle

class TestPongGame(unittest.TestCase):
    # move methode from Ball class
    def test_ball_movement(self):
        canvas = tk.Canvas(tk.Tk(), width=500, height=400)
        ball = Ball(canvas, 250, 200)

        initial_position = canvas.coords(ball.id)[:2]
        ball.move()
        updated_position = canvas.coords(ball.id)[:2]

        self.assertNotEqual(initial_position, updated_position)

        ball.move()
        ball.move()
        ball.move()
        ball.move()
        final_position = canvas.coords(ball.id)[:2]
        self.assertNotEqual(updated_position, final_position)

        # Test negative y_speed
        ball.y_speed = 3
        ball.move()
        reversed_position = canvas.coords(ball.id)[:2]
        self.assertNotEqual(final_position, reversed_position)

    #bounce_wall() methode from Ball class
    def test_ball_bounce_wall(self):
        canvas = tk.Canvas(tk.Tk(), width=500, height=400)
        ball = Ball(canvas, 490, 200)

        initial_x_speed = ball.x_speed
        ball.bounce_wall()
        updated_x_speed = ball.x_speed

        self.assertNotEqual(initial_x_speed, updated_x_speed)

        # checking the bounce wall speeds
        ball.bounce_wall()
        ball.bounce_wall()
        ball.bounce_wall()
        final_x_speed = ball.x_speed
        self.assertNotEqual(updated_x_speed, final_x_speed)

    #Paddle clasee methods test case.
    def test_paddle_movement(self):
        canvas = tk.Canvas(tk.Tk(), width=500, height=400)
        paddle = Paddle(canvas, 200, 390)

        initial_position = canvas.coords(paddle.id)[:2]
        paddle.move_right(None)
        paddle.move()
        updated_position = canvas.coords(paddle.id)[:2]

        self.assertNotEqual(initial_position, updated_position)

        paddle.move_left(None)
        paddle.move()
        paddle.move()
        paddle.move()
        final_position = canvas.coords(paddle.id)[:2]
        self.assertNotEqual(updated_position, final_position)

        # Test negative x_speed
        paddle.x_speed = -5
        paddle.move()
        reversed_position = canvas.coords(paddle.id)[:2]
        self.assertNotEqual(final_position, reversed_position)

        # Test when x_speed is 0
        paddle.x_speed = 0
        paddle.move()
        stationary_position = canvas.coords(paddle.id)[:2]
        self.assertEqual(reversed_position, stationary_position)


    #paddle class methods test cases.
    def test_paddle_boundary_movement(self):
        canvas = tk.Canvas(tk.Tk(), width=500, height=400)
        paddle = Paddle(canvas, 490, 390)

        initial_position = canvas.coords(paddle.id)[:2]
        paddle.move_right(None)
        paddle.move()
        updated_position = canvas.coords(paddle.id)[:2]

        # To nsure that the paddle does not move beyond the right boundary
        self.assertEqual(initial_position, updated_position)

        paddle.move_left(None)
        paddle.move()
        paddle.move()
        paddle.move()
        final_position = canvas.coords(paddle.id)[:2]
        self.assertEqual(updated_position, final_position)

        # Test negative x_speed
        paddle.x_speed = -5
        paddle.move()
        reversed_position = canvas.coords(paddle.id)[:2]
        self.assertEqual(final_position, reversed_position)

        # Test when x_speed is 0
        paddle.x_speed = 0
        paddle.move()
        stationary_position = canvas.coords(paddle.id)[:2]
        self.assertEqual(reversed_position, stationary_position)

        # Test when x_speed exceeds left boundary
        paddle.x_speed = -10
        paddle.move()
        beyond_boundary_position = canvas.coords(paddle.id)[:2]
        self.assertEqual(stationary_position, beyond_boundary_position)

    #Paddle class methods test case
    def test_paddle_initial_position(self):
        canvas = tk.Canvas(tk.Tk(), width=500, height=400)
        paddle = Paddle(canvas, 200, 390)

        # To ensure that the paddle is created with the correct initial position
        self.assertEqual(canvas.coords(paddle.id), [200, 390, 300, 400])

        paddle = Paddle(canvas, 350, 390)
        self.assertEqual(canvas.coords(paddle.id), [350, 390, 450, 400])

        paddle = Paddle(canvas, 100, 390)
        self.assertEqual(canvas.coords(paddle.id), [100, 390, 200, 400])


if __name__ == '__main__':
    unittest.main()
