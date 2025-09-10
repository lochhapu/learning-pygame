import pygame
from sys import exit

# Initialize pygame modules
pygame.init()

# Set up the main game window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')  # Title of the game window
clock = pygame.time.Clock()  # Clock object to control frame rate

# Load a custom pixel font for text rendering
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)

# Load background surfaces
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Render static text and set it starting position
score = 0
text_surface = test_font.render(f'My Game', False, 'Black')
text_rectangle = text_surface.get_rect(center=(400, 50))

# Load enemy (snail) sprite and set its starting position
snail_surface = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(800, 300))

# Load player sprite and set its starting position
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_rectangle.y -= 100
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_rectangle.y += 100

    # Check keys been held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rectangle.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rectangle.x += 5

    # Draw background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))


    # Draw player character
    screen.blit(player_surface, player_rectangle)

    # --- Snail movement logic ---
    # Move snail left across the screen
    # Reset to the right side once it goes off-screen
    if snail_rectangle.x < -100:
        snail_rectangle.x = 800
    else:
        snail_rectangle.x -= 4
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(text_surface, text_rectangle)

    score = 1

    # Check collision of player and snail
    if player_rectangle.colliderect(snail_rectangle):
        print('Collision detected.')
    else:
        print(0)

    # Update the display and maintain a stable frame rate
    pygame.display.update()
    clock.tick(60)
