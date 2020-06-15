import pygame, random
""" Importando todas as funcionalidades """
from pygame.locals import *

""" Inicializando as variaveis de movimento """
UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3

""" Gerar posicoes validas """
def ongrid():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

""" Funcao para fazer que a cobra coma """
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

""" Iniciando o jogo """
pygame.init()
""" Criando a tela """
screen = pygame.display.set_mode((600, 600))
""" Titulo """
pygame.display.set_caption('Snake')

""" A cobra sera uma lista """
snake = [(200, 200), (210, 200), (220, 200)]

""" Criando o visual da cobra """
snakeskin = pygame.Surface((10,10))

""" Adicionando uma cor em RGB"""
snakeskin.fill((53, 153, 20))

mydirection = LEFT 


""" Criando a comida da cobra """
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

""" Posicao aleatoria """
appleposition = ongrid()

""" Limitando o fps da cobra ou seja a velocidade dela """
clock = pygame.time.Clock()

""" Variavel com a velocidade da cobra """
velocidade = 12
""" Forma de Executar o jogo """
while True:
    """ Adicionando os fps da cobra """
    clock.tick(velocidade)

    """ Fazendo a colisao da cobra com a comida"""
    if collision(snake[0], appleposition):
        """ Comida aparece em um novo lugar """
        appleposition = ongrid()
        """ Aumentando a cobra """
        snake.append((0,0))
        """ Aumentando a velocidade """
        velocidade += 1

    """ Facendo o movimento da cobra pegando a posicao anterior """
    for i in range (len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1] )

    """ Movimentos da cobra """
    if mydirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if mydirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if mydirection == RIGTH:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if mydirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    """ Funcao para fechar o jogo """
    for event in pygame.event.get():
        """ Pegar o botao de fechar o jogo """
        if event.type == QUIT:
            pygame.quit()
        """ Lendo as teclas """
        if event.type == KEYDOWN:
            if event.key == K_UP:
                mydirection = UP
            if event.key == K_DOWN:
                mydirection = DOWN
            if event.key == K_RIGHT:
                mydirection = RIGTH
            if event.key == K_LEFT:
                mydirection = LEFT
                
    """ Limpando a tela """
    screen.fill((0,0,0))

    """ Criando a maca em uma posicao aleatoria """
    screen.blit(apple, appleposition)

    """ Criando a cobra na tela """
    for pos in snake:
        screen.blit(snakeskin, pos)

    """ Fazer que o jogo funcione """
    pygame.display.update()