
import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ping-pong')

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 40)

bg_colour = pygame.Color('grey12')
light_gray = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

# Collisions


while True:
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Visuals
    screen.fill(bg_colour)

    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.ellipse(screen, light_gray, ball)
    pygame.draw.aaline(screen, light_gray, (screen_width/2, 0)(screen_width/2, screen_height))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)