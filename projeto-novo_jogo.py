import pygame
from pygame.display import set_caption
from pygame.locals import *

# inicializar
pygame.init()

tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display,set_caption("Brick Breaker")

tamanho_bola = 15
bola = pygame.Rect(100,500,tamanho_bola,tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0,750,tamanho_jogador,20)

qtde_blocos_linha = 8
qtde_linhas_blocos = 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

def criar_blocos(qtde_blocos_linha, qtde_linha_blocos):
    bloco = []
    #criar blocos
    return qtde_total_blocos

cores = {
    "branco": (255,255,255),
    
}
# criar funções do jogp


# desenhar

# criar loop infinito