import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2 - 40/2
y = altura/2 - 50/2

y_azul= randint(40,600)
x_azul= randint(50,430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do: ')

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    x = max(0, min(x,largura - 40))
    y = max(0, min(y, altura - 50))

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50 ))
    ret_azul = pygame.draw.rect(tela,(0,0,255), (x_azul,y_azul,40,50))


    if ret_vermelho.colliderect(ret_azul):
        x_azul=randint(40,600)
        y_azul=randint(50,430)
        pontos = pontos + 1

    tela.blit(texto, (400, 30))
    pygame.display.update()

