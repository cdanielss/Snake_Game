# -*- coding: utf-8 -*-
import pygame
import pygame.locals
from random import randrange
print("Módulos importados com sucesso")
a = a
try:
    pygame.init()
    print("Start")
except:
    print("Start")

tamanho = 10
largura = 600
altura = 600
placar = 40

preto=(0,0,0)
vermelho = (227,47,34)
verde = (66,204,39)
branco = (255,255,255)
azul=(0,0,255)
prata=(192,192,192)
laranja=(255,69,0)
cinza=(79,79,79)
cinzaClaro=(220,220,220)

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

class Texto:
    def __init__(self, msg, cor, tam):
        self.font = pygame.font.SysFont(None, tam)
        self.texto = self.font.render(msg, True, cor)

    def exibir(self, x, y):
        fundo.blit(self.texto, [x, y])

class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cabeca = [x,y]
        self.comp = 1
        self.cobra = [self.cabeca]
        self.direcao = ""

    def movimento(self, x, y):
        self.cabeca = [x,y]
        self.cobra.append([x,y])
    
    def cresce(self):
        self.comp += 1

    def exibir(self):
        for XY in self.cobra:
            pygame.draw.rect(fundo, verde, [XY[0], XY[1], tamanho, tamanho])
    
    def rastro(self):
        if len(self.cobra) > self.comp:
            del self.cobra[0]
    
    def morreu(self):
        if any(Bloco == self.cabeca for Bloco in self.cobra[:-1]):
            return True
        return False

    def reiniciar(self, x, y):
        self.x = x
        self.y = y
        self.cabeca = [x,y]
        self.comp = 1
        self.cobra = [self.cabeca]
    


class Comida:
    def __init__(self):
        self.x = randrange(0,largura-tamanho, 10)
        self.y = randrange(0,altura-tamanho-placar, 10)
    
    def exibir(self):
        pygame.draw.rect(fundo, vermelho, [self.x, self.y, tamanho, tamanho])
    
    def reposicionar(self):
        self.x = randrange(0,largura-tamanho, 10)
        self.y = randrange(0,altura-tamanho-placar, 10)


class Jogo:
    def __init__(self):
        self.jogando = True
        self.perdeu = False
        self.pos_x = randrange(0, largura-tamanho, 10)
        self.pos_y = randrange(0, altura-tamanho-placar, 10)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.pontos = 0
        self.cobra = Cobra(self.pos_x, self.pos_y)
        self.comida = Comida()
    
    def iniciando(self):
        while self.jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and self.cobra.direcao != "direita":
                        self.cobra.direcao = "esquerda"
                    if event.key == pygame.K_d and self.cobra.direcao != "esquerda":
                        self.cobra.direcao = "direita"
                    if event.key == pygame.K_w and self.cobra.direcao != "baixo":
                        self.cobra.direcao = "cima"
                    if event.key == pygame.K_s and self.cobra.direcao != "cima":
                        self.cobra.direcao = "baixo"
                    if event.key == pygame.K_LEFT and self.cobra.direcao != "direita":
                        self.cobra.direcao = "esquerda"
                    if event.key == pygame.K_RIGHT and self.cobra.direcao != "esquerda":
                        self.cobra.direcao = "direita"
                    if event.key == pygame.K_UP and self.cobra.direcao != "baixo":
                        self.cobra.direcao = "cima"
                    if event.key == pygame.K_DOWN and self.cobra.direcao != "cima":
                        self.cobra.direcao = "baixo"
                    if event.key == pygame.K_SPACE:
                        self.cobra.cresce()
                    if event.key == pygame.K_b:
                        self.jogando = False
                        self.perdeu = True
                        self.perdido()
            
            if self.jogando:
                fundo.fill(branco)
                if self.cobra.direcao == "cima":
                    self.pos_y -= tamanho
                elif self.cobra.direcao == "baixo":
                    self.pos_y += tamanho
                elif self.cobra.direcao == "esquerda":
                    self.pos_x -= tamanho
                elif self.cobra.direcao == "direita":
                    self.pos_x += tamanho
                else:
                    pass

                if self.pos_x == self.comida.x and self.pos_y == self.comida.y:
                    self.comida.reposicionar()
                    self.cobra.cresce()
                    self.pontos += 1
                
                if self.pos_x + tamanho > largura:
                    self.pos_x = 0
                if self.pos_x < 0:
                    self.pos_x=largura-tamanho
                if self.pos_y + tamanho > altura-placar:
                    self.pos_y = 0
                if self.pos_y < 0:
                    self.pos_y= altura-tamanho-placar
                
                self.cobra.movimento(self.pos_x, self.pos_y)
                self.cobra.rastro()

                if self.cobra.morreu():
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()
                
                self.cobra.exibir()

                pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
                textoPlacarSombra = Texto("Total de Pontos: "+str(self.pontos), cinza, 25)
                textoPlacarSombra.exibir(9, altura-31)
                textoPlacar = Texto("Total de Pontos: "+str(self.pontos), branco, 25)
                textoPlacar.exibir(10, altura-30)
                
                self.comida.exibir()

                pygame.display.update()

                relogio.tick(15)
        return 0 

    def perdido(self):
        while self.perdeu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    self.perdeu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.jogando = True
                        self.perdeu = False
                        self.pos_x=randrange(0,largura-tamanho,10)
                        self.pos_y=randrange(0,altura-tamanho-placar,10)
                        self.cobra.direcao = ""
                        self.comida.reposicionar()
                        self.cobra.reiniciar(self.pos_x, self.pos_y)
                        self.velocidade_x=0
                        self.velocidade_y=0
                        self.pontos = 0
                    if event.key == pygame.K_s:
                        self.jogando = False
                        self.perdeu = False
            
            fundo.fill(branco)

            textoPerdeuSombra = Texto("Game Over", cinza, 50)
            textoPerdeuSombra.exibir(64, 29)
            textoPerdeu = Texto("Game Over", verde, 50)
            textoPerdeu.exibir(65, 30)

            
            textoPontuacaoSombra = Texto("Total de Pontos : "+str(self.pontos), cinzaClaro, 30)
            textoPontuacaoSombra.exibir(69, 79)
            textoPontuacao = Texto("Total de Pontos : "+str(self.pontos), preto, 30)
            textoPontuacao.exibir(70, 80)

            
            pygame.draw.rect(fundo, prata, [43, 118, 139, 31])
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            textoContinuar = Texto("Continuar(C)", branco, 30)
            textoContinuar.exibir(50, 125)

            
            pygame.draw.rect(fundo, prata, [188, 118, 79, 31])
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            textoSair = Texto("Sair(S)", branco, 30)
            textoSair.exibir(195, 125)

            pygame.display.update()
        return 0




start = Jogo()
start.iniciando()
pygame.quit()
