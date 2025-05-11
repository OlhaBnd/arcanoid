import pygame                          
pygame.init()                         

back = (200,255,255)                 
mw = pygame.display.set_mode((500,500))  
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
