import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Brown Circle Clicker")
running = True
score = 0
increase = 1

font = pygame.font.SysFont(None, 36)

def render_cookie():
    cookie_surf = pygame.Surface((600, 600))
    cookie_surf.fill((0, 0, 0))
    pygame.draw.circle(cookie_surf, (100, 40, 0), (300, 300), 200)
    cookie_surf.set_colorkey((0, 0, 0))

    cookie_mask = pygame.mask.from_surface(cookie_surf)

    text = font.render("Click the cookie!", False, (255, 255, 255))
    cookie_surf. blit(text, (0, 0))

    text = font.render(f"Score : {score}", False, (255, 255, 255))
    cookie_surf. blit(text, (600 - text.get_width(), 0))

    return cookie_surf, cookie_mask





while running:
    cookie_surf, cookie_mask = render_cookie()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            offset = (mouse_pos[0] - 0, mouse_pos[1] - 0)
            if cookie_mask.overlap(pygame.mask.Mask((1, 1), fill=True), offset):
                score += increase

    screen.fill((150, 200, 255))

    screen.blit(cookie_surf, (0, 0))

    pygame.display.update()
