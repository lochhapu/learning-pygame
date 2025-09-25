import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = int(current_time / 1000)
    score_surface = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('The Running Alien')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
snail_surface = pygame.image.load('graphics/snail/snail_1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(800, 300))
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
player_jumped = False
game_active = False
start_time = 0
just_started = True

# Game loop
while True:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # Player movement: jumping
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and player_jumped == False:
                    player_gravity = -20
                    player_jumped = True
        else:
            # Start or restart game
            player_rectangle.x = 80
            if event.type == pygame.KEYDOWN:
                game_active = True
                just_started = False
                snail_rectangle.x = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        # Snail movement logic
        if snail_rectangle.x < -100:
            snail_rectangle.x = 800
        else:
            snail_rectangle.x -= 6

        # Player gravity
        player_rectangle.y += player_gravity
        if (player_jumped == True):
            player_gravity += 1
        if (player_jumped == True and player_rectangle.bottom >= 300):
            player_jumped = False
            player_rectangle.bottom = 300 
            player_gravity = 0
        # Check collision of player and snail
        if player_rectangle.colliderect(snail_rectangle):
            game_active = False
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(player_surface, player_rectangle)
        screen.blit(snail_surface, snail_rectangle)
        score = display_score()

    # Start page state
    elif just_started:
        player_rectangle.x = 350
        snail_rectangle.x = 250
        title = test_font.render('The Running Alien', False, (64, 64, 64))
        title_rect = title.get_rect(center = (400, 100))
        text = test_font.render('Press any key to start.', False, (64, 64, 64))
        text_rect = text.get_rect(center = (400, 165))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(player_surface, player_rectangle)
        screen.blit(snail_surface, snail_rectangle)
        screen.blit(title, title_rect)
        screen.blit(text, text_rect)

    # Game over state
    else:
        score_text = test_font.render(f'Your score: {score}', False, (64, 64, 64))
        score_rect = score_text.get_rect(center = (400, 150))
        text = test_font.render('Press any key to start again.', False, (64, 64, 64))
        text_rect = text.get_rect(center = (400, 200))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(player_surface, player_rectangle)
        screen.blit(snail_surface, snail_rectangle)
        screen.blit(score_text, score_rect)
        screen.blit(text, text_rect)

    # Update the display and maintain a stable frame rate
    pygame.display.update()
    clock.tick(60)
