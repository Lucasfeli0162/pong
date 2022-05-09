import pygame
from pygame.locals import *

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Pong')

timer = pygame.time.Clock()
branco = (255, 255, 255)
preto = (0, 0, 0)

fonte = pygame.font.SysFont(None, 24, bold=True)


class Player1:
    def __init__(self):
        self.largura = 10
        self.altura = 40
        self.x = 0
        self.y = ALTURA // 2 - self.altura // 2
        self.player = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))
        self.pontos = 0

    def draw(self):
        self.player = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))

    def move(self, direction):
        if direction == 1:
            self.y -= 5
        else:
            self.y += 5


class Player2:
    def __init__(self):
        self.largura = 10
        self.altura = 40
        self.x = LARGURA - self.largura
        self.y = ALTURA // 2 - self.altura // 2
        self.player = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))
        self.pontos = 0

    def draw(self):
        self.player = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))

    def move(self, direction):
        if direction == 1:
            self.y -= 5
        else:
            self.y += 5


class Ball:
    def __init__(self):
        from random import choice
        self.largura = 6
        self.altura = 6
        self.x = LARGURA // 2 - self.largura // 2
        self.y = ALTURA // 2 - self.altura // 2
        direcao_bola = choice([1, -1])
        self.speed_x = choice([3, 4, 5]) * direcao_bola
        direcao_bola = choice([1, -1])
        self.speed_y = choice([3, 4, 5]) * direcao_bola
        self.bola = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))

    def restart(self):
        from random import choice
        self.x = LARGURA // 2 - self.largura // 2
        self.y = ALTURA // 2 - self.altura // 2
        direcao_bola = choice([1, -1])
        self.speed_x = choice([3, 4, 5]) * direcao_bola
        direcao_bola = choice([1, -1])
        self.speed_y = choice([3, 4, 5]) * direcao_bola
        self.bola = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))

    def draw(self):
        self.bola = pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura))

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y + self.altura >= ALTURA:
            self.speed_y *= -1
        elif self.y <= 0:
            self.speed_y *= -1


player1 = Player1()
player2 = Player2()
ball = Ball()

while True:
    timer.tick(30)
    tela.fill(preto)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            pygame.quit()

    player1.draw()
    player2.draw()
    ball.update()
    ball.draw()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_w] and player1.y >= 0:
        player1.move(1)
    elif keys_pressed[K_s] and player1.y + player1.altura <= ALTURA:
        player1.move(2)
    if keys_pressed[K_UP] and player2.y >= 0:
        player2.move(1)
    elif keys_pressed[K_DOWN] and player2.y + player1.altura <= ALTURA:
        player2.move(2)

    if player1.player.colliderect(ball.bola) or player2.player.colliderect(ball.bola):
        ball.speed_x *= -1
    if ball.x <= 0:
        player2.pontos += 1
        ball.restart()
    elif ball.x + ball.largura >= LARGURA:
        player1.pontos += 1
        ball.restart()

    text_player_1 = fonte.render(f'Pontos: {player1.pontos}', True, (255, 255, 255))
    text_player_2 = fonte.render(f'Pontos: {player2.pontos}', True, (255, 255, 255))
    tela.blit(text_player_1, (0, 0))
    tela.blit(text_player_2, (LARGURA - text_player_2.get_width() - 5, 0))

    pygame.display.flip()
