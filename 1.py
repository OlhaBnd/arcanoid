import pygame

pygame.init()  # Ініціалізація pygame

# Задаємо параметри вікна та колір фону
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))  # Створюємо вікно гри
mw.fill(back)  # Заповнюємо фон заданим кольором

clock = pygame.time.Clock()  # Створюємо годинник для управління часом в грі

# Змінні для координат платформи
platform_x = 200
platform_y = 330

# Змінні для напрямків руху м'яча
dx = 3
dy = 3

# Флаги для руху платформи
move_right = False
move_left = False

# Прапорець завершення гри
game_over = False

# Клас для створення областей (прямокутників)
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ Конструктор класу Area для створення прямокутників """
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

# Клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        """ Конструктор класу Picture, що успадковує клас Area """
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

# Створення об'єктів м'яча та платформи
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 30)

# Створення ворогів
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
        x = x + 55
    count = count - 1

# Основний цикл гри
while not game_over:
    mw.fill(back)  # Оновлюємо фон

    # Обробка подій
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

    # Рух платформи
    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3

    # Рух м'яча
    ball.rect.x += dx
    ball.rect.y += dy

    # Перевірка зіткнень м'яча з межами вікна
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    # Перевірка зіткнень м'яча з платформою
    if ball.rect.colliderect(platform.rect):
        dy *= -1

    # Відображення монстрів
    for m in monsters:
        m.draw()

    # Відображення платформи та м'яча
    platform.draw()
    ball.draw()

    pygame.display.update()  # Оновлення відображення екрану
    clock.tick(40)  # Встановлення FPS

pygame.quit()  # Вихід з pygame
