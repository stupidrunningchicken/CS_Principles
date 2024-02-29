import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_size = 50
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (player_size, player_size))
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 7

# Bullet
bullet_size = 5
bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (bullet_size, bullet_size))
bullet_speed = 10
bullets = []

# Enemy
enemy_size = 50
enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))
enemy_speed = 3
enemies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_bullet(x, y):
    screen.blit(bullet_img, (x, y))

def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def game_loop():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Shooting
        if keys[pygame.K_SPACE]:
            bullet_x = player_x + player_size // 2 - bullet_size // 2
            bullet_y = player_y
            bullets.append([bullet_x, bullet_y])

        # Move and draw bullets
        for bullet in bullets:
            bullet[1] -= bullet_speed
            draw_bullet(bullet[0], bullet[1])

        # Spawn enemies
        if random.randint(1, 100) == 1:
            enemy_x = random.randint(0, WIDTH - enemy_size)
            enemy_y = 0
            enemies.append([enemy_x, enemy_y])

        # Move and draw enemies
        for enemy in enemies:
            enemy[1] += enemy_speed
            draw_enemy(enemy[0], enemy[1])

        # Collision detection
        for bullet in bullets:
            for enemy in enemies:
                if (enemy[0] < bullet[0] < enemy[0] + enemy_size and
                        enemy[1] < bullet[1] < enemy[1] + enemy_size):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10

        # Check if enemies reach the player
        for enemy in enemies:
            if enemy[1] + enemy_size > player_y:
                game_over()

        screen.fill(BLACK)
        draw_player(player_x, player_y)
        draw_score()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()