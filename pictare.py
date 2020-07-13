import pygame
pygame.init()

frstr = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pictare")

ceas = pygame.time.Clock()

class desen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.latura = 10
        self.culoare = True
        self.image = pygame.Surface((self.latura, self.latura))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.vit = 4
    def update(self):
        self.taste = pygame.key.get_pressed()
        if self.taste[pygame.K_UP]:
            self.rect.y -= self.vit
        if self.taste[pygame.K_DOWN]:
            self.rect.y += self.vit
        if self.taste[pygame.K_LEFT]:
            self.rect.x -= self.vit
        if self.taste[pygame.K_RIGHT]:
            self.rect.x += self.vit
        if self.taste[pygame.K_SPACE]:
            self.image.fill((0, 0, 0))
            self.culoare = False
        if self.taste[pygame.K_RETURN]:
            self.image.fill((255, 0, 0))
            self.culoare = True
        if self.taste[pygame.K_w]:
            self.latura += 1
            self.image = pygame.Surface((self.latura, self.latura))
            if self.culoare:
                self.image.fill((255, 0, 0))
        if self.taste[pygame.K_s] and self.latura > 0:
            self.latura -= 1
            self.image = pygame.Surface((self.latura, self.latura))
            if self.culoare:
                self.image.fill((255, 0, 0))
        if self.taste[pygame.K_r]:
            self.image = pygame.Surface((10, 10))
            if self.culoare:
                self.image.fill((255, 0, 0))
            self.latura = 10

toate = pygame.sprite.Group()
dsn = desen()
toate.add(dsn)

rulare = True
while rulare:
    ceas.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rulare = False

    toate.update()
    toate.draw(frstr)
    pygame.display.flip()

pygame.quit()
