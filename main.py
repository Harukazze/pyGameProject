import pygame


class MainMenu:
    def __init__(self):
        self.buttons = []
        self.callback = []
        self.selected_option = 0

    def append_button(self, button, callback):
        self.buttons.append(font.render(button, True, (255, 255, 255)))
        self.callback.append(callback)

    def switch(self, direction):
        if 0 <= self.selected_option + direction <= len(self.buttons) - 1:
            self.selected_option += direction
        else:
            pass

    def select(self):
        print('123')
        self.callback[self.selected_option]()


    def draw(self, surface, posX, posY, padding):
        for i, option in enumerate(self.buttons):
            option_rect = option.get_rect()
            option_rect.topleft = (posX, posY + i * padding)
            if i == self.selected_option:
                pygame.draw.rect(surface, (20, 20, 20), option_rect)
            surface.blit(option, option_rect)


if __name__ == '__main__':

    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 50)

    menu = MainMenu()
    menu.append_button('New Game', lambda: print('123321'))
    menu.append_button('Quit Game', pygame.quit)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu.switch(1)
                elif event.key == pygame.K_s:
                    menu.switch(-1)
                elif event.key == pygame.K_SPACE:
                    menu.select()

        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()
pygame.quit()
