import pygame

# Clase que gestiona el spritesheet
class Spritesheet:
    def __init__(self, filename):
        # Carga el spritesheet completo
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    # Método para extraer un sprite dado un rectángulo (x, y, ancho, alto)
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return sprite

# Clase Jugador con animación
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet):
        super().__init__()
        self.spritesheet = spritesheet
        self.image = self.spritesheet.get_sprite(0, 0, 32, 32)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.current_frame = 0
        self.frames = []
        self.load_frames()

    # Cargamos los 6 sprites del movimiento
    def load_frames(self):
        for i in range(6):  # Asume que están en la primera fila del spritesheet
            frame = self.spritesheet.get_sprite(i * 32, 0, 32, 32)
            self.frames.append(frame)

    # Actualizamos el sprite actual para crear la animación
    def update(self, keys):
        self.current_frame += 0.2  # Controla la velocidad de la animación
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]

        # Movimiento simple del jugador
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

# Cargar spritesheet
spritesheet = Spritesheet('Pink_Monster_Walk_6.png')

# Crear el jugador usando los sprites
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
