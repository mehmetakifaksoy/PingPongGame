import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5

left_paddle = pygame.Rect(10, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(screen_width - 20, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Set up the ball
ball_size = 10
ball_speed = 4
ball_pos = [screen_width // 2, screen_height // 2]
ball_vel = [random.choice([-1, 1]), random.choice([-1, 1])]

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change paddle position
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.y -= paddle_speed
            if event.key == pygame.K_s:
                left_paddle.y += paddle_speed
            if event.key == pygame.K_UP:
                right_paddle.y -= paddle_speed
            if event.key == pygame.K_DOWN:
                right_paddle.y += paddle_speed

    # Keep paddles on the screen
    if left_paddle.top <= 0:
        left_paddle.top = 0
    if left_paddle.bottom >= screen_height:
        left_paddle.bottom = screen_height
    if right_paddle.top <= 0:
        right_paddle.top = 0
    if right_paddle.bottom >= screen_height:
        right_paddle.bottom = screen_height

    # Move the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Bounce the ball off the top and bottom
    if ball_pos[1] <= 0 or ball_pos[1] + ball_size >= screen_height:
        ball_vel[1] = -ball_vel[1]

    # Bounce the ball off the paddles
    if pygame.Rect(0, 0, paddle_width, paddle_height).collidepoint(ball_pos[0] - ball_size, ball_pos[1]):
        ball_vel[0] = -ball_vel[0]
    if pygame.Rect(0, 0, paddle_width, paddle_height).collidepoint(ball_pos[0] + ball_size, ball_pos[1]):
        ball_vel[0] = -ball_vel[0]

    # Draw the screen
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, pygame.Rect(ball_pos[0], ball_pos[1], ball_size, ball_size))
    pygame.display.flip()

# Quit Pygame
pygame.quit()