import pygame

# Clase Jugador
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = (0, 128, 255)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Clase Enemigo
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = (255, 0, 0)

    def move_towards(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += 1
        if self.rect.y < player.rect.y:
            self.rect.y += 1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

player = Player(100, 100)
enemy = Enemy(200, 200)

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

    # Enemigo se mueve hacia el jugador
    enemy.move_towards(player)

    player.draw(screen)
    enemy.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
