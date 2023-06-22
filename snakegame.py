import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the initial snake position and direction
snake_pos = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'

# Set up the initial food position
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawned = True

# Set up the game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[0][1] -= 10
    elif direction == 'DOWN':
        snake_pos[0][1] += 10
    elif direction == 'LEFT':
        snake_pos[0][0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0][0] += 10

    # Check for collision with food
    if snake_pos[0] == food_pos:
        food_spawned = False
        snake_pos.append([0, 0])

    # Check for collision with boundaries or self
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        game_over = True
    for block in snake_pos[1:]:
        if block == snake_pos[0]:
            game_over = True

    # Spawn new food if necessary
    if not food_spawned:
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawned = True

    # Clear the screen
    window.fill(BLACK)

    # Draw the snake
    for block in snake_pos:
        pygame.draw.rect(window, GREEN, pygame.Rect(block[0], block[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(15)

# Quit the game
pygame.quit()
