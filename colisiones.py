import pygame

# Clase Jugador
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Clase Objeto
class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))

player = Player(100, 100)
obstacle = Obstacle(200, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.move(1, 0)
    if keys[pygame.K_UP]:
        player.move(0, -1)
    if keys[pygame.K_DOWN]:
        player.move(0, 1)

    # Detección de colisión
    if player.rect.colliderect(obstacle.rect):
        font = pygame.font.Font(None, 36)
        text = font.render("Colision detectada", True, (255, 0, 0))
        screen.blit(text, (100, 100))

    pygame.draw.rect(screen, (0, 128, 255), player.rect)
    pygame.draw.rect(screen, (255, 0, 0), obstacle.rect)

    pygame.display.flip()

pygame.quit()
