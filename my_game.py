import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render(f'My Game', False, 'Black')
text_rectangle = text_surface.get_rect(center=(400, 50))
snail_surface = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(800, 300))
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
player_jumped = False

# Game loop
while True:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Player movement: jumping
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and player_jumped == False:
                player_gravity = -20
                player_jumped = True

    # Moving left & right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rectangle.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rectangle.x += 5

    # Snail movement logic
    if snail_rectangle.x < -100:
        snail_rectangle.x = 800
    else:
        snail_rectangle.x -= 6

    # Check collision of player and snail
    if player_rectangle.colliderect(snail_rectangle):
        print('Collision detected.')
    else:
        print(0)

    # Player gravity
    player_rectangle.y += player_gravity
    if (player_jumped == True):
        player_gravity += 1
    if (player_jumped == True and player_rectangle.bottom >= 300):
        player_jumped = False
        player_rectangle.bottom = 300 
        player_gravity = 0

    # Draw
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(player_surface, player_rectangle)
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(text_surface, text_rectangle)

    # Update the display and maintain a stable frame rate
    pygame.display.update()
    clock.tick(60)
