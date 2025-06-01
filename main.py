import pygame
import random

# 1. Ініціалізація
pygame.init()

# 2. Екран
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя гра")

# 3. Кольори
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLACK = (0, 0, 0)

# 4. Гравець
player = pygame.Rect(100, 500, 50, 50)
player_speed = 5

# 5. Перешкоди
obstacles = [pygame.Rect(random.randint(200, 750), random.randint(100, 500), 50, 50) for _ in range(5)]
obstacle_speeds = [random.choice([-2, 2]) for _ in range(5)]

# 6. Зона перемоги
win_zone = pygame.Rect(700, 0, 100, 100)

# 7. Годинник
clock = pygame.time.Clock()
running = True

# 8. Головний цикл
while running:
    clock.tick(60)  # 60 кадрів на секунду

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Рух гравця ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    # --- Рух перешкод ---
    for i in range(len(obstacles)):
        obstacles[i].x += obstacle_speeds[i]
        if obstacles[i].left <= 0 or obstacles[i].right >= WIDTH:
            obstacle_speeds[i] *= -1  # змінює напрям руху

    # --- Колізії ---
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            print("Програш!")
            running = False

    if player.colliderect(win_zone):
        print("Перемога!")
        running = False

    # --- Малювання ---
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, win_zone)
    pygame.draw.rect(screen, BLUE, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    pygame.display.flip()

pygame.quit()
