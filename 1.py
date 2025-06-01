import pygame
pygame.init()

# --- Налаштування вікна та кольору фону ---
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

# --- Швидкість м'яча ---
dx = 3
dy = 3

# --- Початкові координати платформи ---
platform_x = 200
platform_y = 330
move_right = False
move_left = False
game_over = False

# === [1] Клас Area для основних графічних об'єктів ===
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# === [2] ДОДАТИ: Клас Label для виводу тексту (YOU WIN / YOU LOSE) ===
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# === [3] Клас Picture для об’єктів-картинок ===
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


# --- Ініціалізація м'яча та платформи ---
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 30)

# --- Генерація монстрів ---
start_x = 5
start_y = 5
count = 9
monsters = []

for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)
    for i in range(count):
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d)
        x += 55
    count -= 1


# === [4] Основний ігровий цикл ===
while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    # --- Рух платформи ---
    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3

    # --- Рух м'яча ---
    ball.rect.x += dx
    ball.rect.y += dy

    # --- Відскок м’яча від стін ---
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    # === [5] ДОДАТИ: Умова програшу ===
    if ball.rect.y > 350:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU LOSE', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True

    # === [6] ДОДАТИ: Умова виграшу ===
    if len(monsters) == 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU WIN', 60, (0, 200, 0))
        time_text.draw(10, 10)
        game_over = True

    # --- Відскок від платформи ---
    if ball.rect.colliderect(platform.rect):
        dy *= -1

    # === [7] ДОДАТИ: Перевірка зіткнення з монстром ===
    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1

    # --- Малювання об'єктів ---
    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)
