import pygame

FPS = 60
clock = pygame.time.Clock()

current_time = 0


class MainMenu:
    def __init__(self):
        self.buttons = []
        self.callback = []
        self.selected_option = 0

    def delete_buttons(self):
        self.buttons = []
        self.callback = []

    def append_button(self, button, callback):
        self.buttons.append(font.render(button, True, (255, 255, 255)))
        self.callback.append(callback)

    def switch(self, direction):
        if 0 <= self.selected_option + direction <= len(self.buttons) - 1:
            self.selected_option += direction
        else:
            pass

    def select(self):
        self.callback[self.selected_option]()

    def draw(self, surface, posX, posY, padding):
        for i, option in enumerate(self.buttons):
            option_rect = option.get_rect()
            option_rect.topleft = (posX, posY + i * padding)
            if i == self.selected_option:
                pygame.draw.rect(surface, (20, 20, 20), option_rect)
            surface.blit(option, option_rect)


class Game:
    def __init__(self):
        screen.fill((255, 255, 255))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        self.bullets = 0


def make_card():
    menu.delete_buttons()
    game = Game()
    screen.blit(player.image, player.rect)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 50)

    menu = MainMenu()
    menu.append_button('New Game', make_card)
    menu.append_button('Quit Game', pygame.quit)

    player = Player(100, 100, 'chelspistoletom.jpg')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if menu.buttons != []:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        menu.switch(1)
                    elif event.key == pygame.K_s:
                        menu.switch(-1)
                    elif event.key == pygame.K_SPACE:
                        menu.select()
            else:
                text_time = 0
                bullets_text = font.render(str(player.bullets), True, (0, 0, 0))
                bullet_image = pygame.image.load("Bullet.png").convert_alpha()
                bullet_image = pygame.transform.scale(bullet_image, (30, 30))
                screen.blit(bullets_text, [850, 0])
                screen.blit(bullet_image, [870, 0])
                screen.blit(player.image, player.rect)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    player.rect.y -= 10
                elif keys[pygame.K_s]:
                    player.rect.y += 10
                elif keys[pygame.K_d]:
                    player.rect.x += 10
                elif keys[pygame.K_a]:
                    player.rect.x -= 10
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if player.bullets == 0:
                        i_need_more_bullets = font.render('I need more bullets!', True, (0, 0, 0))
                        screen.blit(i_need_more_bullets, [player.rect[0], player.rect[1] - 50])
                        text_time = pygame.time.get_ticks()
                current_time = pygame.time.get_ticks()


        pygame.display.update()
        menu.draw(screen, 100, 100, 75)
        clock.tick(FPS)

pygame.quit()
