import pygame

# Clase que gestiona un spritesheet
class Spritesheet:
    def __init__(self, filename):
        # Cargamos el archivo de imagen del spritesheet
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    # Método para extraer un sprite dado un rectángulo (x, y, ancho, alto)
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return sprite

# Clase Jugador usando un sprite extraído del spritesheet
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet):
        super().__init__()
        # Extraemos el sprite del jugador desde el spritesheet
        self.image = spritesheet.get_sprite(0, 0, 32, 32)  # Asume que el sprite del jugador está en (0, 0) con tamaño 64x64
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Carga el spritesheet
spritesheet = Spritesheet('Pink_Monster_Walk_6.png')

# Creamos el jugador usando un sprite del spritesheet
player = Player(100, 100, spritesheet)
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
