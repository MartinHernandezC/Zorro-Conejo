import pygame
class Assets():
    def __init__(self, x, y, image):
        self.image = pygame.Surface((80, 100))
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.jump_height =0
        self.jump_speed = 10
        self.jumping = False

    def move(self, screen_width, screen_height):
        SPEED = 5
        dx = 0 
        dy = 0

        #obtener eventos
        key = pygame.key.get_pressed()
        #Movimiento
        if key[pygame.K_LEFT]:
            dx = -SPEED
        if key[pygame.K_RIGHT]:
            dx = SPEED

        #Limites de pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            if not self.jumping:
                self.jumping = True
                self.rect.x = -self.rect.width
                self.rect.y = screen_height - 0 - self.rect.height - self.jump_height
        if self.jumping:
            dy -= self.jump_speed
            if self.rect.bottom <= screen_height - 0:
                dy = 0
                self.jumping = False

        #Actualizar Posición
        self.rect.x += dx
        self.rect.y += dy
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image.set_colorkey((0,0,0))