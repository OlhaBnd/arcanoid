import pygame

pygame.init()
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

racket_x = 200
racket_y = 330

game_over = False

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)   # Створюємо прямокутник з координатами і розміром
        self.fill_color = back                         # Колір заливки (за замовчуванням — колір фону)
        if color:
            self.fill_color = color                    # Якщо передано колір — використовуємо його

    def color(self, new_color):                        # Метод зміни кольору області
        self.fill_color = new_color

    def fill(self):                                    # Малює прямокутник у вікні гри
        pygame.draw.rect(mw, self.fill_color, self.rect)


    def collidepoint(self, x, y):                      # Перевірка зіткнення з точкою (наприклад, мишкою)
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):                       # Перевірка зіткнення з іншим прямокутником
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)  # Викликаємо конструктор батьківського класу
        self.image = pygame.image.load(filename)        # Завантажуємо зображення з файлу

    def draw(self):                                     # Виводить зображення у вікно на позицію прямокутника
        mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)


start_x = 5 
start_y = 5
count = 9
monsters = []

for j in range (3):
    y = start_y + (55*j)
    x = start_x + (27.5*j)
    for i in range(count):
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d)
        x= x+55

    count = count -1


while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)

