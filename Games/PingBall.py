import pygame as pg
import sys

SCREEN_SIZE = [640, 480]
WIDTH = SCREEN_SIZE[0]
HEIGHT = SCREEN_SIZE[1]

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (200, 200, 0)

BRICK_WIDTH = 60
BRICK_HEIGHT = 15

PADDLE_WIDTH = 60
PADDLE_HEIGHT = 12

BALL_SIZE = 16
BALL_RADIUS = int(BALL_SIZE / 2)

MAX_PADDLE_X = WIDTH - PADDLE_WIDTH
MAX_BALL_X = WIDTH - BALL_SIZE
MAX_BALL_Y = HEIGHT - BALL_SIZE

PADDLE_Y = HEIGHT - PADDLE_HEIGHT - 10

STATE_WAIT = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3


class PingBall:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption("PingBall")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 30)

        self.init_game()

    def init_game(self):
        self.lives = 3
        self.score = 0
        self.state = STATE_WAIT

        self.paddle = pg.Rect(300, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = pg.Rect(300, PADDLE_Y - BALL_SIZE, BALL_SIZE, BALL_SIZE)
        # self.ball_move = [5, -5]

        self.create_bricks()

    def create_bricks(self):
        Y = 35
        self.bricks = []
        for i in range(7):
            X = 35
            for j in range(8):
                self.bricks.append(pg.Rect(X, Y, BRICK_WIDTH, BRICK_HEIGHT))
                X += BRICK_WIDTH + 10
            Y += BRICK_HEIGHT + 5

    def draw_bricks(self):
        for brick in self.bricks:
            pg.draw.rect(self.screen, yellow, brick)

    def check_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.paddle.left -= 5
            if self.paddle.left < 0:
                self.paddle.left = 0
        if keys[pg.K_RIGHT]:
            self.paddle.left += 5
            if self.paddle.left > MAX_PADDLE_X:
                self.paddle.left = MAX_PADDLE_X
        if keys[pg.K_SPACE] and self.state == STATE_WAIT:
            self.ball_move = [5, -5]
            self.state = STATE_PLAYING
        if keys[pg.K_r] and (self.state == STATE_GAME_OVER or self.state == STATE_WON):
            self.init_game()

    def move_ball(self):
        self.ball.left += self.ball_move[0]
        self.ball.top += self.ball_move[1]

        if self.ball.left <= 0:
            self.ball.left = 0
            self.ball_move[0] = -self.ball_move[0]
        elif self.ball.left >= MAX_BALL_X:
            self.ball.left = MAX_BALL_X
            self.ball_move[0] = -self.ball_move[0]

        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_move[1] = -self.ball_move[1]

    def handle_collisions(self):
        for brick in self.bricks:
            if self.ball.colliderect(brick):
                self.score += 1
                self.ball_move[1] = -self.ball_move[1]
                self.bricks.remove(brick)
                break

        if len(self.bricks) == 0:
            self.state = STATE_WON

        if self.ball.colliderect(self.paddle):
            self.ball.top = PADDLE_Y - BALL_SIZE
            self.ball_move[1] = -self.ball_move[1]
        elif self.ball.top > self.paddle.top:
            self.lives -= 1
            if self.lives > 0:
                self.state = STATE_WAIT
            else:
                self.state = STATE_GAME_OVER

    def show_stats(self):
        if self.font:
            font_surface = self.font.render("SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, white)
            self.screen.blit(font_surface, (205, 5))

    def show_message(self, message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message, False, white)
            x = (SCREEN_SIZE[0] - size[0]) / 2
            y = (SCREEN_SIZE[1] - size[1]) / 2
            self.screen.blit(font_surface, (x, y))

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill(black)
            self.check_input()

            if self.state == STATE_PLAYING:
                self.move_ball()
                self.handle_collisions()
            elif self.state == STATE_WAIT:
                self.ball.left = self.paddle.left + self.paddle.width / 2
                self.ball.top = self.paddle.top - self.ball.height
                self.show_message("PRESS SPACE TO LAUNCH THE BALL")
            elif self.state == STATE_GAME_OVER:
                self.show_message("GAME OVER. PRESS R TO PLAY AGAIN")
            elif self.state == STATE_WON:
                self.show_message("YOU WON! PRESS R TO PLAY AGAIN")

            self.draw_bricks()
            pg.draw.rect(self.screen, blue, self.paddle)
            pg.draw.circle(self.screen, white, (self.ball.left + BALL_RADIUS, self.ball.top + BALL_RADIUS), BALL_RADIUS)
            self.show_stats()

            self.clock.tick(60)
            pg.display.update()


if __name__ == "__main__":
    PingBall().run()
