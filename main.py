import pygame


global passive

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Brown Circle Clicker")
running = True
score = 0
increase = 1
passive = 0

font = pygame.font.SysFont(None, 36)


class MenuItem():
    def __init__(self, x, y, text, img=None, font=None, value=0):
        self.img = pygame.Surface((400, 100))
        self.img.set_colorkey((0, 0, 0))
        self.back = pygame.Surface((400, 100))
        self.back.fill((0, 0, 100))
        self.back.set_alpha(255)

        self.img.blit(self.back, (0, 0))

        self.rect = pygame.Rect(0, 0, 400, 100)
        self.rect.topleft = (x, y)
        self.text = text
        self.font = font
        self.value = value
        self.color = (0, 0, 0)

    def render_item_text(self):
        return self.font.render(self.text, True, self.color)

    def render_value_text(self):
        return self.font.render(f"Cost: {self.value}", True, self.color)

    def render(self):
        self.img = pygame.Surface((400, 100))
        self.img.set_colorkey((0, 0, 0))
        self.back = pygame.Surface((400, 100))
        self.back.fill((0, 0, 100))
        self.back.set_alpha(255)

        self.img.blit(self.back, (0, 0))

    def draw(self):
        self.render()
        self.img.blit(self.render_item_text(), (0, 0))
        self.img.blit(self.render_value_text(), (0, 50))

        win = pygame.display.get_surface()
        win.blit(self.img, self.rect.topleft)

    def get_clicked(self, pos):
        return self.rect.collidepoint(pos)



def render_cookie():
    global passive, score, increase
    cookie_surf = pygame.Surface((600, 600))
    cookie_surf.fill((0, 0, 0))
    pygame.draw.circle(cookie_surf, (100, 40, 0), (300, 300), 200)
    cookie_surf.set_colorkey((0, 0, 0))

    cookie_mask = pygame.mask.from_surface(cookie_surf)

    text = font.render("Click the cookie!", False, (255, 255, 255))
    cookie_surf. blit(text, (0, 0))

    text = font.render(f"Score : {score}", False, (255, 255, 255))
    cookie_surf. blit(text, (600 - text.get_width(), 0))

    text = font.render(f"Gain : {increase}", False, (255, 255, 255))
    cookie_surf.blit(text, (600 - text.get_width(), text.get_height()))

    text = font.render(f"Passive : {passive}", False, (255, 255, 255))
    cookie_surf.blit(text, (600 - text.get_width(), text.get_height() * 2))

    return cookie_surf, cookie_mask


def render_menu():
    menu_surf = pygame.Surface((400, 600))
    menu_surf.set_colorkey((0, 0, 0))

    menu_back = pygame.Surface((400, 600))
    menu_back.fill((0, 0, 0))
    menu_back.set_alpha(100)

    text = font.render("Menu", True, (255, 255, 255))
    menu_surf.blit(text, (200 - text.get_width() // 2, 0))

    return menu_surf, menu_back

menu = []
menu.append(MenuItem(600, 30, "Increase Gain!", None, font, 10))
menu.append(MenuItem(600, 135, "Increase Passive!", None, font, 20))
menu.append(MenuItem(600, 240, "Super Increase Gain!", None, font, 100))

while running:
    cookie_surf, cookie_mask = render_cookie()
    menu_surf, menu_back = render_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            offset = (mouse_pos[0] - 0, mouse_pos[1] - 0)
            if cookie_mask.overlap(pygame.mask.Mask((1, 1), fill=True), offset):
                score += increase
            for index, item in enumerate(menu):
                if menu[index].get_clicked(mouse_pos):
                    if menu[index].text == "Increase Gain!":
                        if score >= menu[index].value:
                            score -= menu[index].value
                            increase += 1
                            menu[index].value += menu[index].value
                    elif menu[index].text == "Increase Passive!":
                        if score >= menu[index].value:
                            score -= menu[index].value
                            passive += 1
                            menu[index].value += menu[index].value
                    elif menu[index].text == "Super Increase Gain!":
                        if score >= menu[index].value:
                            score -= menu[index].value
                            increase += 10
                            menu[index].value += menu[index].value

    if pygame.time.get_ticks() % 1000 == 0:
        score += passive

    screen.fill((150, 200, 255))

    screen.blit(cookie_surf, (0, 0))
    screen.blit(menu_back, (600, 0))
    screen.blit(menu_surf, (600, 0))

    for item in menu:
        item.draw()

    pygame.display.update()
